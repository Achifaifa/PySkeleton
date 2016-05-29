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

testdata=[["2015-20-20 :: 13:37:04", "@blaubleublue", "Complex system replacements feel like like they'll be simpler and faster to build. But that is because human brains can only hold cartoons.", "avatar1"], ["date2", "user2", "Complex system replacements feel like like they'll be simpler and faster to build. But that is because human brains can only hold cartoons.", "avatar2"],["date3", "user3", "Complex system replacements feel like like they'll be simpler and faster to build. But that is because human brains can only hold cartoons.", "avatar3"], ["date4", "user4", "Complex system replacements feel like like they'll be simpler and faster to build. But that is because human brains can only hold cartoons.", "avatar4"]]

w=windows.update_window()
w.send(None)
for i in testdata: 
  w.send(i)
  import time; time.sleep(3)