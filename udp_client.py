
#Oleksandra Kovalenko Homework 2 (client UDP)

"""
UDP Chat-Bot Client
Connects to server using UDP and sends a message per user input
Waits for a single reply (can be lost; press Enter to resend if needed)
"""
import argparse, socket, sys

def main():
    p = argparse.ArgumentParser(description="UDP chat-bot client")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=12000)
    p.add_argument("--timeout", type=float, default=2.0, help="seconds to wait for a reply")
    args = p.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(args.timeout)
        print("Type your message in the format 'capital of ...' and press Enter. 'bye' to get a goodbye. Ctrl+C to exit.")
        while True:
            try:
                line = input("> ")
            except EOFError:
                break
            msg = line.strip()
            s.sendto(msg.encode("utf-8"), (args.host, args.port))
            try:
                data, _ = s.recvfrom(2048)
                resp = data.decode("utf-8").strip()
                print(resp)
                if resp.lower().startswith("bye"):
                    # UDP has no connections; we just stop the client.
                    break
            except socket.timeout:
                print("[UDP] No reply we lost your reply. Try again.")

if __name__ == "__main__":
    main()
