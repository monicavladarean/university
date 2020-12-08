#include "SortedBag.h"
#include "SortedBagIterator.h"

SortedBag::~SortedBag()
{
	delete[] this->elems;
	delete[] this->indexes;
}

SortedBag::SortedBag(Relation r)
{
	this->capacity = 20;
	this->elems = new TComp[capacity];
	this->indexes = new int[capacity];
	for (int i = 0; i < this->capacity - 1; i++)
		this->indexes[i] = i + 1;
	this->indexes[this->capacity - 1] = -1;
	this->head = -1;
	this->rel = r;
	this->firstEmpty = 0;
}

void SortedBag::add(TComp e)
{
	if (this->size()== this->capacity)
	{
		//double the capacity,copy the elems and new init for the indexes
		int cap = this->capacity;
		this->capacity = this->capacity * 2;
		TComp* el = new TComp[this->capacity]; 
		for (int i = 0; i < this->size(); i++)
			el[i] = this->elems[i];
		delete[] this->elems;
		this->elems = el;
		int* ele = new int[this->capacity]; 
		for (int i = 0; i < this->size(); i++)
			ele[i] = this->indexes[i];
		delete[] this->indexes;
		this->indexes = ele;
		for (int i = cap; i < this->capacity-1; i++)
			this->indexes[i] = i + 1;
		this->indexes[this->capacity - 1] = -1;
		this->firstEmpty = cap;
	}
	if (this->isEmpty())
	{
		//if the list is empty initialise the head =>teta(1)
		this->head = this->firstEmpty;
		this->elems[this->head] = e;
		this->firstEmpty = this->indexes[this->firstEmpty];
		this->indexes[this->head] = -1;
	}
	else 
	{
		if (this->rel(e, this->elems[this->head]))
		{
			this->elems[firstEmpty] = e;
			int next_empty = this->indexes[firstEmpty];
			this->indexes[firstEmpty] = this->head;
			this->head = this->firstEmpty;
			this->firstEmpty = next_empty;
		}
		else {
			int current = this->head,prev=0;
			while (this->indexes[current] != -1 && this->rel(this->elems[current], e))
			{
				prev = current;
				current = this->indexes[current];
			}
			if (this->rel(this->elems[current], e))
			{
			this->elems[this->firstEmpty] = e;
			int ind = this->indexes[current];
			this->indexes[current] = this->firstEmpty;
			int next_emp = this->indexes[this->firstEmpty];
			this->indexes[this->firstEmpty] = ind;
			this->firstEmpty = next_emp;
			}
			//teta(1) checks if the el is in rel with current => adds it before the end
			else
			{
				this->elems[this->firstEmpty] = e;
				this->indexes[prev] = this->firstEmpty;
				int next_empty = this->indexes[this->firstEmpty];
				this->indexes[this->firstEmpty] = current;
				this->firstEmpty = next_empty;
			}
		}

	}

}

bool SortedBag::remove(TComp e)
{
	if (not(this->search(e)))
		return false;
	int i = 0;
	int current = this->head;
	int prev = 0;
	while (this->indexes[current] != -1 && this->elems[current] != e)
	{
		prev = current;
		current = this->indexes[current];
	}
	if (this->indexes[current] != -1)
	{
		if (current == this->head)
		{
			int l = this->firstEmpty;
			int ind = this->indexes[current];
			this->firstEmpty = this->head;
			this->indexes[this->firstEmpty] = l;
			this->head = ind;
			return true;
		}
		else
		{
			this->indexes[prev] = this->indexes[current];
			int le = this->firstEmpty;
			this->firstEmpty = current;
			this->indexes[this->firstEmpty] = le;
			return true;
		}

	}
	else
	{
		if (this->size() == 1)
		{
			for (int i = 0; i < this->capacity - 1; i++)
				this->indexes[i] = i + 1;
			this->indexes[this->capacity - 1] = -1;
			this->head = -1;
			this->firstEmpty = 0;
			return true;
		}
		else
		{
			this->indexes[prev] = this->indexes[current];
			int le = this->firstEmpty;
			this->firstEmpty = current;
			this->indexes[this->firstEmpty] = le;
			return true;
		}
	}
	return false;
}

bool SortedBag::search(TComp e) const
{
	if (this->isEmpty())
		return false;
	//if e is in relation with the first elem ,then return false
	if (this->rel(e, this->elems[this->head]) && this->elems[this->head] != e)
		return false;
	//check if it is the first one
	if (this->elems[this->head] == e)
		return true;
	//we search for it
	int current = this->head;
	while (this->indexes[current] != -1 && this->elems[current] != e)
		current = this->indexes[current];
	//see if we found it and return t or f
	if (this->indexes[current] != -1 || this->indexes[current] == -1 && this->elems[current] == e)
		return true;
	else
		return false;
}
int SortedBag::nrOccurrences(TComp e) const
{
	if (this->head == -1)
		return 0;
	int nr = 0;
	int current = this->head;
	while(this->indexes[current] != -1)
	{
		if (this->elems[current] == e)
			nr++;
		current = this->indexes[current];
	}
	if (this->elems[current] == e)
		nr++;
	return nr;
}

int SortedBag::size() const
{
	if (this->head == -1)
		return 0;
	int current = this->head;
	int i = 0;
	while (this->indexes[current] != -1)
	{
		i++;
		current = this->indexes[current];
	}
	return i + 1;
}

SortedBagIterator SortedBag::iterator() 
{
	return SortedBagIterator(*this);
}

bool SortedBag::isEmpty() const
{
	if (this->head ==-1)
		return true;
	return false;
}


void SortedBag::tostr()
{
	cout << "The head is: " << this->head << "\n";
	cout << "First Empty is:" << this->firstEmpty << "\n";
	cout << "Size is: " << this->size() << "\n";
	int current = this->head;
	if (this->head == -1)
		cout << "None\n";
	else {
		cout << "The array:\n";
		while (this->indexes[current] != -1)
		{
			cout << this->elems[current] << ", ";
			current = this->indexes[current];
		}
		cout << this->elems[current] << "\n";
		for (int i = 0; i < this->capacity; i++)
			cout << this->elems[i] << " ";
		cout << "\n";
		cout << "The indexes:\n";
		for (int i = 0; i < this->capacity; i++)
			cout << this->indexes[i] << " ";
		cout << "\n";
	}

}

int SortedBag::toSet()
{
	if (this->head == -1)
		return 0;
	int current = this->head;
	int nr= 0;
	while (this->indexes[current] != -1)
	{
		if (this->nrOccurrences(this->elems[current]) > 1)
		{
			this->remove(this->elems[current]);
			nr++;
		}
		current = this->indexes[current];
	}
	return nr;

}
