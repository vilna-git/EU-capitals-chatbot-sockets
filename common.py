
#Oleksandra Kovalenko common.py
# Shared helpers for the chat-bot
import re

QA_MAP = {
  "hello": "Hi! I'm Synyi Voron — your European capitals chat-bot.",
  "hi": "Hi! I'm Synyi Voron — your European capitals chat-bot.",
  "what is your name": "I'm Synyi Voron, a socket-based bot who knows EU capitals.",
  "capital of france": "The capital of France is Paris — the City of Light, known for art, fashion, and the Eiffel Tower.",
  "capital of germany": "The capital of Germany is Berlin — a creative, modern city that’s been rebuilt into a hub of culture and tech.",
  "capital of italy": "The capital of Italy is Rome — once the heart of the Roman Empire and home to the Colosseum and Vatican City.",
  "capital of spain": "The capital of Spain is Madrid — famous for its royal palace, tapas, and vibrant nightlife.",
  "capital of poland": "The capital of Poland is Warsaw — a resilient city rebuilt after WWII with a charming old town.",
  "capital of sweden": "The capital of Sweden is Stockholm — spread across 14 islands, known for design and innovation.",
  "capital of netherlands": "The capital of the Netherlands is Amsterdam — full of canals, bikes, and cozy cafes.",
  "capital of belgium": "The capital of Belgium is Brussels — home to the EU headquarters and famous for waffles and chocolate.",
  "capital of austria": "The capital of Austria is Vienna — Mozart’s city, known for classical music and elegant coffee houses.",
  "capital of greece": "The capital of Greece is Athens — the cradle of democracy with iconic ancient ruins like the Parthenon.",
  "capital of portugal": "The capital of Portugal is Lisbon — a sunny, hilly city known for pastel buildings and tram rides.",
  "capital of czech republic": "The capital of the Czech Republic is Prague — full of gothic architecture and the famous Charles Bridge.",
  "capital of hungary": "The capital of Hungary is Budapest — split by the Danube and known for its thermal baths.",
  "capital of denmark": "The capital of Denmark is Copenhagen — stylish, sustainable, and home to the Little Mermaid statue.",
  "capital of finland": "The capital of Finland is Helsinki — a seaside city with Nordic design and cozy saunas.",
  "capital of ireland": "The capital of Ireland is Dublin — famous for its literary history and lively pub culture.",
  "capital of croatia": "The capital of Croatia is Zagreb — a mix of Austro-Hungarian architecture and Mediterranean charm.",
  "capital of romania": "The capital of Romania is Bucharest — known as 'Little Paris' for its wide boulevards and Belle Époque buildings.",
  "capital of bulgaria": "The capital of Bulgaria is Sofia — one of Europe’s oldest cities, surrounded by mountains.",
  "capital of estonia": "The capital of Estonia is Tallinn — a digital-first city with a beautifully preserved medieval old town.",
  "capital of latvia": "The capital of Latvia is Riga — an Art Nouveau gem on the Baltic Sea with a lively old town.",
  "capital of lithuania": "The capital of Lithuania is Vilnius — known for its baroque architecture and diverse cultural heritage.",
  "capital of slovakia": "The capital of Slovakia is Bratislava — sitting on the Danube with views of nearby Austria and Hungary.",
  "capital of slovenia": "The capital of Slovenia is Ljubljana — a green, charming city with riverside cafes and bridges.",
  "capital of luxembourg": "The capital of Luxembourg is Luxembourg City — one of Europe’s wealthiest capitals, built on dramatic cliffs.",
  "capital of cyprus": "The capital of Cyprus is Nicosia — the world’s last divided capital, with Greek and Turkish sectors.",
  "capital of malta": "The capital of Malta is Valletta — a tiny fortified city filled with golden stone buildings and sea views.",
  "bye": "Bye!"
}

def normalize(text: str) -> str:
    # Lowercase, collapse spaces, strip punctuation around words
    text = text.lower()
    text = re.sub(r"[\s]+", " ", text)
    text = re.sub(r"(^\W+|\W+$)", "", text.strip())
    return text

def answer(msg: str) -> str:
    key = normalize(msg)
    # Exact match first
    if key in QA_MAP:
        return QA_MAP[key]
    # Simple contains-based fallbacks
    for country in ["france","germany","italy","spain","poland","sweden","netherlands",
                    "belgium","austria","greece","portugal","czech republic","hungary",
                    "denmark","finland","ireland","croatia","romania","bulgaria","estonia"]:
        if country in key and "capital" in key:
            return QA_MAP.get(f"capital of {country}")

    if key in ("bye", "goodbye", "quit", "exit"):
        return QA_MAP["bye"]

    return "I only know the capitals of EU countries! Try asking 'capital of France' or 'capital of Poland'."
