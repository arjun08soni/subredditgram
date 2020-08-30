from telegram.ext import Updater, CommandHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from urllib.parse import urlparse
import telegram                       
import requests
import re
import urllib.request
import json
import tldextract
import urllib
import urllib.error
import praw
data=[]
reddit=praw.Reddit(client_id="your_client_id",client_secret="your_client_secret",user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")

def top(bot, update,args):
    evaluate(bot,update,args) 
    sub_reddit=data[0]
    time=data[1]
    limit=data[-1]
    print('top','r/'+sub_reddit,time,limit)
    topsub=reddit.subreddit(sub_reddit).top(time,limit=int(limit))  
    postdata(bot,update,topsub) 

def hot(bot, update,args):
    evaluate(bot,update,args) 
    sub_reddit=data[0]
    limit=data[1]
    print('hot','r/'+sub_reddit,limit)
    hotsub=reddit.subreddit(sub_reddit).hot(limit=int(limit))  
    postdata(bot,update,hotsub) 

def new(bot, update,args):
    evaluate(bot,update,args) 
    sub_reddit=data[0]
    limit=data[1]
    print('new','r/'+sub_reddit,limit)
    newsub=reddit.subreddit(sub_reddit).new(limit=int(limit))
    postdata(bot,update,newsub)

def evaluate(bot,update,args):
    data.clear()
    length=len(args)
    if length==0:
        bot.send_message(chat_id=chat_id,text="Enter the name of the subreddit. Example command: /top pics 3 month. Where 3 is the number of posts and other options for time is: day, week, month, year, all")
    elif length!=0:
        for i in args:
            try:
                if type(int(i))==int and int(i)>30:
                    limit=i #change i to limit more than 30
                    print("Try less number please")
                elif type(int(i))==int:
                    limit=i
            except: data.append(i)
        data.append(limit)
    return data



def postdata(bot,update,hotsub):
    chat_id = update.message.chat_id
    count=1
    for submission in hotsub:
            print(str(count),submission.title)
            info = tldextract.extract(submission.url)
            # print(info)

            try:
                if info.domain=='imgur':
                    if "gifv" in submission.url:
                        gif=submission.url.replace('gifv','mp4')
                        bot.send_animation(chat_id=chat_id,animation=gif,caption="Post "+str(count)+": "+submission.title)
                    else: bot.sendPhoto(chat_id=chat_id,photo=submission.url,caption="Post "+str(count)+": "+submission.title)
                elif info.domain=='redd':
                    bot.sendPhoto(chat_id=chat_id,photo=submission.url,caption="Post "+str(count)+": "+submission.title)
                elif info.domain=='redgifs' or info.domain=='gfycat': 
                    video=submission.preview['reddit_video_preview']['fallback_url']
                    bot.send_video(chat_id=chat_id,video=video,caption="Post "+str(count)+": "+submission.title)
                elif info.domain=='instantfap':
                    bot.sendMessage(chat_id=chat_id,text=submisson.url,caption="Post "+str(count)+": "+submission.title)
                else: bot.sendMessage(chat_id=chat_id,text="Post "+str(count)+": "+submission.title+" "+submission.url)
            except BadRequest:
                bot.sendMessage(chat_id=chat_id,text="Post "+str(count)+": "+submission.url)
            except KeyError:
                bot.sendMessage(chat_id=chat_id,text="Post "+str(count)+": "+submission.url)
            count+=1

def main():
    updater = Updater('your_telegram_bot_token')                    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('top',top,pass_args=True))
    dp.add_handler(CommandHandler('hot',hot,pass_args=True))
    dp.add_handler(CommandHandler('new',new,pass_args=True))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
