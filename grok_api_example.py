from openai import OpenAI

# Ersetze 'dein_api_key_hier' mit deinem echten API-Schlüssel aus console.x.ai
client = OpenAI(
    api_key="dein_api_key_hier",
    base_url="https://api.x.ai/v1"
)

# Beispiel-Anfrage an Grok 4
response = client.chat.completions.create(
    model="grok-4",  # Verwende 'grok-4' für Grok 4
    messages=[{"role": "user", "content": "Hallo, was ist die Bedeutung des Lebens?"}]
)
print(response.choices[0].message.content)
