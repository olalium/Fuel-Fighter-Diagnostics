import SocketServer

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = str(self.request.recv(1024)).strip("b'")
        print("{} wrote:".format(self.client_address[0]))
        print(str(self.data))
        # just send back the same data, but upper-cased
        self.request.sendall(bytes(self.data.upper(), 'ascii'))

if __name__ == "__main__":
    HOST, PORT = "10.22.27.156", 800

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
