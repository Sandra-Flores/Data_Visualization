import instagram
import requests
import urllib
from urllib import urlopen
from instagram.client import InstagramAPI

# using the access token
access_token = "3132861916.1677ed0.93a9d071ab1b4659b7cf46905bf5ebe8"
client_secret = "92bde21f90a04c39b71dbfabf2540e70"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

f=urlopen("https://api.instagram.com/v1/locations/{location-id}/media/recent?access_token=3132861916.1677ed0.93a9d071ab1b4659b7cf46905bf5ebe8").read()

print f
