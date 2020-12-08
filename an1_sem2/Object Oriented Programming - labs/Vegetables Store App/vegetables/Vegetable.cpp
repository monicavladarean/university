#include "Vegetable.h"



Vegetable::Vegetable(std::string fam, std::string name, std::string parts) :name{ name }, family{ fam }, parts{parts}
{
}

std::string Vegetable::get_fam()
{
	return this->family;
}

std::string Vegetable::get_name()
{
	return this->name;
}

std::string Vegetable::get_parts()
{
	return this->parts;
}


Vegetable::~Vegetable()
{
}
