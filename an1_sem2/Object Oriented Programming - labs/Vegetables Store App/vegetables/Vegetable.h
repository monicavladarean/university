#pragma once
#include<vector>
#include<string.h>
#include<iostream>

class Vegetable
{
private:
	std::string name;
	std::string family;
	std::string parts;
public:
	Vegetable(std::string fam,std::string name,std::string parts);
	std::string get_fam();
	std::string get_name();
	std::string get_parts();
	~Vegetable();
};

