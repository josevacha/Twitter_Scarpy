import tweepy
import authenticate as oauth
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


 
def authenticate(): 
	auth = OAuthHandler(oauth.consumer_key, oauth.consumer_secret)
	auth.set_access_token(oauth.access_token, oauth.access_secret)
	api = tweepy.API(auth)
	return api

def get_statuses():
	# for status in tweepy.Cursor(api.home_timeline).items(10):
	#     # Process a single status
	#    return status 

	statuses = tweepy.Cursor(api.home_timeline).items(10)
	return statuses

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('thanksgiving2.txt', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
 
api = authenticate()

# twitter_stream = Stream(api.auth, MyListener())
# twitter_stream.filter(track=['#food' '#thanksgiving'])