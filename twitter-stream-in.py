#! /usr/bin/env python

import json, os, tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import apikeys, windows

auth = OAuthHandler(apikeys.apikey, apikeys.apisecret)
auth.set_access_token(apikeys.consumerkey, apikeys.consumersecret)
api = tweepy.API(auth)
w=windows.update_window()
w.send(None)

class listener(StreamListener):

  def on_data(self, data):
    try:

      data=json.loads(data)

      text=data["text"]
      user="%s (@%s)"%(data["user"]["name"],data["user"]["screen_name"])
      date=data["created_at"]

      # Get image
      # os.system("rm avatar")
      # avatar=data["user"]["profile_image_url"].replace("\/","/")
      # zz=os.system("wget %s -o avatar 2> /dev/null"%avatar)
      # avatar="avatar" if not zz else "init.jpg"

      w.send((date,user,text))#,avatar))

    except BaseException as e:

      with open('./log', 'a') as f:
        print("\n----------------------\nError on_data: %s" % str(e))

    finally:

      return True

  def on_error(self, status):
    print(status)
    return True

twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=['#followback'])
# 

# testdata=[["2015-20-20 :: 13:37:04", "@blaubleublue", "Complex system replacements feel like like they'll be simpler and faster to build. But that is because human brains can only hold cartoons.", "avatar1"], 
# ["2015-20-20 :: 13:37:10", "@trex", "buy my new shirt, 'i object to the use of the word waifu, but i think you are welcome to like any anime cutie you want'", "avatar2"],
# ["2015-20-20 :: 13:39:11", "@amazewalls", "Coroutines and generators are awesome", "avatar3"], 
# ["2015-20-20 :: 13:47:44", "@totallynotabot", "Beautiful new large-scale brain etchings from the fantastic Gregg Dun thepipetteer.com/self-reflected... pic.twitter.com/SNFkSgoUkw", "avatar4"]]

# for i in testdata: 
#   w.send(i)
#   import time; time.sleep(10)