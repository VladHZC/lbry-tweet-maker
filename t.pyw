import requests
import tweepy
import json 
import yaml
from pathlib import Path
import time


yaml_file = open("config.yaml", 'r')
yaml_content = yaml.load(yaml_file)

consumer_key = yaml_content["consumer_key"]
consumer_secret = yaml_content["consumer_secret"]
access_token = yaml_content["access_token"]
access_token_secret = yaml_content["access_token_secret"]
channelId = yaml_content["channelID"]


try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
except Exception as e: 
    exit(-1)


for number_of_tries in range(5):
    try:
        json = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"channel": channelId,
                                                                                         "stream_types": ["video",
                                                                                         "document"], 
                                                                                         "order_by": ["release_time"]}}).json()
        items = json["result"]["items"]
    except:
        time.sleep(5)
        continue

    for item in items:
        claimId = item["claim_id"]
        title = item["value"]["title"]
        url = item["permanent_url"]
        name = item['name']
     
        break

    Path("last_claim_id.txt").touch()
    lastClaimId = open("last_claim_id.txt", "r").read()

    if(claimId != lastClaimId):
        try:
            api.update_status('Check my most recent LBRY post, join us ''https://open.lbry.com/'+ name + "#" + claimId)
            f = open("last_claim_id.txt", "w")
            f.write(claimId)
            f.close()
        except: 
            exit(-1)

    exit(0)
