#include "MapIterator.h"
#include "Map.h"
#include <exception>

MapIterator::MapIterator(const Map & map):
	c{ map }, current{map.head}
{
	this->first();
}

void MapIterator::first()
{
	this->current = this->c.head;
}

void MapIterator::next()
{
	if (this->valid() == false)
		throw std::exception();
	this->current = this->current->get_next();
}

bool MapIterator::valid() const
{
	if (this->current == NULL)
		return false;
	return true;
}

TElem MapIterator::getCurrent() const
{
	if (this->valid() == false)
		throw std::exception();
	return this->current->get_info();
}

void MapIterator::jumpForward(int k)
{
	if (k <= 0)
		throw std::exception();
	if (this->valid() == false)
		throw std::exception();
	if (k > this->c.size())
	{
		this->current = NULL;
		return;
	}
	for (int i = 0; i < k; i ++)
	{
		if (this->valid() == false)
			return;
		this->current = this->current->get_next();
	}
}
