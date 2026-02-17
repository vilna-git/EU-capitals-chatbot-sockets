
#Oleksandra Kovalenko Homework 2 (server TCP)

"""
TCP Chat-Bot Server (reliable)
Listens on a TCP socket and accepts connections;
for each client, receives line-delimited messages
Replies with a simple answer
"""
import argparse, socket, threading
from common import answer

def handle_client(conn, addr):
    with conn:
        try:
            conn.sendall(b"Welcome to Synyi Voron, your European capitals TCP based chat bot.\n")
        except Exception:
            return
        buffer = b""
        while True:
            data = conn.recv(1024)
            if not data:
                break
            buffer += data
            # TCP is a byte stream; split on newlines to get complete messages
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                msg = line.decode("utf-8", errors="ignore").strip()
                if not msg:
                    continue
                resp = answer(msg)
                try:
                    conn.sendall((resp + "\n").encode("utf-8"))
                except Exception:
                    return
                if resp.lower().startswith("bye"):
                    return

def serve(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Allow quick restart during testing
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        print(f"Server listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()

def main():
    p = argparse.ArgumentParser(description="TCP chat-bot server")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=12000)
    args = p.parse_args()
    serve(args.host, args.port)

if __name__ == "__main__":
    main()
