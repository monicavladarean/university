#pragma once
#include "Vegetable.h"

class Repo
{
private:
	std::vector<Vegetable> repo;
public:
	Repo();
	void read_from_file();
	std::vector<Vegetable> get_all();
	std::vector<Vegetable> get_sort();
	std::vector<Vegetable> get_families(std::string fam);
	~Repo();
};

