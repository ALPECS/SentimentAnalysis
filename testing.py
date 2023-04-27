import openai
import os
import pandas as pd
import tweepy
import openai
import re


# Method for getting data given a ticker
def getData(ticker):
    tweet_dataset = []
    tweets = twitterAPI.search_tweets(q=ticker + ' -filter:retweets -filter:replies',
                                      lang="en",
                                      result_type="recent",
                                      count=10
                                      )
    for tweet in tweets:
        tweet_content = {'id': tweet.id,
                         'date': tweet.created_at,
                         'user_name': tweet.user.screen_name,
                         'text': tweet.text,
                         }

        tweet_dataset.append(tweet_content)

    tweet_dataframe = pd.DataFrame(tweet_dataset)
    return tweet_dataframe


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


# Put in your tokens
consumer_key = "BkEPb0jyEMmw878gj74vOrkFY"
consumer_secret = "24dZiQhAZdTX4QFuZc9EZpfYJdnw83tzTARVq9KH0mITjQrcyE"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAL4NnAEAAAAAp%2BpBIxt%2FjZja7nn5wEZtInIgCAs%3DFzdsKA1nkcN6OrdDlCGiuKHcpRDowA8lcNAmZT0FVwl5YefguE"

# Connect to the Twitter API
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
twitterAPI = tweepy.API(auth)

# Get your pandas dataframe
tweet_df = getData("RDNT")
