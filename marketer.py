import tweepy
import csv
import pandas as pd
csvWriter = csv.writer(csvFile)

#tokens initialized
consumer_key = 'IUK4LzRRBjNZSPse0Yrh0ASzs'
consumer_secret = 'R7wgP61StMDNKtSN71hWTj7ROjIa15m8643bfm9Cy8XsUG6BSR'
access_token = '1226323598144458754-gAWJFxK7fzoioaPomxaUS7PemHhDIl'
access_token_secret = 'MtMZOPHtFyTmAu14zwRRrgJNUZx8gDZUuItwXIz8VFMHv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

for tweet in tweepy.Cursor(api.search,q="#wfh",count=100,
                           lang="en").items():
    csvWriter.writerow([tweet.user.screen_name, tweet.text.encode('utf-8')])
    print(tweet.created_at, tweet.text)
    reply= "our landing page text goes here"
    message= "@%s" %(tweet.user.screen_name) + str(reply)
    api.update_status(message, tweet.id)






    
