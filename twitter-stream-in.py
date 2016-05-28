#! /usr/bin/env python

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import apikeys
import windows

# auth = OAuthHandler(apikeys.apikey, apikeys.apisecret)
# auth.set_access_token(apikeys.consumerkey, apikeys.consumersecret)
# api = tweepy.API(auth)

class listener(StreamListener):

  def on_data(self, data):
    try:
      text=data["text"]
      user="%s (@%s)"%(data["user"]["name"],data["user"]["screen_name"])
      date=data["created_at"]
      avatar=data["user"]["profile_image_url"].replace("\/","/")

      updatescreen(date,user,text,avatar)
    except BaseException as e:
      with open('./log', 'a') as f:
        print("\n----------------------\nError on_data: %s\n" % str(e))
    finally:
      return True

  def on_error(self, status):
    print(status)
    return True

# twitter_stream = Stream(auth, listener())
# twitter_stream.filter(track=['#GasteizMakerDay'])
# 

testdata=[["date1", "user1", "text1", "avatar1"], ["date1", "user1", "text1", "avatar1"],["date1", "user1", "text1", "avatar1"], ["date1", "user1", "text1", "avatar1"]]

w=windows.update_window()
w.send(None)
for i in testdata: 
  w.send((testdata[0],testdata[1],testdata[2],testdata[3]))
  import time; time.sleep(3)