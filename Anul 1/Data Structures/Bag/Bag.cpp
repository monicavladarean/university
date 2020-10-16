#include "Bag.h"
#include "BagIterator.h"

Bag::~Bag()
{

}

void Bag::resize()
{
	auto *old_table = table;
	int old_size = buckets;
	buckets *= 2;
	firstFree = 0;
	auto *new_table = new TElem[buckets];
	auto *new_next = new int[buckets];

	table = new_table;
	delete[] next;
	next = new_next;

	for (int i = 0; i < buckets; i++) 
	{
		table[i] = INT_MAX;
		next[i] = INT_MAX;
	}

	for (int i = 0; i < old_size; i++) 
	{
		if (old_table[i] != INT_MAX) 
		{
			int pos = hash(old_table[i]);
			if (table[pos] == INT_MAX)
			{
				table[pos] = old_table[i];
				next[pos] = INT_MAX;
				if (firstFree == pos)
					findFirstFree();
			}
			else 
			{
				int current = pos;
				while (next[current] != INT_MAX)
					current = next[current];
				table[firstFree] = old_table[i];
				next[firstFree] = INT_MAX;
				next[current] = firstFree;
				findFirstFree();
			}
		}
	}

	delete[] old_table;
}

void Bag::findFirstFree()
{
	for (int i = 0; i < buckets; i++) 
	{
		if (table[i] == INT_MAX) 
		{
			firstFree = i;
			break;
		}
	}
}

Bag::Bag()
{
	buckets = 1000000;
	firstFree = 0;
	length = 0;
	this->table = new TElem[buckets];
	this->next = new int[buckets];

	for (int i = 0; i < buckets; i++) 
	{
		table[i] = INT_MAX;
		next[i] = INT_MAX;
	}
}

void Bag::add(TElem e)
{
	if (firstFree == buckets) 
	{
		resize();
	}

	int pos = hash(e);
	if (table[pos] == INT_MAX) 
	{
		table[pos] = e;
		next[pos] = INT_MAX;
		if (firstFree == pos)
			findFirstFree();
	}
	else 
	{
		int current = pos;
		while (next[current] != INT_MAX)
			current = next[current];
		table[firstFree] = e;
		next[firstFree] = INT_MAX;
		next[current] = firstFree;
		findFirstFree();
	}
	length++;
}

bool Bag::remove(TElem e)
{
	int pos = hash(e);
	int prev = INT_MAX;
	do 
	{
		if (table[pos] == e)
		{
			table[pos] = INT_MAX;
			if (prev != INT_MAX)
				next[prev] = next[pos];
			length--;
			findFirstFree();
			return true;
		}
		prev = pos;
		pos = next[pos];
	} while (pos != INT_MAX);
	return false;
}

bool Bag::search(TElem e) const
{
	int pos = hash(e);
	do 
	{
		if (table[pos] == e)
			return true;
		pos = next[pos];
	} while (pos != INT_MAX);
	return false;
}

int Bag::nrOccurrences(TElem e) const
{
	int s = 0;
	int pos = hash(e);
	do
	{
		if (table[pos] == e)
			s++;
		pos = next[pos];
	} while (pos != INT_MAX);
	return s;
}

int Bag::size() const
{
	return length;
}

BagIterator Bag::iterator() const
{
	return BagIterator(*this);
}

bool Bag::isEmpty() const
{
	return length==0;
}
