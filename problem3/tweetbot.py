import tweepy

consumer_key='zTUSwg4iz6CyHoxj7BeO7ikS3'
consumer_secret='kcAXNwoeJpZbP3881f0C1KGj8mizXP9fcNMLa1u88GrmPSuUQp'
access_token='895530546368880640-xkIOYGwkmJDaSLp6RsdDMmFB3E3Uqtx'
access_token_secret='DpWt7PIIuIvXTYdvLHQJlyyIN12VlnCxW6fpcWa7oRvpY'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
foll=open("followers.txt","w+")
fr=open("following.txt","w+")
user = api.get_user('roshan_61')
print (user.screen_name)
print ('follower cout')
print (user.followers_count)
print ('following cout')
print (user.friends_count)
print ('following ------------------------------------------')
for status in tweepy.Cursor(api.friends).items():
    print (status.screen_name)
    fr.write(status.screen_name + "\n")
print ('follower------------------------------------')
for follower in tweepy.Cursor(api.followers).items():
   print (follower.screen_name)
   foll.write(follower.screen_name + "\n")
foll.close()
fr.close()
while True:
    try:
            tweets = api.user_timeline(screen_name = 'boltiot',count='1000')
            for tweet in tweets:
                if not tweet.favorited:
                    api.create_favorite(tweet.id)
                    print('Liked @boltiot tweet')
                if not tweet.retweeted:
                    api.retweet(tweet.id)
                    print ('retweet @botiot tweet')
    except Exception as e:
            print ('Already liked @botiot tweet')
    try:
             cricTweet = tweepy.Cursor(api.search, q='IOT').items()
             for tweet in cricTweet:
                if not tweet.favorited:
                   api.create_favorite(tweet.id)
                   print('Liked #IOT tweet')
                if not tweet.retweeted:
                   api.retweet(tweet.id)
                   print('Retweet #IOT tweet')
    except Exception as e:
            print ('Already tweeted')
    



