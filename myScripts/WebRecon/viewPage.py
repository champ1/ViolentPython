import mechanize

def testProxy(url,proxy):
  browser = mechanize.Browser()
  browser.set_proxies(proxy)
  page = browser.open(url)
  source_code = page.read()
  print source_code


url = 'http://whatismyuseragent.dotdoh.com/'
hideMeProxy = {'http':'221.10.40.237:82'}
testProxy(url,hideMeProxy)
