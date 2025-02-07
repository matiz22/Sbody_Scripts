from ollama import Client


class OllamaClient:
    def __init__(self, host="http://localhost:11434/"):
        self.client = Client(host=host)

    def ask(self, model, system_prompt, user_messages, formatoutput=None):
        system_message = {
            "role": "system",
            "content": system_prompt,
        }
        return self.client.chat(
            model=model, messages=[system_message] + user_messages, format=formatoutput
        ).message.content
