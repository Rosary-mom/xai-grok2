import os
from openai import OpenAI
from dotenv import load_dotenv
import markdown

load_dotenv() 

XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "system", "content": "You are Grok, a chatbot designed to inspire positivity in human life"},
        {"role": "user", "content": "What to do when faced with life challenges?"},
    ],
)

response = completion.choices[0].message

md = markdown.Markdown(extensions=["fenced_code"])
converted = md.convert(response.content)

print(converted)
