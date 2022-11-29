#open command prompt or you're version of it
#install pyshorteners
#type "pip install pyshorteners" then press enter
# Go !

import pyshorteners
url = input ("Enter URL you want to shorten:")
shortener = pyshorteners. Shortener()
x = shortener.tinyurl.short(url)
print(x)
