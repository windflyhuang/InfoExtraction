# coding:utf-8
from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url,str_typthon):
        fullurl,html_cont = self.downloader.downloadwithname(root_url,str_typthon)
        new_urls= self.parser.paser_urls(fullurl, html_cont)
        print("craw %s : %s" % (str_typthon, new_urls))
        dataset=self.parser.paser_content(new_urls)
        self.outputer.output_xml(dataset)




if __name__ == '__main__':
    fobj = open('typhon.txt',encoding='utf-8')
    sourceInLines =fobj.readlines()
    obj_spider = SpiderMain()
    for line in sourceInLines:
        str_typthon="台风"+line.strip()
        root_url='https://baike.baidu.com/item/'
        #root_url = "https://baike.baidu.com/item/%E5%8F%B0%E9%A3%8E%E8%BE%BE%E7%BB%B4/20352148"
        obj_spider.craw(root_url,str_typthon)

