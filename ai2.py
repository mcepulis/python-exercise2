import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

response = client.beta.chat.completions.parse(
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ],
    response_format=CalendarEvent,
    model="gpt-4o",
)

event = response.choices[0].message.content

print(event)

