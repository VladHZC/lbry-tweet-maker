import requests
import tweepy
import json 
import yaml
from pathlib import Path
import time

for x in range(1,20):
    time.sleep(1)
    print(x)


yaml_file = open("config.yaml", 'r')
yaml_content = yaml.load(yaml_file)

consumer_key = yaml_content["consumer_key"]
consumer_secret = yaml_content["consumer_secret"]
access_token = yaml_content["access_token"]
access_token_secret = yaml_content["access_token_secret"]
channelId = yaml_content["channelID"]

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth
    except Exception as e: 
        return None

oauth = OAuth()
api = tweepy.API(oauth)   

json = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"channel": channelId,
                                                                                         "stream_types": ["video",
                                                                                         "document"], 
                                                                                         "order_by": ["release_time"]}}).json()


Path("last_claim_id.txt").touch()
lastClaimId = open("last_claim_id.txt", "r").read()

for item in json["result"]["items"]:
    claimId = item["claim_id"]
    title = item["value"]["title"]
    url = item["permanent_url"]
    name = item['name']
    tweet = item["value"]["description"]
    print(url + " / " + title + " / " + claimId)
    break

if(claimId != lastClaimId):
    api.update_status('Check my most recent LBRY post, escape big tech, join us ''https://open.lbry.com/'+ name + "#" + claimId)
    f = open("last_claim_id.txt", "w")
    f.write(claimId)
    f.close()
