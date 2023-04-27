openai.api_key = 'pk-JsMTVtPJVasDqBDFMosXZqmbfTRPYxhWbvCWRqzhkTDGGpUe'
openai.api_base = 'https://api.pawan.krd/v1'

response = openai.Completion.create(
    model="gpt-3.5-turbo",
    temperature= "0",
    prompt = "Rate this from a scale of 0 to 10, 0 being negative, 5 being nuteral 10 being positive: ' this product is okay '"
)

print(response.choices[0].text)