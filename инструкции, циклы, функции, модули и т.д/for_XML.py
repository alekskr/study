from lxml import etree

xml_string = "<a><b>hello</b></a>"

root = etree.fromstring(xml_string)

print(type(root))  # <class 'lxml.etree._Element'>