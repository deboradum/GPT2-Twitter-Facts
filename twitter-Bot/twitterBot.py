import requests
from requests_oauthlib import OAuth1
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("APIKEY")
api_key_secret = os.environ.get("APIKEYSECRET")
access_token = os.environ.get("ACCESSTOKEN")
access_token_secret = os.environ.get("ACCESSTOKENSECRET")


API_URL = "https://api.twitter.com/2/tweets"

def get_fact():
    fact = "test"

    return fact


def format_tweet(text):
    return {"text": "{}".format(text)}


def main():
    fact = get_fact()
    payload = format_tweet(fact)
    auth = OAuth1(api_key, api_key_secret, access_token, access_token_secret)

    response = requests.post(auth=auth,
                             url=API_URL,
                             json=payload,
                             headers={"Content-Type": "application/json"})


if __name__ == "__main__":
    main()
