import requests
import tweepy
import json 
from pathlib import Path

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth
    except Exception as e: 
        return None

oauth = OAuth()
api = tweepy.API(oauth)   
channelId = "@vlad#e"

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
    #tweet = item["value"]["description"]
    print(url + " / " + title + " / " + claimId)
    break

if(claimId != lastClaimId):
    api.update_status('https://open.lbry.com/'+ name + "#" + claimId)
    f = open("last_claim_id.txt", "w")
    f.write(claimId)
    f.close()

    # 1) Make it in a way that you just need to click so it can update the twitter
    # 2) Make script monitor lbry channel to post update twitter 
    # 3) ADD description tweet before URL 
    # 4) Make a version that allows you to post your entire channel with a daily post option tool 
