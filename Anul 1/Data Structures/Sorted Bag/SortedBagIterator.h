#pragma once
#include <iostream>
#include "SortedBag.h"

typedef int TComp;

typedef TComp TElem;

//class SortedBag;

class SortedBagIterator
{
	friend class SortedBag;

private:
	//the iterator stores a reference to the container 
	SortedBag& bag;
	//other specific attributes: current, etc
	int current;
	SortedBagIterator(SortedBag& bag);

public:
	TComp getCurrent();
	bool valid();
	void next();
	void first();
};
