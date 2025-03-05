import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()

class CalendarEvent(BaseModel):
    color: list[str]
    action: str

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

response = client.beta.chat.completions.parse(
    messages=[
        # {"role": "system", "content": "provide color and action from content"},
        {"role": "user", "content": "We are moving from black bridge to white"},
    ],
    response_format=CalendarEvent,
    model="gpt-4o",
)

event = response.choices[0].message.content

print(event)

