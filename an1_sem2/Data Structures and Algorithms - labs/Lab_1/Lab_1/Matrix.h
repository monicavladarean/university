#pragma once
#include"DynamicVector.h"
#include<exception>
typedef int TElem;

#define NULL_TELEM 0

class Matrix {

private:

	/*representation of the matrix*/
	int columns;
	int lines;
	DynamicVector elements;
	DynamicVector row_nr;
	DynamicVector column_nr;

public:

	//constructor

	//throws exception if nrLines or nrCols is negative or zero

	Matrix(int nrLines, int nrCols);


	//returns the number of lines

	int nrLines() const;



	//returns the number of columns

	int nrColumns() const;



	//returns the element from line i and column j (indexing starts from 0)

	//throws exception if (i,j) is not a valid position in the Matrix

	int element(int i, int j);



	//modifies the value from line i and column j

	//returns the previous value from the position

	//throws exception if (i,j) is not a valid position in the Matrix

	int modify(int i, int j, int e);

	void resize(int newLines, int newCol);


};

