#include "BagIterator.h"

BagIterator::BagIterator(const Bag & c):
	c{c}
{
	this->first();
}

void BagIterator::first()
{
	for (int i = 0; i < c.buckets; i++) {
		if (c.table[i] != INT_MAX) {
			current = i;
			break;
		}
	}
}

void BagIterator::next()
{
	current++;
	if (valid() == false)
		throw (std::exception());
	while (c.table[current] == INT_MAX && current < c.buckets)
		current++;
}

bool BagIterator::valid() const
{
	if (c.isEmpty())
		return false;
	return current < c.buckets;
}

TElem BagIterator::getCurrent() const
{
	if (valid() == false)
		throw (std::exception());
	return c.table[current];
}
