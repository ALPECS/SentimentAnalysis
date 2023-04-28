# Documentation for Code

The provided code is a Python script that uses the Twitter API and OpenAI to get tweets related to a specific keyword and classify their sentiment as positive, negative, or neutral. Check out the ipynb for neat charts as well.

## Function `getData(ticker, data)`

This function takes two parameters, `ticker` and `data`. `ticker` is a string that represents the keyword for which the tweets are to be fetched. `data` is an integer that represents the number of tweets to be fetched. The function uses the `search_tweets()` method of the `tweepy` library to fetch tweets related to the `ticker` keyword. It then extracts the tweet's ID, creation date, user name, and text and stores them in a list of dictionaries. Finally, the function returns a pandas dataframe containing the extracted information.

## Function `get_sentiment(text, ticker)`

This function takes two parameters, `text` and `ticker`. `text` is a string that represents the tweet's text for which the sentiment is to be classified. `ticker` is a string that represents the keyword for which the tweets are fetched. The function uses OpenAI's GPT-3 API to classify the sentiment of the tweet as positive, negative, or neutral. It creates a prompt using the tweet's text and the `ticker` keyword and sends it to the API for classification. The function then extracts the sentiment from the API's response and returns it as a string.

## Twitter API Authentication

The script uses the Twitter API to fetch tweets. To use the API, you need to authenticate yourself by providing your consumer key, consumer secret, and bearer token. You can obtain these credentials by creating a developer account on the Twitter Developer Portal and creating a new app. Once you have the credentials, replace `<Your Key>`, `<Your Secret>`, and `<Your Bearer Token>` with your credentials.

## OpenAI API Authentication

The script uses the OpenAI API to classify the sentiment of the tweet. To use the API, you need to authenticate yourself by providing your API key and base URL. You can obtain these credentials by creating an account on the OpenAI website and creating a new API key. Once you have the credentials, replace `<Your API Key>` and `<Your API Base>` with your credentials.

## Charts made by this code
![image](https://user-images.githubusercontent.com/99166566/235082836-5b6fb607-b50a-4d50-84c2-2e9b12c4756b.png)
![image](https://user-images.githubusercontent.com/99166566/235082853-35d4738a-e0c0-4a83-b480-4c6be709192a.png)
![image](https://user-images.githubusercontent.com/99166566/235082864-19285a17-3208-4886-8bf1-1661eb8f33dc.png)



