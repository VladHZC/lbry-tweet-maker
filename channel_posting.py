import requests
import tweepy
import json 
import yaml
from pathlib import Path
from time import sleep

yaml_file = open("config.yaml", 'r')
yaml_content = yaml.load(yaml_file, Loader = yaml.FullLoader)

consumer_key = yaml_content["consumer_key"]
consumer_secret = yaml_content["consumer_secret"]
access_token = yaml_content["access_token"]
access_token_secret = yaml_content["access_token_secret"]
channelId = yaml_content["channelID"]

def get_twitter_api(tweepy, consumer_key, consumer_secret,access_token,access_token_secret):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        return api
    except Exception as e: 
        print('entrei')
        print(e)
        exit(-1)

    



