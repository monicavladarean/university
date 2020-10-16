#include "SortedBagIterator.h"
#include "SortedBag.h"

SortedBagIterator::SortedBagIterator(SortedBag& bag): bag{bag}
{
	this->current = bag.head;
}

TComp SortedBagIterator::getCurrent()
{
	if (not(this->valid()))
		throw std::invalid_argument("received negative value");
	return this->bag.elems[this->current];
}

bool SortedBagIterator::valid()
{
	if (this->bag.isEmpty())
		return false;
	if (this->current == -1)
		return false;
	if (this->bag.indexes[current] != -1)
		return true;
	else
	{
		return this->bag.search(this->bag.elems[this->current]);
	}

}

void SortedBagIterator::next()
{
	if (not(this->valid()))
		throw std::invalid_argument("received negative value");
	if (this->bag.indexes[this->current] == -1)
		this->current = -1;
	else
		this->current = this->bag.indexes[this->current];
}

void SortedBagIterator::first()
{
	this->current = this->bag.head;
}
