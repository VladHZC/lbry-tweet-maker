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


def get_page(page, channelId = channelId, page_size = 50):
    json = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"channel": channelId,"page_size": page_size,"page":page,
                                                                                    "stream_types": ["video",
                                                                                    "document"], 
                                                                                    "order_by": ["^release_time"]}}).json()
    items = json["result"]["items"]
    return items

def get_all(page=1):
    all_items = get_page(page)
    if len(all_items) > 0:
        new_page = page + 1
        return all_items + get_all(new_page)
    else:
        return all_items
    



