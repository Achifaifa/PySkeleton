#! /usr/bin/env python

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import apikeys

auth = OAuthHandler(apikeys.apikey, apikeys.apisecret)
auth.set_access_token(apikeys.consumerkey, apikeys.consumersecret)

api = tweepy.API(auth)
class listener(StreamListener):

  def on_data(self, data):
    try:
      with open('python.json', 'a') as f:
        f.write(data)
        return True
    except BaseException as e:
      print("Error on_data: %s" % str(e))
    return True

  def on_error(self, status):
    print(status)
    return True

twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=['#GasteizMakerDay'])

