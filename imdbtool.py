#!/usr/bin/env python

import argparse
import urllib
import sys
import json

parser = argparse.ArgumentParser(description='Get IMDb data for a movie')

parser.add_argument("-t", help="Movie title")
parser.add_argument("-y", help="Year of release", type=int)
parser.add_argument("-i", help="IMDb movie id")
parser.add_argument("-r", help="Return raw XML/JSON response", choices=['JSON','XML'])
parser.add_argument("--plot", help="Length of plot summary", choices=['short','full'])
parser.add_argument("--tomatoes", help="Include Rotten Tomatoes data too", action="store_true")

args = parser.parse_args()

params = {}
keys = ['t', 'y', 'i', 'plot', 'r', 'tomatoes']

for k in keys:
  if args.__getattribute__(k): params[k] = args.__getattribute__(k)

if len(params) == 0:
  parser.print_usage()
  sys.exit()


### call IMDb API

apicall = urllib.urlopen('http://www.omdbapi.com/?%s' % urllib.urlencode(params))
result = apicall.read()
apicall.close()

# print raw output and exit, if raw output was requested
if args.r:
  print result
  sys.exit()

# print requested info

data = json.loads(result)
for k in data:
  print k.lower() + ":"
  print data[k].encode('utf-8')
  print "\n"
