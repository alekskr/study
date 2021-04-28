from lxml import etree

file = open('index.xml', 'r', encoding='UTF-8')

root = etree.parse(file).getroot()
etree.dump(root)

for i in root[0]:
    print(i.get('name'))


a = '<a attr="123"><b attr="456"/><c/></a>'
b = 'attr'

root = etree.fromstring(a)
attribute = root[0].get(b)

if attribute:
    print(attribute)
else:
    print(None)