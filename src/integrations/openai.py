from model.timeline import Timeline
from openai import OpenAI

client = OpenAI()


def send_to_chatgpt(timeline: Timeline) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": timeline.title}]
    )

    return completion.choices[0].message
