#include "Repo.h"

Repo::Repo()
{
	this->initialize();
}

Repo::~Repo()
{
}

int Repo::adoptions_size()
{
	return this->adoption_list.size();
}

std::vector<Horse> Repo::get_all()
{
	return this->repo;
}

void Repo::initialize()
{
	std::ifstream fin("TextFile2.txt");
	std::string name, breed, link;
	int age;
	while (fin >> name >> breed >> link >> age)
		this->repo.push_back(Horse{ name, breed, link, age });
}

std::vector<Horse> Repo::get_adoptions() const
{
	return this->adoption_list;
}

int Repo::get_adoption_size()
{
	return this->adoption_list.size();
}

Horse Repo::get_adoption(int i)
{
	return this->adoption_list.at(i);
}

int Repo::size() const
{
	return this->repo.size();
}

void Repo::add_horse(const TElem element)
{
	this->repo.push_back(element);
}

TElem  Repo::get_element(int i)
{
	return this->repo.at(i);
}

void Repo::delete_horse(int i)
{
	this->repo.erase(repo.begin() + i);
}

void Repo::delete_horse_2(Horse horse)
{
	int i;
	for (i=0;i<this->repo.size();i++)
	{
		if(this->repo.at(i).get_name()==horse.get_name())
			break;
	}
	this->delete_horse(i);
}

void Repo::update_age(int i, int name)
{
	TElem elem = repo.at(i);
	elem.set_age(name);
	this->repo.erase(repo.begin() + i);
	this->repo.push_back(elem);
}

void Repo::update_breed(int i, std::string name)
{
	TElem elem = repo.at(i);
	elem.set_breed(name);
	this->repo.erase(repo.begin() + i);
	this->repo.push_back(elem);
}

void Repo::update_link(int i, std::string name)
{
	TElem elem = repo.at(i);
	elem.set_link(name);
	this->repo.erase(repo.begin() + i);
	this->repo.push_back(elem);
}

void Repo::update_name(int i, std::string name)
{
	TElem elem = repo.at(i);
	elem.set_name(name);
	this->repo.erase(repo.begin() + i);
	this->repo.push_back(elem);
}

void Repo::add_adoption(int pos)
{
	this->adoption_list.push_back(this->repo.at(pos));
	this->delete_horse(pos);
}
