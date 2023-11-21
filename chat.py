from openai import OpenAI
from conf import APIKEY

client = OpenAI(
  api_key = APIKEY,  # this is also the default, it can be omitted
)

def chat(messages: list) -> str:
    print("Before chat.completions")
    result = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)
    response_text = result.choices[0].message.content
    print("After chat.completions" + response_text)
    return response_text
