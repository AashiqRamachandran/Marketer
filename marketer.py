import tweepy
import csv
import pandas as pd
import time

#tokens initialized
consumer_key = 'IUK4LzRRBjNZSPse0Yrh0ASzs'
consumer_secret = 'R7wgP61StMDNKtSN71hWTj7ROjIa15m8643bfm9Cy8XsUG6BSR'
access_token = '1226323598144458754-gAWJFxK7fzoioaPomxaUS7PemHhDIl'
access_token_secret = 'MtMZOPHtFyTmAu14zwRRrgJNUZx8gDZUuItwXIz8VFMHv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

def postt(message, idom):
    api.update_status(message, idom)
    time.sleep(2)

for tweet in tweepy.Cursor(api.search,q="#wfh",count=100,
                           lang="en").items():
    print(tweet.created_at, tweet.text)
    reply= "Looks like you have been talking about WFH. We are working on an interesting solution for WFH, check it out here ! http://www.intelitix.com/hrsolutions/RWQ/"
    message= "@%s Hey! " %(tweet.user.screen_name) + str(reply)
    postt(message,tweet.id)






    
