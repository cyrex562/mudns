import socketserver

class ThreadedDNSRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(0xffff)

        # parse the request
        


        cur_thread = threading.current_thread()

        # generate a response

        response = bytes("", "utf-8")
        self.request.sendall(response)


class ThreadedDNSServer(
    socketserver.ThreadingMixIn, 
    socketserver.UDPServer):
    pass

def run():
    try:
        HOST, PORT = "localhost", 53
        server = ThreadedDNSServer(
            (HOST, PORT), 
            ThreadedDNSRequestHandler)
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print("server loop running in thread:", server_thread.name)
    except KeyboardInterrupt as ki:
        server.shutdown()
        server.server_close()
    

if __name__ == "__main__":
    run()

