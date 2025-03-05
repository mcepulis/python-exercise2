import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()

class CalendarEvent(BaseModel):
    answer: str
    

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

user_question = input('Enter your question:')

response = client.beta.chat.completions.parse(
    messages=[
        {"role": "system", "content": "answer in one word"},
        {"role": "user", "content": user_question},
    ],
    response_format=CalendarEvent,
    model="gpt-4o",
)

event = response.choices[0].message.content

print(event)

