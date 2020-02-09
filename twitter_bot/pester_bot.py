import tweepy, os, requests
from datetime import datetime, timedelta
from time import sleep

min_t = timedelta(minutes = 15)
bill = 'https://images.sftcdn.net/images/t_app-cover-l,f_auto/p/ce2ece60-9b32-11e6-95ab-00163ed833e7/260663710/the-test-fun-for-friends-screenshot.jpg'
target = "@DisImma"


CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)      #1


def tweet_image(url, user, tweet_id):
    filename = 'brl-20-brazilian-reals-2.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename,status=user, in_reply_to_status_id=tweet_id)
        os.remove(filename)
    else:
        print("Unable to download image")

while True:
    seen_tweets = api.user_timeline(screen_name = target,count = 10)  #2
    for tweet in seen_tweets:
        tweet_posted = tweet.created_at
        time_check = datetime.utcnow()
        try:
            failsafe = tweet.retweeted_status #3
        except:
            if tweet.in_reply_to_status_id == None: #4
                tweet_delta = time_check - tweet_posted
                if tweet_delta < min_t: #5
                    tweet_image(bill, target, tweet.id) #6
    sleep(900)  #7
                













'''for tweet in seen_tweets:
    tweet_id = tweet.id
    now = datetime.now()
    time = tweet.created_at
    if tweet.in_reply_to_status_id == None:
        print(time-now)
        print("")
        print(time)
        if abs(time-now) < min_t:
            print(tweet_id)'''
        
#    try:
#        print(tweet.retweeted_status)
#    except:
#        print(tweet.created_at)