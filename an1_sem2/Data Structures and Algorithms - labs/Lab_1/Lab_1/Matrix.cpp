#include "Matrix.h"


Matrix::Matrix(int nrLines, int nrCols) :
	lines{ nrLines }, columns{ nrCols }, elements{}, row_nr{}, column_nr{}
{
}

int Matrix::nrLines() const
{
	return this->lines;
}

int Matrix::nrColumns() const
{
	return this->columns;
}

int Matrix::element(int i, int j)
{
	if (i >= this->nrLines() || j >= this->nrColumns())
		throw std::exception();
	if (i<0 || j <0)
		throw std::exception();
	for (int k = 0; k < this->elements.getSize(); k++)
		if (this->column_nr.get_elem(k) == j && this->row_nr.get_elem(k) == i)
			return this->elements.get_elem(k);
	return 0;
}

int Matrix::modify(int i, int j, int e)
{
	if (i >= this->nrLines() || j >= this->nrColumns())
		throw std::exception();
	if (i < 0 || j < 0)
		throw std::exception();
	int aux = this->element(i, j);
	if (aux == 0)
	{
		this->elements.add(e);
		this->row_nr.add(i);
		this->column_nr.add(j);
	}
	else
		for(int k=0;k<this->elements.getSize();k++)
			if (i==this->row_nr.get_elem(k) && j==this->column_nr.get_elem(k))
			{
				this->elements.delete_elem(k);
				this->elements.add(e);
			}
	return aux;
}

void Matrix::resize(int newLines, int newCol)
{
	if (newLines <= 0 || newCol <= 0)
		throw std::exception();
	if (newLines > this->lines || newCol > this->columns)
	{
		for (int i = this->lines; i < this->elements.getSize(); i++)
			for (int j = this->columns; j < this->elements.getSize(); j++)
		{
			this->elements.add(0);
			this->column_nr.add(j);
			this->row_nr.add(i);
		}
	}

	else
	{
		for (int i = 0; i < this->elements.getSize(); i++)
		{
			if (this->column_nr.get_elem(i) > newCol || this->row_nr.get_elem(i) > newLines)
			{
				this->elements.delete_elem(i);
				this->column_nr.delete_elem(i);
				this->row_nr.delete_elem(i);
			}
		}
	}
	this->lines = newLines;
	this->columns = newCol;
}
