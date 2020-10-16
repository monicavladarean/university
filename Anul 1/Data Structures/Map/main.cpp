#include"ShortTest.h"
#include"ExtendedTest.h"
#include"Map.h"
#include"MapIterator.h"
#include<iostream>
#include<assert.h>

int main()
{
	Map m;
	MapIterator id = m.iterator();
	m.add(1, 1);
	id.first();
	std::cout << "(" << id.getCurrent().first << " , " << id.getCurrent().second << ")";
	m.add(2, 2);
	m.add(3, 3);
	id.jumpForward(2);
	std::cout << "(" << id.getCurrent().first << " , " << id.getCurrent().second << ")";
	
	testAll();
	return 0;
} 