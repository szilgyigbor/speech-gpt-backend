import openai
from api_keys import API_KEY

openai.api_key = API_KEY


def get_answer(message_history):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=message_history
    )
    message_history.append(completion.choices[0].message)

    return message_history
