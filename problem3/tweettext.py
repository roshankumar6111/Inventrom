import tweepy

consumer_key='zTUSwg4iz6CyHoxj7BeO7ikS3'
consumer_secret='kcAXNwoeJpZbP3881f0C1KGj8mizXP9fcNMLa1u88GrmPSuUQp'
access_token='895530546368880640-xkIOYGwkmJDaSLp6RsdDMmFB3E3Uqtx'
access_token_secret='DpWt7PIIuIvXTYdvLHQJlyyIN12VlnCxW6fpcWa7oRvpY'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.get_user('boltiot')
print (user.screen_name)
print ('follower cout')
print (user.followers_count)
print ('friends name------------------------------------------')
for status in tweepy.Cursor(api.friends).items(200):
    print(status.screen_name)
print ('follower name------------------------------------')
for follower in tweepy.Cursor(api.followers).items(200):
   print (follower.screen_name)
while True:
    try:
            tweets = api.user_timeline(screen_name = 'boltiot',count='10')
            for tweet in tweets:
                if not tweet.favorited:
                    #print (tweet)
                    api.create_favorite(tweet.id)
                if not tweet.retweeted:
                    api.retweet(tweet.id)
    except Exception as e:
            print ('already liked')
    try:
             cricTweet = tweepy.Cursor(api.search, q='IOT').items()
             for tweet in cricTweet:
                if not tweet.favorited:
                   api.create_favorite(tweet.id)
                   # print (tweet.created_at, tweet.text, tweet.lang)
                if not tweet.retweeted:
                   api.retweet(tweet.id)
    except Exception as e:
            print ('TWEETED')
    



