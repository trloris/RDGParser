import sys
import xml.etree.ElementTree as ET


def search(group, description, location=''):
	name = group.find('./properties/name')
	servers = group.findall('./server')
	location = '%s -> %s' % (location, name.text)
	if servers:
		for server in servers:
			server_name = server.find('./displayName')
			if description == server_name.text:
				print location
	else:
		groups = group.findall('./group')
		for group in groups:
			search(group, description, location)

xml_file = sys.argv[1]
description = sys.argv[2]

tree = ET.parse(xml_file)

root = tree.getroot()

groups = root.findall('./file/group')

for group in groups:
	search(group, description)