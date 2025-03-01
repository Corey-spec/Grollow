import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
    {"role": "user", "content": "Hi ChatGPT. Say hi Back!"}
])      
answer = response.choices[0].message.content
print(answer)