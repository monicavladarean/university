#include"ExtendedTest.h"
#include"ShortTest.h"
#include"Matrix.h"
#include "assert.h"
int main()
{
	testAll();
	testAllExtended();

	Matrix m(2,2);
	for (int i = 0; i < m.nrLines(); i++)
		for (int j = 0; j < m.nrColumns(); j++)
			m.modify(i, j, 3);

	m.resize(1, 1);
	assert(m.nrColumns()==1);
	assert(m.nrLines() == 1);
	for (int i = 0; i < m.nrLines(); i++)
		for (int j = 0; j < m.nrColumns(); j++)
			assert(m.element(i, j) == 3);

	return 0;
}