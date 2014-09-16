#!/usr/bin/python
# -*- coding: utf-8 -*-
import mechanize


def testProxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print source_code


url = 'http://wtfismyip.com/'
hideMeProxy = {'http': '127.0.0.1:8118'}

testProxy(url, hideMeProxy)


