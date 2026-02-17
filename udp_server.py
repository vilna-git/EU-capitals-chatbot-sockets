
#Oleksandra Kovalenko Homework 2 (server UDP)

"""
UDP Chat-Bot Server (unreliable)
Uses UDP socket; for each datagram, sends a reply to the sender
each message is independent -> no connection state
"""
import argparse, socket
from common import answer

def serve(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Server listening on {host}:{port}")
        while True:
            data, client_addr = s.recvfrom(2048)
            msg = data.decode("utf-8", errors="ignore").strip()
            resp = answer(msg)
            s.sendto((resp + "\n").encode("utf-8"), client_addr)

def main():
    p = argparse.ArgumentParser(description="UDP chat-bot server")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=12000)
    args = p.parse_args()
    serve(args.host, args.port)

if __name__ == "__main__":
    main()
