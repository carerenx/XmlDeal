import json
import xmltodict

from xml.etree import ElementTree as Et
from xml.dom.minidom import parse

xmlFile = parse("../demo.xml")
# print(xmlFile.toprettyxml())
xmlString=xmlFile.toprettyxml()


# xmlFile=Et.parse("../demo.xml")
# xmlFile.
# xmlRoot=xmlFile.getroot()
# print(xmlRoot)

xmlJson=json.dumps(xmltodict.parse(xmlString),indent=4)
print(xmlJson)

# with open是python 中打开文件的命令，在使用完毕后会自动关闭。mode有w/r/a，w：删除后写入，a：尾部添加写入，r：读取
with open('demo.json', mode='w', encoding='utf-8', newline='') as f:
    f.write(xmlJson)
