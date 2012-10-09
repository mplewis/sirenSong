#!/usr/bin/python

# Run this from /etc/profile as follows to pass in the right data:
#     python sirenSong.py `hostname` $SSH_CLIENT `date +'%a %b %d, %I:%M %P %Z'` 

# for key in os.environ:
#     print key, os.getenv(key)

import os
import string
import urllib2
import json

def getEnvKey(key):
	return os.getenv(key)

hostIp   = urllib2.urlopen('http://ip.42.pl/raw').read()
hostname = string.replace(os.popen('hostname').read(), '\n', '')

# ipDataRaw = '134.84.72.136 50350 38426'
ipDataRaw = getEnvKey('SSH_CLIENT')
ipData = string.split(ipDataRaw)

clientIp   = ipData[0]
clientPort = ipData[1]
serverPort = ipData[2]

# clientIpLoc = 'Baldwinsville, NY, US'
clientIpLocData = json.load(urllib2.urlopen('http://freegeoip.net/json/' + clientIp))
clientIpLoc = clientIpLocData['city'] + ', ' + clientIpLocData['region_code'] + ', ' + clientIpLocData['country_code']

dateAndTime = string.replace(os.popen("date +'%a %b %d, %I:%M %P %Z'").read(), '\n', '')

# Tue Oct 09, 01:10 am CDT: Access on HostName, port 31337 from 24.24.24.24 (New Brunswick, Canada).
message = dateAndTime + ": Access on " + hostname + ", port " + serverPort + " from " + clientIp + " (" + clientIpLoc + ")."

print message