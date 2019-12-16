#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 9 14:36:24 2019

@author: James Farmer

Version 1.0.1
ChangeLog:
    1.0.1: changed the txtpath to use os.path module, ensuring that the path to
            text files is correct regardless of how the program is initiated.
    
Calls an instance of printing_press.Editor and sends the articles to the Slack
channel ID specified in the accompanying text file 'channel.txt'

#### IMPORTANT ####
This code requires you to have already registered a new Slack App, and added
the bot user token to your system environment variables. See documentation at
https://github.com/jtfarm/paperboy-academic for details.
"""
nKeywordMatches = 2
files = {
        'authors':'authors.txt',
        'channel':'channel.txt',
        'feeds':'feeds.txt',
        'keywords':'keywords.txt'
        }

import slack
import ssl as ssl_lib
import certifi
from printing_press import Editor
import os

txtpath = os.path.dirname(os.path.abspath(__file__)) + '/userTextFiles/'

kwargs = dict((v,txtpath+files[v]) for v in files)
kwargs.update({'nLow':nKeywordMatches})

def send_message(article):
    return client.chat_postMessage(**article)


if __name__ == "__main__":
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    editor = Editor(**kwargs)
#    with open('token.txt') as f:
#        slack_token = f.read()
    slack_token = os.environ['SLACK_TOKEN']
    client = slack.WebClient(token=slack_token,ssl=ssl_context)
    results = [send_message(art) for art in editor.articles]
