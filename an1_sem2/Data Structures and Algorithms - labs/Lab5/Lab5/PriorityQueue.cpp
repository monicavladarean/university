#include "PriorityQueue.h"
#include <stdexcept>

void PriorityQueue::resize()
{
	std::pair<TElem, TPriority> *newElements = new std::pair<TElem, TPriority>[2 * this->capacity];
	for (int i = 0; i < this->capacity; i++)
	{
		newElements[i] = this->elements[i];
	}
	this->elements = newElements;
	this->capacity *= 2;
}

PriorityQueue::PriorityQueue(Relation r)
{
	this->relation = r;
	this->capacity = 5;
	this->elements = new std::pair<TElem, TPriority>[this->capacity];
}

void PriorityQueue::push(TElem e, TPriority p)
{
	if (this->size == this->capacity)
	{
		this->resize();
	}
	this->size++;
	this->elements[this->size - 1] = std::make_pair(e, p);
	this->bubbleUp(this->size - 1);
}

Element PriorityQueue::top() const
{
	if (this->isEmpty())
		throw std::runtime_error("Empty queue!");
	return this->elements[0];
}

void PriorityQueue::bubbleUp(int position)
{
	Element element = this->elements[position];
	int parent_position = (position - 1) / 3;
	while (position > 0 && !this->relation(this->elements[parent_position].second, element.second))
	{
		this->elements[position] = this->elements[parent_position];
		position = parent_position;
		parent_position = (position - 1) / 3;
	}
	this->elements[position] = element;
}

void PriorityQueue::bubbleDown(int position)
{
	Element elem = this->elements[position];
	while (position < this->size)
	{
		int max_child = this->getBiggestChildPos(position);
		if (max_child != -1 && this->relation(this->elements[max_child].second, elem.second))
		{
			Element aux = this->elements[position];
			this->elements[position] = this->elements[max_child];
			this->elements[max_child] = aux;
			position = max_child;

		}
		else
		{
			position = this->size + 1;
		}
	}

}

int PriorityQueue::getBiggestChildPos(int parentPosition)
{
	int child_array_size = this->size - (3 * parentPosition + 1);
	if (child_array_size > 3)
		child_array_size = 3;
	if (child_array_size <= 0)
		return -1;
	Element max = this->elements[parentPosition * 3 + 1];
	int max_position = parentPosition * 3 + 1;
	for (int i = 1; i < child_array_size; i++)
		if (this->relation(this->elements[parentPosition * 3 + 1 + i].second, max.second))
		{
			max = this->elements[parentPosition * 3 + 1 + i];
			max_position = parentPosition * 3 + 1 + i;
		}

	return max_position;

}

Element PriorityQueue::pop()
{
	if (this->isEmpty())
		throw std::runtime_error("Empty queue!");
	Element deleted = this->elements[0];
	this->elements[0] = this->elements[this->size - 1];
	this->size -= 1;
	this->bubbleDown(0);
	return deleted;

}

bool PriorityQueue::isEmpty() const
{
	return this->size == 0;
}

PriorityQueue::~PriorityQueue()
{
	delete[] this->elements;
}
