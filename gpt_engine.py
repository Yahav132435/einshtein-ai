import openai
import os
from persona import SYSTEM_PROMPT

openai.api_key = os.getenv("OPENAI_API_KEY")

class GPTClient:
    def __init__(self, model="gpt-4"):
        self.model = model

    def ask(self, question):
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=0.8,
            max_tokens=500
        )
        return response['choices'][0]['message']['content']