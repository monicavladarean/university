#pragma once

class DynamicVector
{
private:
	int size, capacity;
	int* elems;

public:
	DynamicVector(int cap = 100);
	DynamicVector(const DynamicVector& v);
	~DynamicVector();

	void add(const int& e);
	//adds an element to the dynamic vector

	int getSize();
	//returns the nr of elements from the dynamic vector

	int get_elem(int i);
	//returns the element from the position i from the dynamic vector

	void resize();
	//doubles the capacity of the dynamic vector, if it's full and we need to add more elements to it

	void delete_elem(int i);
	//deletes the element from the position i from the dynamic vector

};

