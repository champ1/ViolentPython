import json
import urllib
import optparse
from anonBrowser import *

class Google_Result:

  def __init__(self,title,text,url):
    self.title = title
    self.text = text
    self.url = url

  def __repr__(self):
    return self.title

def google(search_term):
  ab = anonBrowser()
  search_term = urllib.quote_plus(search_term)
  response = ab.open('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + search_term)
  objects = json.load(response)
  results = []
  for result in objects['responseData']['results']:
    url = result['url']
    title = result['titleNoFormatting']
    text = result['content']
    new_gr = Google_Result(title, text, url)
    results.append(new_gr)
    return results

def main():

  keyword = 'Boondock Saint'
  results = google(keyword)
  print results

if __name__ == '__main__':
  main()
