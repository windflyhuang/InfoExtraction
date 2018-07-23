# coding:utf-8
from bs4 import BeautifulSoup
import re
import urllib.parse
from baike_spider import html_downloader


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        if(soup.find('ul', class_=["custom_dot", "para-list", "list-paddingleft-1"])):
           links=soup.find('ul', class_=["custom_dot", "para-list", "list-paddingleft-1"]).find_all('a', href=re.compile(
               r'/item/'))
           for link in links:
               new_url = link['href']
               new_full_url = urllib.parse.urljoin(page_url, new_url)
               new_urls.add(new_full_url)
        else:
            new_urls.add(page_url)
            if(soup.find_all('a', href=re.compile(r'#viewPageContent'))):
               links = soup.find_all('a', href=re.compile(r'#viewPageContent'))
               for link in links:
                  new_url = link['href']
                  new_full_url = urllib.parse.urljoin(page_url, new_url)
                  new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        #获取title
        title_node1 = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title_head'] = title_node1.get_text().strip()
        res_data['title_main'] =''
        if(soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h2')):
           title_node2= soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h2')
           res_data['title_main']=title_node2.get_text().strip()
        # 获取台风简介
        res_data['summary']=''
        if (soup.find('div', class_="lemma-summary").find('div')):
           summary_node = soup.find('div', class_="lemma-summary").find('div')
           res_data['summary'] = summary_node.get_text().strip()

        # 获取结构化信息
        res_data['infobox']={}
        if(soup.find('div', class_="basic-info cmn-clearfix")):
           infobox = {}
           infobox_listname=soup.find('div', class_="basic-info cmn-clearfix").find_all('dt',class_='basicInfo-item '
                                                                                                   'name')
           infobox_listvalue=soup.find('div', class_="basic-info cmn-clearfix").find_all('dd',class_='basicInfo-item '
                                                                                                  'value')
           namelist = []
           for namenode in infobox_listname:
               namelist.append(namenode.get_text().strip())
           valuelist = []
           for valuenode in infobox_listvalue:
               valuelist.append(valuenode.get_text().strip())
           # for namenode,valuenode in infobox_listname,infobox_listvalue:
           for i in range(0, len(namelist)):
               infobox[namelist[i]] = valuelist[i]
           res_data['infobox'] = infobox

        #获取后续内容class="para"
        later_text=''
        text_nodelist=soup.find_all('div', class_="para")
        for text_node in text_nodelist:
            later_text+=text_node.get_text().strip()
        res_data['later_text']=later_text

        return res_data

    def paser_urls(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls

    def paser_content(self, new_urls):
        dataset=[]
        for pageurl in new_urls:
            page_html=html_downloader.HtmlDownloader().download(pageurl)
            soup_obj= BeautifulSoup(page_html, 'html.parser', from_encoding='utf-8')
            new_data = self._get_new_data(pageurl, soup_obj)

            dataset.append(new_data)
        return dataset
