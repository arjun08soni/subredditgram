# subredditgram
This is Telegram bot to browse your favourite subreddits directly on your Telegram.
I've used PRAW to get API access. 
https://python-telegram-bot.org/ for Telegram bot API wrapper built on python

you must authenticate on praw to get access id. https://praw.readthedocs.io/en/latest/

Commands available on bot:
/hot subreddit_name number_of_posts                 example: /hot learnjavascript 10 -You will recieve 10 hot posts from the sub 'learnjavascript'
/new subreddit_name number_of_posts                 example: /new learnjavascript 10 -You will recieve 10 newest or latest posts from the sub 'learnjavascript'
/top subreddit_name number_of_posts time_period     example: /top learnjavascript 10 month -You will recieve 10 top posts of the month from the sub 'learnjavascript'
                                    time_period=month/all/year/week
