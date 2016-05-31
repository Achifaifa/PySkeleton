#! /usr/bin/env python

import json, os, serial, time, tweepy
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
      for i in range(3)
        a.send("0,255,0")
        time.sleep(0.5)
        a.send("255,255,255")
        time.sleep(0.5)

    except BaseException as e:

      print("----------------------\n",e)

    finally:

      return True

  def on_error(self, status):
    print(status)
    return True

a=serial.Serial()
a.setBaudrate=(9600)
a.setPort("/dev/ttyACM0")
a.open()
a.send("255,255,255")
twitter_stream = Stream(auth, listener())
twitter_stream.filter(track=['#gasteizmakerday'])