#! /usr/bin/env python
#
# PROJECT NAME : DeskQuote
# DESCRIPTION  : Delivers random quote at your desktop at fixed time from http://www.brainyquote.com
# AUTHOR       : Daxeel Soni
# AUTHOR EMAIL : sayhi@daxeelsoni.in
# AUTHOR WEB   : www.daxeelsoni.in
#
# Copyright (c) 2016, Daxeel Soni
# All rights reserved.

from bs4 import BeautifulSoup
import urllib2
from pync import Notifier
from random import randint
from time import sleep
import sys

args = sys.argv # Parsing arguments
base_url = "http://www.brainyquote.com/quotes/topics/topic_"

# Categories
categories = {
	1: ['inspirational', 13],
	2: ['motivational', 8]
	3: ['success', 38]
}

def make_quote():
	select_category = randint(1, 3)
	select_page = randint(1, categories[select_category][1])
	select_quote = randint(0, 25)

	final_url = base_url + categories[select_category][0] + str(select_page) + '.html'

	req = urllib2.Request(final_url, headers={'User-Agent' : "DeskQuote"})
	html = urllib2.urlopen(req)
	soup = BeautifulSoup(html, "html.parser")

	quote = soup.find_all('span', {'class': 'bqQuoteLink'})[select_quote].text
	link = "http://www.brainyquote.com" + soup.find_all('span', {'class': 'bqQuoteLink'})[select_quote].a['href']

	Notifier.notify(quote, title='DeskQuote', open=link) # Push desktop notification for new tweet

if len(args) == 3:
	while True:
		make_quote()
		sleep(int(args[2]))
else:
	print "Invalid syntax. Checkout docs at https://github.com/daxeel/DeskQuote"

	
