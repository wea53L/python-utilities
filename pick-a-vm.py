#! /usr/bin/python

# pick-a-vm
# goal is to find a random VM from Vulnhub.com
# warrenkopp@gmail.com
# frequentlyinaccurate.net


# start
from feedparser import parse
from random import randint
from urllib import urlretrieve
from os import path
from urlparse import urlsplit

# Plan A: pull rss, parse for VMs, random picker, output links(?)
vh_feed = parse("http://www.vulnhub.com/feeds/torrent/atom/")
vh_total = len(vh_feed['entries'])
seed = int(vh_total-1)

vm_pick =  randint(0,seed)
print "pick = # %s" % vm_pick

print vh_feed['entries'][vm_pick]['title']

# take torrent url, put file in ~/Downloads for transmission to find

pick_url = vh_feed['entries'][vm_pick]['link']
print pick_url

vm_pick_filename = path.basename(urlsplit(pick_url).path)
vm_pick_filename = "/Users/warrenkopp/Downloads/" + vm_pick_filename

print vm_pick_filename

# if block to avoid overwrite existing thing of name
if not path.isfile(vm_pick_filename):
 	urlretrieve (pick_url, vm_pick_filename)








# footer / references
# http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python
# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
# http://stackoverflow.com/questions/10552188/python-split-url-to-find-image-name-and-extension