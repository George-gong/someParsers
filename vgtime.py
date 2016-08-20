# coding=utf8

import urllib2

from lxml import etree


PS_FORUMN_URL = 'http://bbs.vgtime.com/module_57.xhtml'


class Spider(object):
    
    def __init__(self, url):
        self.url = url
        
    def parse(self):
        pass
    
    def _request(self, url=None):
        """ http request
        """
        if not url:
            url = self.url
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        return res.read()


class VgtimeSpider(Spider):

    
    def parse(self):
        body = self._request()
        root = etree.HTML(body)
        url_list = root.xpath("//ul[contains(@id,'content')]/li/descendant::a/@href")
        print url_list


if __name__ == "__main__":
    VgtimeSpider(PS_FORUMN_URL).parse()
