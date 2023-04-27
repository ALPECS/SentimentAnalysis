import openai
import os
import pandas as pd


import tweepy

consumer_key = "BkEPb0jyEMmw878gj74vOrkFY"
consumer_secret = "24dZiQhAZdTX4QFuZc9EZpfYJdnw83tzTARVq9KH0mITjQrcyE"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAL4NnAEAAAAAp%2BpBIxt%2FjZja7nn5wEZtInIgCAs%3DFzdsKA1nkcN6OrdDlCGiuKHcpRDowA8lcNAmZT0FVwl5YefguE"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
twitterAPI = tweepy.API(auth)


tweet_dataset = []
tweets = twitterAPI.search_tweets(q='RDNT -filter:retweets -filter:replies',
                                  lang = "en",
                                  result_type="recent",
                                  count = 10
                                 )

for tweet in tweets:
    tweet_content = {'id': tweet.id,
                     'date': tweet.created_at,
                     'user_name': tweet.user.screen_name,
                     'text': tweet.text,
                     }

    tweet_dataset.append(tweet_content)

tweet_dataframe = pd.DataFrame(tweet_dataset)
print(tweet_dataframe.shape)
tweet_dataframe.head()





