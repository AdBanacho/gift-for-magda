def generate_prompt_gpt(message):
    return """introduce your self GPT-3."""


def generate_prompt_song(message):
    return """Write a song about sweet Magda."""


def generate_prompt_translate(message):
    return f'''Translate text to Polish.
    "{message}"'''


def generate_prompt_story(message):
    return f'''Topic: {message[0]}
    Three-Sentence {message[0]} Story about {message[0]}: "'''


def generate_prompt_magda(message):
    return f'''Why auntie Magda is a greatest auntie on the world?"'''


def generate_prompt_wish(message):
    return f'''Write sweet and crazy wishes for Magda."'''


def generate_prompt_emoji(message):
    return f'''translate text to emojis.
    text: M{message}
    emoji: "'''
