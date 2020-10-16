#include "ExtendedTest.h"
#include "ShortTest.h"
#include <iostream>

int main()
{
	testAll();

	std::cout << "Short test passed!\n";

	testAllExtended();

	std::cout << "Extended test passed!\n";

	return 0;
}