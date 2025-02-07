from openai import OpenAI


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI()

    def ask(self, model, system_prompt, user_messages, formatoutput=None):
        system_message = {
            "role": "system",
            "content": system_prompt,
        }

        return (
            self.client.chat.completions.create(
                model=model,
                messages=[system_message] + user_messages,
                response_format={"type": "json_object"},
            )
            .choices[0]
            .message.content
        )
