#!/usr/bin/python

from LinkedList import LinkedList

pList = []
myList = LinkedList()

count = 0
while count < 10 :
	pList.append(count)
	myList.append(count)
	count += 1

count = 0
while count < len(pList) :
	print pList[count]
	print myList.get(count)
	count += 1

