#!/usr/bin/env python

#system tools
import os, sys, pprint

#api tools
import requests, base64, json

#handy
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

CONSUMER_KEY = 'hcvgASeCyxkz4fGbsyA9yt9WD'  
CONSUMER_SECRET = 'bvSuLB49sVBlyu7jILbJU2IpRH8BqGmBy0ClZ48KpnLTKFJAsx'

#the base twitter url for sending api requests
URL = 'https://api.twitter.com/oauth2/token'

#the search term to be used
SEARCH_TERM = 'techcrunch'

#base64 encode credentials
credentials = base64.urlsafe_b64encode('%s:%s' % (CONSUMER_KEY, CONSUMER_SECRET))

#custom headers for the api keys
custom_headers = {
    'Authorization': 'Basic %s' % (credentials),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
}

grant_type_data = 'grant_type=client_credentials'


#putting it all together
response = requests.post(URL, headers=custom_headers, data=grant_type_data)

#what is in this thing?
# print response.json()


#dump token to variable
access_token = response.json().get('access_token')
# access_token = response.json()['access_token']

#custom for the search api
search_headers = {'Authorization': 'Bearer %s' % (access_token)}

#send the request
response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=%s&count=100' % SEARCH_TERM, headers=search_headers)

pp = pprint.PrettyPrinter(indent=2)

# print response.json().get('statuses')[0].keys()
# print response.json().get('statuses')[0]['text']
#print response.json().get('statuses')[0]['user'].keys()

#pp.pprint(response.json().get('statuses')[1]['user'])

#profile_image_url, screen_name, created_at, time_zone, location

tweet_list = response.json().get('statuses')

for tweet in tweet_list:
    tweet_location = tweet.get('user').get('location')

    if tweet_location != '' and tweet_location != None:

        print "TWEET-------------"
        print tweet.get('user').get('profile_image_url')
        print tweet.get('user').get('screen_name')
        print tweet.get('user').get('created_at')
        print tweet.get('user').get('location')
        print "TWEET-TEXT---------"
        print tweet.get('text')


#include a field for search term on the Tweet model


