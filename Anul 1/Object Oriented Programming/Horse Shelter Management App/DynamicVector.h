#pragma once
#include "Horse.h"

typedef Horse TElem;
template <typename TElem>

class DynamicVector
{
private:
	int size, capacity;
	TElem* elems;

public:
	DynamicVector(int cap = 100);
	DynamicVector(const DynamicVector<TElem> & v);
	~DynamicVector();

	void add(const TElem& e);
	//adds an element to the dynamic vector

	int getSize();
	//returns the nr of elements from the dynamic vector

	TElem get_elem(int i);
	//returns the element from the position i from the dynamic vector

	void resize();
	//doubles the capacity of the dynamic vector, if it's full and we need to add more elements to it

	void delete_elem(int i);
	//deletes the element from the position i from the dynamic vector

	/*DynamicVector operator+(TElem e);
	friend DynamicVector operator+(TElem e, DynamicVector &v);
	DynamicVector operator=(DynamicVector v);
	*/

	/*DynamicVector operator+(TElem e, DynamicVector &v)
	{
		v.add(e);
		return DynamicVector();
	}*/

};
template <typename TElem>
DynamicVector<TElem>::DynamicVector(int cap)
{
	this->size = 0;
	this->capacity = cap;

	this->elems = new TElem[this->capacity];
}
template <typename TElem>
DynamicVector<TElem>::DynamicVector(const DynamicVector<TElem> & v)
{
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new TElem[this->capacity];

	for (int i = 0; i < v.size; i++)
		this->elems[i] = v.elems[i];
}
template <typename TElem>
int DynamicVector<TElem>::getSize() {
	return this->size;
}
template <typename TElem>
TElem DynamicVector<TElem>::get_elem(int i)
{
	return this->elems[i];
}
template <typename TElem>
void DynamicVector<TElem>::resize()
{
	this->capacity *= 2;
	TElem* aux;
	aux = new TElem[this->capacity];
	for (int i = 0; i < this->size; i++)
		aux[i] = this->elems[i];
	delete[]this->elems;
	this->elems = aux;
}
template <typename TElem>
void DynamicVector<TElem>::delete_elem(int i)
{
	for (int j = i + 1; j < this->size; j++)
		this->elems[j - 1] = this->elems[j];
	this->size--;
}

template <typename TElem>
DynamicVector<TElem>::~DynamicVector()
{
	delete[] this->elems;
}
template <typename TElem>
void DynamicVector<TElem>::add(const TElem & e)
{
	if (this->capacity == this->size)
		this->resize();
	this->elems[this->size++] = e;
}
