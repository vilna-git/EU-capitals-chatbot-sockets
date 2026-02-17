# EU countries' capitals TCP/UDP Chatbot

A socket programming demonstration implementing both TCP and UDP client-server architectures with a conversational chatbot that answers queries about EU capital cities.

##Overview

**Synyi Voron** is a socket-based chatbot that provides short information about the capital cities of 27 European countries in the EU. This project was made to understand the behind-the-scenes of the fundamental network programming concepts by implementing the same chatbot functionality using two different transport layer protocols.

### Key Features

- **Dual Protocol Support**
  - TCP implementation with persistent connections and multi-threading
  - UDP implementation with connectionless datagrams
  
- **Query Processing**
  - Case-insensitive pattern matching
  - Regex-based text normalization
  - Whitespace and punctuation handling
  
- **27 European Countries**
  - Comprehensive coverage of EU capitals
  - Additional contextual information about each city
  - Fallback responses for unrecognized questions

## Architecture

### TCP Implementation (Reliable)
- **Connection-oriented**: Persistent connection between client and server
- **Multi-threaded server**: Handles multiple concurrent clients using `threading`
- **Message buffering**: Line-delimited message parsing for stream-based protocol
- **Graceful shutdown**: Proper connection termination with "bye" command
- **Socket options**: `SO_REUSEADDR` for rapid testing cycles

### UDP Implementation (Unreliable)
- **Connectionless**: Each message is independent
- **Stateless server**: No connection state maintained
- **Timeout handling**: Client-side timeout recovery for packet loss
- **No delivery guarantee**: Demonstrates unreliable transport characteristics
- **Simple architecture**: Single-threaded, event-driven design

## Technical Comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Persistent | Connectionless |
| Reliability | Guaranteed delivery | Best-effort |
| Ordering | In-order delivery | No ordering guarantee |
| Overhead | Higher (handshake, ACKs) | Lower (no connection setup) |
| Use Case | Reliable communication | Speed over reliability |
| Multi-client | Threading required | Naturally stateless |

## Getting Started

### Prerequisites
- Python 3.8 or higher
- No external dependencies (uses only standard library modules)

### Installation

```bash
git clone https://github.com/vilna-git/EU-capitals-chatbot-sockets.git
cd EU-capitals-chatbot-sockets
```

## Usage

### TCP Version

**Start the TCP server:**
```bash
python3 tcp_server.py --host 127.0.0.1 --port 12000
```

**Connect with TCP client:**
```bash
python3 tcp_client.py --host 127.0.0.1 --port 12000
```

### UDP Version

**Start the UDP server:**
```bash
python3 udp_server.py --host 127.0.0.1 --port 12000
```

**Connect with UDP client:**
```bash
python3 udp_client.py --host 127.0.0.1 --port 12000 --timeout 2.0
```


## Implementation Details

### Query Processing (`common.py`)

**Normalization Pipeline:**
1. Convert to lowercase
2. Collapse multiple spaces
3. Strip surrounding punctuation
4. Exact match lookup
5. Fallback to substring matching

```python
def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[\s]+", " ", text)
    text = re.sub(r"(^\W+|\W+$)", "", text.strip())
    return text
```

### TCP Server Architecture

```python
# Multi-threaded server handles concurrent clients
def handle_client(conn, addr):
    with conn:
        conn.sendall(b"Welcome message\n")
        buffer = b""
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # Parse line-delimited messages
            buffer += data
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                # Process message and respond
```

### UDP Server Architecture

```python
# Stateless server processes independent datagrams
def serve(host: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        while True:
            data, client_addr = s.recvfrom(2048)
            msg = data.decode("utf-8").strip()
            resp = answer(msg)
            s.sendto(resp.encode("utf-8"), client_addr)
```

## Supported Countries

The chatbot knows capitals of 27 EU countries:

**Western Europe:** France, Germany, Netherlands, Belgium, Luxembourg, Austria  
**Southern Europe:** Italy, Spain, Portugal, Greece, Malta, Cyprus  
**Northern Europe:** Sweden, Denmark, Finland, Norway, Ireland  
**Central Europe:** Poland, Czech Republic, Hungary, Slovakia, Slovenia  
**Eastern Europe:** Romania, Bulgaria, Estonia, Latvia, Lithuania, Croatia


## Possible Issues

**TCP: "Address already in use"**
- Wait 30-60 seconds after stopping server
- Or use different port number
- Server uses `SO_REUSEADDR` to minimize this

**UDP: "No reply we lost your reply"**
- Normal behavior demonstrating packet loss
- Press Enter to resend message
- Adjust timeout with `--timeout` flag

---

**Note:** This is an educational project only. Production chatbots require natural language processing, databases, and large error handling.
