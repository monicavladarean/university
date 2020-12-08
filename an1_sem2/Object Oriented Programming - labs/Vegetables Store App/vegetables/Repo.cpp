#include "Repo.h"
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

Repo::Repo()
{
	this->read_from_file();
}

void Repo::read_from_file()
{
	std::string name;
	std::string family;
	std::string parts;
	std::ifstream fin("TextFile1.txt");
	while (fin>>family>>name>>parts)
	{
		Vegetable veg{ family,name,parts };
		this->repo.push_back(veg);
	}
}

std::vector<Vegetable> Repo::get_all()
{
	return this->repo;
}

std::vector<Vegetable> Repo::get_sort()
{
	std::vector<Vegetable> aux = this->repo;
	for (int i = 0; i < aux.size() - 1; i++)
	{
		for (int j = i + 1; j < aux.size(); j++)
			if (aux.at(i).get_fam() > aux.at(j).get_fam())
				std::swap(aux.at(i), aux.at(j));
	}
	for (int i = 0; i < aux.size() - 1; i++)
	{
		for (int j = i + 1; j < aux.size(); j++)
			if (aux.at(i).get_fam() == aux.at(j).get_fam())
				aux.erase(aux.begin() + j);
	}
	return aux;
}

std::vector<Vegetable> Repo::get_families(std::string fam)
{
	std::vector<Vegetable> aux;
	for (int i = 0; i < this->repo.size() ; i++)
	{
		if (this->repo.at(i).get_fam().find(fam) == 0)
				aux.push_back(repo.at(i));
	}
	return aux;
}


Repo::~Repo()
{
}
