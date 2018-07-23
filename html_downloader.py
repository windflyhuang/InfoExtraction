# coding:utf-8
import urllib.request
import sys
import time
import socket

class HtmlDownloader(object):

    def downloadwithname(self, url,typhoname):
        if url is None:
            return None
        socket.setdefaulttimeout(10)  # 设置socket层的超时时间为20秒
        typhon=urllib.parse.quote(typhoname)
        full_url=url+typhon
        response = urllib.request.urlopen(full_url)
        htmlcont=response.read()
        if response.getcode() != 200:
            return None
        response.close()
        time.sleep(2)
        return full_url,htmlcont
    def download(self, url):
        if url is None:
            return None
        socket.setdefaulttimeout(10)  # 设置socket层的超时时间为20秒
        response = urllib.request.urlopen(url)
        htmlcont = response.read()

        if response.getcode() != 200:
            return None
        response.close()
        time.sleep(2)
        return htmlcont