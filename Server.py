# -*- coding: utf-8 -*-
import SocketServer

"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""
clients={}

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def handle(self):
        """
        This method handles the connection between a client and the server.login
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request
        global clients
        clients[self] = self.ip
    
        # Loop that listens for messages from the client
        while True:
            try:
                recieved_string = self.connection.recv(4096)
                for client in clients:
                    if client is not clients[self]:
                        client.connection.sendall(recieved_string)
            except:
                print("connection closed.")
                self.connection.close()
                clients.pop(self,None)
                break

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = '37.187.53.31', 800
    print ('Server running...')

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
