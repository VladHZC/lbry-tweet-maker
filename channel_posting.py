import requests
import tweepy
import json 
import yaml
from pathlib import Path
from time import sleep
import sqlite3

yaml_file = open("config.yaml", 'r')
yaml_content = yaml.load(yaml_file, Loader = yaml.FullLoader)

consumer_key = yaml_content["consumer_key"]
consumer_secret = yaml_content["consumer_secret"]
access_token = yaml_content["access_token"]
access_token_secret = yaml_content["access_token_secret"]
channelId = yaml_content["channelID"]
databaseName = 'database copy 2.sqlite'
# databaseName = 'test.db'

def get_twitter_api(tweepy, consumer_key, consumer_secret,access_token,access_token_secret):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        return api
    except Exception as e: 
        exit(-1)


def get_page(page, channelId = channelId, page_size = 50):
    json = requests.post("http://localhost:5279", json={"method": "claim_search", "params": {"channel": channelId,"page_size": page_size,"page":page,
                                                                                    "stream_types": ["video",
                                                                                    "document"], 
                                                                                    "order_by": ["^release_time"]}}).json()
    items = json["result"]["items"]
    return items

def get_all_pages(page=1):
    all_items = get_page(page)
    if len(all_items) > 0:
        new_page = page + 1
        return all_items + get_all_pages(new_page)
    else:
        return all_items
    

# Return a sqlite database
def get_db_conn(dbName,sqlite3 = sqlite3):
    conn = sqlite3.connect(dbName)
    return conn

    
def save_in_db(conn, all_items):
    cur = conn.cursor()
    for item in all_items:
        claimId = item["claim_id"]
        title = item["value"]["title"]
        url = item["permanent_url"]
        name = item['name']
        sql = f'INSERT INTO posts (claimId, title, url, name, posted) VALUES ("{claimId}","{title}","{url}","{name}", 0);'
        print('salvei')
        print(sql)
        cur.execute(sql)
    conn.commit()
    conn.close()


def check_if_database_is_empty(conn):
    cur = conn.cursor()
    query = 'SELECT * FROM posts'
    result = cur.execute(query)
    if not result.fetchall():
        return True
    return False

def call():
    conn = get_db_conn(databaseName)
    is_db_empty = check_if_database_is_empty(conn)
    if is_db_empty:
        all_items = get_all_pages()
        save_in_db(conn,all_items)
        print('All posts saved!')
    