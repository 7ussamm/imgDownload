import random
import urllib.request
import os

url = input('Enter url you need: ') #usr prefered image url
dirr = input('Paste here your location: ') #usr prefered location
os.chdir(dirr)

def dwn(url):
    nme = random.randint(1, 1000)
    imgNme = str(nme) + '.jpg' #gives the img a random name
    urllib.request.urlretrieve(url, imgNme)
dwn(url)