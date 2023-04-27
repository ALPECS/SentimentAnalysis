import openai
import re

openai.api_key = 'pk-JsMTVtPJVasDqBDFMosXZqmbfTRPYxhWbvCWRqzhkTDGGpUe'
openai.api_base = 'https://api.pawan.krd/v1'


def get_sentiment(text):
    prompt_text = """Classify the sentiment of the following tweet as positive, negative, or neutral towards Microsoft. 
    text: {}
    sentiment: """.format(text)

    sentiment = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt_text,
        max_tokens=15,
        temperature=0,
    )

    # remove special characters e.g n etc, from response
    sentiment = re.sub('W+', '', sentiment['choices'][0]['text'])

    return sentiment