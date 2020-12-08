#include "Controller.h"



Controller::Controller(Repo& repo):
	repo{repo}
{
}

std::vector<Vegetable> Controller::get_repo()
{
	return this->repo.get_all();
}

std::vector<Vegetable> Controller::get_sort()
{
	return this->repo.get_sort();
}

std::vector<Vegetable> Controller::get_families(std::string fam)
{
	return this->repo.get_families(fam);
}

Vegetable Controller::get_parts_of_veg(std::string name)
{
	for (auto i : this->repo.get_all())
	{
		if (i.get_name().find(name) == 0)
			return i;
	}
}


Controller::~Controller()
{
}
