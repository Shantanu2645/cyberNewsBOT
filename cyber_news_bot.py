#!/usr/bin/env python3

import feedparser
import requests
import time

bleeping_url = "https://www.bleepingcomputer.com/feed/"
packetstorm_url  = 'https://rss.packetstormsecurity.com/'
theHNews_url = "https://feeds.feedburner.com/TheHackersNews"
nakedsec_url = "https://nakedsecurity.sophos.com/feed/"
hackaday_url = "https://hackaday.com/blog/feed/"

try:
    bleeping_feed = feedparser.parse(bleeping_url).entries[0]
    thehackernews_feed  = feedparser.parse(theHNews_url).entries[0]
    nakedsec_feed       = feedparser.parse(nakedsec_url).entries[0]
    packetstorm_feed    = feedparser.parse(packetstorm_url).entries[0]
    hackaday_feed = feedparser.parse(hackaday_url).entries[0]

except IndexError:
    bleeping_feed = {}
    thehackernews_feed  = {}
    nakedsec_feed    = {}
    packetstorm_feed = {}
    hackaday_feed = {}

def bleeping():
    global bleeping_feed
    global bleeping_url

    try:
        if not bleeping_feed:
            bleeping_feed = feedparser.parse(bleeping_url).entries[0]

        else:
            feed = feedparser.parse(bleeping_url)
            latest_feed_entry = feed.entries[0]
            if latest_feed_entry['title'] != bleeping_feed['title']:

                news = {
                        "content": latest_feed_entry['title']+"\n"+latest_feed_entry.link,
                        "username": "BleepingNews",
                        "avatar_url": "https://w7.pngwing.com/pngs/507/494/png-transparent-adwcleaner-potentially-unwanted-program-adware-browser-hijacking-computer-software-computer-computer-logo-computer-program-thumbnail.png",
                        "attachments": []
                       }
                requests.post(webhook_url,json=news)
            bleeping_feed = latest_feed_entry
            time.sleep(interval)
    except IndexError:
        pass

def thehackernews():
    global thehackernews_feed
    global theHNews_url
    try:
        if not thehackernews_feed:
            thehackernews_feed  = feedparser.parse(theHNews_url).entries[0]
        else:
            feed = feedparser.parse(theHNews_url)
            latest_feed = feed.entries[0]

            if latest_feed['title'] != thehackernews_feed['title']:
                news = {
                    "content": latest_feed['title']+"\n"+latest_feed['link'],
                    "username": "The Hacker News",
                    "avatar_url": "https://thehackernews.com/new-images/img/b/R29vZ2xl/AVvXsEjucioIaLjDLMVbAzsIDpaYM754ZmWwLu6oPFfZ95bcJQK9paBjdrkpQnnjTExUWJbExlV10x25riYersOaWF_TFGCFvlw52qXMvrNMGacAb6nkP1RBTMGL1yWdvoajXbj5qf4U9O_sH6tH-BxNpOveZnxMT6bVDX57FaKB1jFlbPExVQgmA4HKKuROJA/s1700/THN.jpg",
                    "attachments": []
                    }
                requests.post(webhook_url,json=news)
                thehackernews_feed = latest_feed
            time.sleep(interval)
    except IndexError:
        pass

def nakedsecurity():
    global nakedsec_feed
    global nakedsec_url
    try:
        if not nakedsec_feed:
            nakedsec_feed = feedparser.parse(nakedsec_url).entries[0]
        else:
            feed = feedparser.parse(nakedsec_url)
            latest_feed = feed.entries[0]
            if latest_feed != nakedsec_feed :
                news ={
                    "content": latest_feed['title']+"\n"+str(latest_feed['links'][0]['href']),
                    "username": "Naked Security - Sophos",
                    "avatar_url": "https://media.licdn.com/dms/image/C4D0BAQG7JPzNAuTXEA/company-logo_200_200/0/1579611356895?e=2147483647&v=beta&t=f8GxbDi1dQIjgSAx_QverApaq8lPIEM8IzZAjCOCXl8",
                    "attachments": []
                    }
                requests.post(webhook_url,json=news)
            nakedsec_feed = latest_feed
            time.sleep(interval)
    except IndexError:
        pass

def packetstorm():
    global packetstorm_feed
    global packetstorm_url
    try:
        if not packetstorm_feed:
            packetstorm_feed    = feedparser.parse(packetstorm_url).entries[0]
        else:
            feed = feedparser.parse(packetstorm_url)
            latest_news_feed = feed.entries[0]
            if latest_news_feed != packetstorm_feed:
                latest_update_url = requests.get(latest_news_feed['links'][0]['href']).url
                news ={
                    "content": latest_news_feed['title']+"\n"+latest_update_url,
                    "username": "Hero Alom - The Unstoppable Character",
                    "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/5/55/Hero_Alom.png",
                    "attachments": []
                }
                requests.post(webhook_url,json=news)
                packetstorm_feed = latest_news_feed
            time.sleep(interval)
    except IndexError:
        pass

def hackaday():
    global hackaday_feed
    global hackaday_url
    try:
        if not hackaday_feed:
            hackaday_feed = feedparser.parse(hackaday_url).entries[0]
        else:
            feed = feedparser.parse(hackaday_url)
            hackaday_latest_feed = feed.entries[0]
            if hackaday_latest_feed['title'] != hackaday_feed['title']:
                news = {
                        "content": hackaday_latest_feed['title']+"\n"+hackaday_latest_feed['link'],
                        "username": "Hackaday",
                        "avatar_url": "https://hackaday.com/wp-content/uploads/2013/02/had_green_glow.png",
                        "attachments": []
                        }
                requests.post(webhook_url, json=news)
                hackaday_feed = hackaday_latest_feed
            time.sleep(interval)

    except IndexError:
        pass

webhook_url = "https://discordapp.com/api/webhooks/1072062492731260968/nOIZYgVMTMbShuwwV9IukiQlelCLaxMkSMA4CxBwkX_Ywve3AMWa6J9fTOB29RnTB9FC"
interval = 12

while True:
    bleeping()
    thehackernews()
    nakedsecurity()
    packetstorm()
    hackaday()
