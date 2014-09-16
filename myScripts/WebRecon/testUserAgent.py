import mechanize

def testUserAgent(url,userAgent):
  browser = mechanize.Browser()
  browser.addheaders = userAgent
#  browser.set_proxies(proxy)
  page = browser.open(url)
  source_code = page.read()
  print source_code


url = 'http://whatismyuseragent.dotdoh.com/'
userAgent = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.2) Gecko/20010726 Netscape6/6.1')]
#hideMeProxy = {'http':'221.10.40.237:82'}
testUserAgent(url,userAgent)
