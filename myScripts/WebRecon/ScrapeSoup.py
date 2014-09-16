from anonBrowser import *
from BeautifulSoup import BeautifulSoup
import os, optparse

def printLinks(url):

  ab = anonBrowser()
  ab.anonymize()
  page = ab.open(url)
  html = page.read()
  try:
    print 'Printing links from BeautifulSoup'
    soup = BeautifulSoup(html)
    links = soup.findAll(name='a')
    for link in links:
      if link.has_key('href'):
        print link['href']
  except:
    pass

def main():

  url = 'http://www.hampsterdance.com'
  printLinks(url)

if __name__ == '__main__':
  main()
