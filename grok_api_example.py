import os
from openai import OpenAI

# Lade den API-Key aus der Environment Variable (aus GitHub Secret)
api_key = os.environ.get('XAI_API_KEY')

if not api_key:
    raise ValueError("API-Key nicht gefunden! Stelle sicher, dass 'XAI_API_KEY' als Secret gesetzt ist.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1"
)

# Beispiel-Anfrage an Grok 4
response = client.chat.completions.create(
    model="grok-4",  # Verwende 'grok-4' für Grok 4
    messages=[{"role": "user", "content": "Hallo, was ist die Bedeutung des Lebens?"}]
)
print(response.choices[0].message.content)
