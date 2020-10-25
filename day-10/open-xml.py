import xml.etree.ElementTree as ET

tree = ET.parse('person.xml')
root = tree.getroot()
print('Root tag: ', root.tag)
print('Attribute: ', root.attrib)

for child in root:
    print('field: ', child.tag)
