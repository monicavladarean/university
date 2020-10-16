#include "Horse.h"
#include <Windows.h>

Horse::Horse(const std::string breed, const std::string name, const std::string link, int age) :
	breed{ breed }, name{ name }, link{ link }, age{ age }
{
}

const std::string Horse::get_breed()
{
	return this->breed;
}

const std::string Horse::get_name()
{
	return this->name;
}

const std::string Horse::get_link()
{
	return this->link;
}

const int Horse::get_age()
{
	return this->age;
}

void Horse::set_breed(std::string& breed)
{
	this->breed = breed;
}

void Horse::set_name(std::string& name)
{
	this->name = name;
}

void Horse::set_link(std::string& link)
{
	this->link = link;
}

void Horse::set_age(int& age)
{
	this->age = age;
}

void Horse::photo_open()
{
	ShellExecuteA(NULL, NULL, "chrome.exe", this->link.c_str(), NULL, SW_SHOWMAXIMIZED);
}

Horse::Horse() :
	breed{ "" }, name{ "" }, link{ "" }, age{ 0 }
{
}


Horse::~Horse()
{
}
