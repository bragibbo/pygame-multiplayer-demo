import json
import socket


class Network:
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_id = ""

    def connect(self):
        msg = json.dumps({"state": "CONNECT"})
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.sendto(bytes(msg, 'utf-8'), (self.UDP_IP, self.UDP_PORT))
        data, addr = self.sock.recvfrom(1024)
        print("received message: %s" % data)
        if len(data) > 0:
            json_data = json.loads(data)
            if self.client_id == "":
                self.client_id = json_data["client_id"]
        # Now that we have established a connection, let's set the socket to be non-blocking
        self.sock.setblocking(False)

    def send_message(self, message):
        message["client_id"] = self.client_id
        formatted_string = json.dumps(message)
        self.sock.sendto(bytes(formatted_string, 'utf-8'), (self.UDP_IP, self.UDP_PORT))

    def receive_message(self):
        try:
            data, addr = self.sock.recvfrom(1024)
        except BlockingIOError:
            pass  # No new data. Reuse old data
        else:
            print("received message: %s" % data)
            if len(data) > 0:
                json_data = json.loads(data)
                return json_data
        return None
