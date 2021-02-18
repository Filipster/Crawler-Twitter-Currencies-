import tweepy
import os
from dotenv import load_dotenv


def login() -> tweepy.API():
    print('[*] Login to Twitter...')
    load_dotenv('./src/env/.env')

    consumer_key = os.getenv('CONSUMER_TOKEN')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_secret = os.getenv('ACCESS_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    try:
        api.me()
    except tweepy.TweepError as err:
        print('[!] Error on login..')
        print(err)
        raise tweepy.TweepError

    print('[+] Logged on Twitter')
    return api
