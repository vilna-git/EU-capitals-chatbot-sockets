# European Capitals TCP/UDP Chatbot

A socket programming demonstration implementing both TCP (reliable) and UDP (unreliable) client-server architectures with a conversational chatbot that answers queries about European capital cities.

## 🤖 Overview

**Synyi Voron** is a socket-based chatbot that provides information about the capital cities of 27+ European countries. This project demonstrates fundamental network programming concepts by implementing the same chatbot functionality using two different transport layer protocols.

### Key Features

- **Dual Protocol Support**
  - TCP implementation with persistent connections and multi-threading
  - UDP implementation with connectionless datagrams
  
- **Intelligent Query Processing**
  - Case-insensitive pattern matching
  - Regex-based text normalization
  - Whitespace and punctuation handling
  
- **27+ European Countries**
  - Comprehensive coverage of EU capitals
  - Rich contextual information about each city
  - Fallback responses for unrecognized queries

## 🏗️ Architecture

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

## 📊 Technical Comparison

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Persistent | Connectionless |
| Reliability | Guaranteed delivery | Best-effort |
| Ordering | In-order delivery | No ordering guarantee |
| Overhead | Higher (handshake, ACKs) | Lower (no connection setup) |
| Use Case | Reliable communication | Speed over reliability |
| Multi-client | Threading required | Naturally stateless |

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- No external dependencies (uses only standard library modules)

### Installation

```bash
git clone https://github.com/vilna-git/european-capitals-chatbot.git
cd european-capitals-chatbot
```

## 💻 Usage

### TCP Version

**Start the TCP server:**
```bash
python3 tcp_server.py --host 127.0.0.1 --port 12000
```

**Connect with TCP client:**
```bash
python3 tcp_client.py --host 127.0.0.1 --port 12000
```

**Example session:**
```
Welcome to Synyi Voron, your European capitals TCP based chat bot.
Type your message in the format 'capital of ...' and press Enter. 'bye' to exit.

> capital of France
The capital of France is Paris – the City of Light, known for art, fashion, and the Eiffel Tower.

> capital of Germany
The capital of Germany is Berlin – a creative, modern city that's been rebuilt into a hub of culture and tech.

> bye
Bye!
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

**Example session:**
```
Type your message in the format 'capital of ...' and press Enter. 'bye' to get a goodbye. Ctrl+C to exit.

> capital of Poland
The capital of Poland is Warsaw – a resilient city rebuilt after WWII with a charming old town.

> capital of Spain
The capital of Spain is Madrid – famous for its royal palace, tapas, and vibrant nightlife.

> bye
Bye!
```

## 🔍 Implementation Details

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

**Key features:**
- Thread per client for concurrent handling
- Message buffering for stream protocol
- Graceful disconnection handling

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

**Key features:**
- No connection state
- Each message independent
- Client address extracted per datagram

## 📁 Project Structure

```
european-capitals-chatbot/
├── common.py          # Shared query processing logic
├── tcp_server.py      # TCP reliable server
├── tcp_client.py      # TCP reliable client
├── udp_server.py      # UDP unreliable server
├── udp_client.py      # UDP unreliable client
├── README.md          # This file
├── LICENSE            # MIT License
└── .gitignore         # Git ignore rules
```

## 🌍 Supported Countries

The chatbot knows capitals of 27+ European countries including:

**Western Europe:** France, Germany, Netherlands, Belgium, Luxembourg, Austria  
**Southern Europe:** Italy, Spain, Portugal, Greece, Malta, Cyprus  
**Northern Europe:** Sweden, Denmark, Finland, Norway, Ireland  
**Central Europe:** Poland, Czech Republic, Hungary, Slovakia, Slovenia  
**Eastern Europe:** Romania, Bulgaria, Estonia, Latvia, Lithuania, Croatia

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Socket programming in Python
- ✅ TCP vs UDP protocol differences
- ✅ Multi-threaded server architecture
- ✅ Client-server communication patterns
- ✅ Error handling and timeout management
- ✅ Message buffering and parsing
- ✅ Text processing with regex

## 🧪 Testing & Validation

### TCP Testing
- Multi-client concurrent connections
- Message ordering verification
- Connection persistence validation
- Graceful shutdown testing

### UDP Testing
- Packet loss simulation (timeout scenarios)
- Independent message processing
- Stateless operation verification

## 📚 Academic Context

**Course:** NYU CS-UY 4793G Computer Networks (Fall 2024)  
**Assignment:** Homework 2 - Socket Programming  
**Student:** Oleksandra Kovalenko

### Exercise Requirements
- Implement both TCP and UDP versions
- Demonstrate understanding of transport layer protocols
- Handle multiple clients (TCP) and stateless operation (UDP)
- Proper error handling and resource management

## 🔧 Command Line Options

### TCP Server
```bash
python3 tcp_server.py [--host HOST] [--port PORT]
# Defaults: host=127.0.0.1, port=12000
```

### TCP Client
```bash
python3 tcp_client.py [--host HOST] [--port PORT]
# Defaults: host=127.0.0.1, port=12000
```

### UDP Server
```bash
python3 udp_server.py [--host HOST] [--port PORT]
# Defaults: host=127.0.0.1, port=12000
```

### UDP Client
```bash
python3 udp_client.py [--host HOST] [--port PORT] [--timeout SECONDS]
# Defaults: host=127.0.0.1, port=12000, timeout=2.0
```

## 🐛 Common Issues

**TCP: "Address already in use"**
- Wait 30-60 seconds after stopping server
- Or use different port number
- Server uses `SO_REUSEADDR` to minimize this

**UDP: "No reply we lost your reply"**
- Normal behavior demonstrating packet loss
- Press Enter to resend message
- Adjust timeout with `--timeout` flag

## 📄 License

MIT License - Free to use for educational purposes.

## 📧 Contact

Questions? Open an issue on GitHub.

---

**Note:** This is an educational project demonstrating network programming concepts. Production chatbots require natural language processing, databases, and robust error handling.
