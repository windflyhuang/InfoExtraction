# coding:utf-8
import xml.etree.ElementTree as ET

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding="utf-8")

        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def output_xml(self,dataset):
        for data in dataset:
            body=ET.Element("body")
            title_head=ET.SubElement(body,'title_head')
            title_head.text=data['title_head']
            title_main = ET.SubElement(body, 'title_main')
            title_main.text = data['title_main']
            summary=  ET.SubElement(body, 'summary')
            summary.text=data['summary']
            infobox=ET.SubElement(body, 'infobox')
            if data['infobox']:
               for key in data['infobox']:
                   node=ET.SubElement(infobox,key)
                   node.text=data['infobox'][key]
            later_text = ET.SubElement(body, 'later_text')
            later_text.text=data['later_text']
            # 创建elementtree对象，写文件
            tree = ET.ElementTree(body)
            xmlfile_path="data/"+data['title_head']+data['title_main']+".xml"
            tree.write(xmlfile_path,encoding='GB2312')



