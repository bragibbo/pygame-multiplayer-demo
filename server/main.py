import json
import socket
import sys

from game_manager import *

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    gm = GameManager()
    while True:
        req, address = sock.recvfrom(1024)
        print("Received: {}".format(req))

        json_req = json.loads(req)
        clients, res = gm.handle_request(json_req, address)
        for conn in clients:
            json_res = json.dumps(res)
            sock.sendto(bytes(json_res, 'utf-8'), conn)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt was caught")
        print("Exiting...")
        sys.exit(0)
