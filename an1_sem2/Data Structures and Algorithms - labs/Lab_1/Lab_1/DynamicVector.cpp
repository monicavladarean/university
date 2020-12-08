#include "DynamicVector.h"

DynamicVector::DynamicVector(int cap)
{
	this->size = 0;
	this->capacity = cap;

	this->elems = new int[this->capacity];
}

DynamicVector::DynamicVector(const DynamicVector & v)
{
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new int[this->capacity];

	for (int i = 0; i < v.size; i++)
		this->elems[i] = v.elems[i];
}

int DynamicVector::getSize() {
	return this->size;
}

int DynamicVector::get_elem(int i)
{
	return this->elems[i];
}

void DynamicVector::resize()
{
	this->capacity *= 2;
	int* aux;
	aux = new int[this->capacity];
	for (int i = 0; i < this->size; i++)
		aux[i] = this->elems[i];
	delete[]this->elems;
	this->elems = aux;
}

void DynamicVector::delete_elem(int i)
{
	for (int j = i + 1; j < this->size; j++)
		this->elems[j - 1] = this->elems[j];
	this->size--;
}

DynamicVector::~DynamicVector()
{
	delete[] this->elems;
}

void DynamicVector::add(const int & e)
{
	if (this->capacity == this->size)
		this->resize();
	this->elems[this->size++] = e;
}

DynamicVector operator+(int e, DynamicVector &v)
{
	v.add(e);
	return DynamicVector();
}
