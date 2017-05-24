# -*- coding: utf-8 -*-

import re
from py3_common import download

import xmltodict


def crawl_sitemap(url):
    '''正则抽取链接'''
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall(r'<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...


def crawl_sitemap_xmltodict(url):
    '''xmltodict包取链接'''
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = xmltodict.parse(sitemap)['urlset']['url']
    # download each link
    for link in links:
        html = download(link['loc'])
        # scrape html here
        # ...


if __name__ == '__main__':
    crawl = crawl_sitemap_xmltodict
    crawl('http://example.webscraping.com/sitemap.xml')
