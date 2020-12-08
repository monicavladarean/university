#pragma once
#include"Repo.h"

class Controller
{
private:
	Repo& repo;
public:
	Controller(Repo& repo);
	std::vector<Vegetable> get_repo();
	std::vector<Vegetable> get_sort();
	std::vector<Vegetable> get_families(std::string fam);
	Vegetable get_parts_of_veg(std::string name);
	~Controller();
};

