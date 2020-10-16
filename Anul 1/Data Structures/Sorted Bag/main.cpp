#include "SortedBag.h"
#include "SortedBagIterator.h"
#include "SHortTest.h"
#include "ExtendedTest.h"
#include <iostream>

using namespace std;

int main() 
{
	test_set();
	cout << "\n";
	testAll();
	cout << "Short test passed!\n";
	testAllExtended();
	cout << "Extended test passed!\n";

	return 0;

}
