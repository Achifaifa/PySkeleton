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
      text="\n".join([i if i for i in text.split("\n")])
      user="%s (@%s)"%(data["user"]["name"],data["user"]["screen_name"])
      date=data["created_at"]

      # Get image
      # os.system("rm avatar")
      # avatar=data["user"]["profile_image_url"].replace("\/","/")
      # zz=os.system("wget %s -o avatar 2> /dev/null"%avatar)
      # avatar="avatar" if not zz else "init.jpg"

      w.send((date,user,text))#,avatar))

    except BaseException as e:

      print("----------------------\n",e)

    finally:

      return True

  def on_error(self, status):
    print(status)
    return True

twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=['#gasteizmakerday'])