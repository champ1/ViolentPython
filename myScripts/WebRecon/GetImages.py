from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os, optparse

def mirrorImages(url,dir):

  ab = anonBrowser()
  ab.anonymize()
  html = ab.open(url)
  soup = BeautifulSoup(html)
  image_tags = soup.findAll('img')
  
  for image in image_tags:
    filename = image['src'].lstrip('http://')
    filename = os.path.join(dir,filename.replace('/','_'))
    print '[+] Saving ' + str(filename)
    data = ab.open(image['src']).read()
    ab.back()
    save = open(filename, 'wb')
    save.write(data)
    save.close()

def main():

  dir = '/tmp'
  url = 'http://xkcd.com'
  mirrorImages(url,dir)

if __name__ == '__main__':
  main()
