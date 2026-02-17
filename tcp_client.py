
#Oleksandra Kovalenko Homework 2 (client TCP)

"""
TCP Chat-Bot Client
Connects to server using TCP and sends a message per user input, then prints reply
"""
import argparse, socket, sys

def main():
    p = argparse.ArgumentParser(description="TCP chat-bot client")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=12000)
    args = p.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.host, args.port))
        # Print any greeting
        try:
            s.settimeout(0.2)
            try:
                print(s.recv(1024).decode("utf-8"), end="")
            except Exception:
                pass
            s.settimeout(None)
        except Exception:
            pass
        print("Type your message in the format 'capital of ...' and press Enter. 'bye' to exit.")
        for line in sys.stdin:
            msg = line.rstrip("\n")
            s.sendall((msg + "\n").encode("utf-8"))
            data = s.recv(1024)
            if not data:
                print("Server closed connection.")
                break
            resp = data.decode("utf-8").strip()
            print(resp)
            if resp.lower().startswith("bye"):
                break

if __name__ == "__main__":
    main()
