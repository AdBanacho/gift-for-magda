import openai


class Gpt:
    def __init__(self, api_key):
        openai.api_key = api_key

    def gpt_3(self, message, temp, prompt, tokens):
        return openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt(message),
            temperature=temp,
            max_tokens=tokens

        ).choices[0].text
