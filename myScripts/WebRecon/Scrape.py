from anonBrowser import *
import os, optparse, re

def printLinks(url):

  ab = anonBrowser()
  ab.anonymize()
  page = ab.open(url)
  html = page.read()
  try:
    print 'Printing links from Regex'
    link_finder = re.compile('href="(.*?)"')
    links = link_finder.findall(html)
    for link in links:
      print link
  except:
    pass

def main():

  url = 'http://www.hampsterdance.com'
  printLinks(url)

if __name__ == '__main__':
  main()
