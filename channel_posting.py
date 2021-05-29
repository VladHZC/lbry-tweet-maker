import requests
import tweepy
import json 
import yaml
import sqlite3

yaml_file = open("config.yaml", 'r')
yaml_content = yaml.load(yaml_file, Loader = yaml.FullLoader)

consumer_key = yaml_content["consumer_key"]
consumer_secret = yaml_content["consumer_secret"]
access_token = yaml_content["access_token"]
access_token_secret = yaml_content["access_token_secret"]
channelId = yaml_content["channelID"]
databaseName = 'database.sqlite'

def get_twitter_api(tweepy=tweepy, consumer_key=consumer_key, consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret):
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


def check_if_database_is_empty(conn):
    cur = conn.cursor()
    query = 'SELECT * FROM posts'
    result = cur.execute(query)
    if not result.fetchall():
        return True
    return False


def get_post_from_db(cursor):
    query = 'SELECT * FROM posts WHERE posted = 0 limit 1;'
    response = cursor.execute(query)
    result = response.fetchone()
    return result


def post_tweet(data, api):
    post_id = data[0]
    claimId = data[1]
    title = data[2]
    url = data[3]
    name = data[4]
    isPosted = data[5]
    api.update_status(f'I am free at LBRY, check my last content and join us https://lbry.tv/{channelId}/{name}:{claimId}')
    print('Posted sucessfully')

def update_db(conn, post_id):
    try:
        query = f'UPDATE posts SET posted = 1 WHERE id = {post_id};'
        conn.cursor().execute(query)
        conn.commit()
    except Exception as e:
        print(e)
        raise e

    
def call():
    conn = get_db_conn(databaseName)
    is_db_empty = check_if_database_is_empty(conn)
    if is_db_empty:
        all_items = get_all_pages()
        save_in_db(conn,all_items)
        print('All posts saved!')
    cur = conn.cursor()
    data = get_post_from_db(cur)
    api = get_twitter_api()
    post_tweet(data,api)
    update_db(conn, data[0])


call()