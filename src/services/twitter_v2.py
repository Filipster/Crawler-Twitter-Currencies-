from TwitterAPI import TwitterAPI
import os
from dotenv import load_dotenv
# from src.services.model import Tweet
import datetime


def login() -> TwitterAPI:
    print('[*] Login to Twitter...')
    load_dotenv('./src/env/.env')

    consumer_key = os.getenv('CONSUMER_TOKEN')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_secret = os.getenv('ACCESS_SECRET')

    api = TwitterAPI(consumer_key, consumer_secret,
                     access_token, access_secret)

    print('[+] Logged on Twitter')
    return api


def sample_tweet(term: str, stream: int = 0, limit: int = 1) -> dict:
    print('[+] Searching a sample Tweet of: {}'.format(term))
    api = login()

    if stream == -1:
        tweets = [tw for tw in api.request(
            'search/tweets', {'q': term, "lang": "en", 'count': limit})]
    else:
        tweets = [tw for tw in api.request(
            'search/tweets', {'q': term, 'count': limit})]

    res = []
    for tw in tweets:
        text = '"' + tw['text'] + '"'
        new_datetime = datetime.datetime.strftime(
            datetime.datetime.strptime(
                tw['created_at'], '%a %b %d %H:%M:%S +0000 %Y'),
            '%Y-%m-%d %H:%M:%S')
        Tweet = {
            'id': tw['id'],
            'created_at': new_datetime,
            'text': text,
            'lang': tw['lang'],
            'retweets': tw['retweet_count'],
            'user_id': tw['user']['id'],
            'user_name': tw['user']['name'],
            'user_followers': tw['user']['followers_count'],
            'user_friends': tw['user']['friends_count'],
            'user_location': tw['user']['location']
        }
        res.append(Tweet)

    return res
