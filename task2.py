#!/usr/bin/python

from xml.etree import ElementTree as et

tree = et.parse("task2.xml")
root = tree.getroot()
member = tree.find("timeout")
member.text = "15s"
tree.write("task2-output.xml") 


