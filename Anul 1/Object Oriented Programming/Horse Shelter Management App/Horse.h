#pragma once
#include <string>
class Horse
{
private:
	std::string breed;
	std::string name;
	std::string link;
	int age;

public:
	Horse(const std::string breed, const std::string name, const std::string link, int age);
	Horse();
	~Horse();

	const std::string get_breed();
	//returns the breed of the horse

	const std::string get_name();
	//returns the nane of the horse

	const std::string get_link();
	//returns the link of the horse

	const int get_age();
	//returns the age of the horse

	void set_breed(std::string& breed);
	//changes the breed of the horse

	void set_name(std::string& name);
	//changes the name of the horse

	void set_link(std::string& link);
	//changes the link of the horse

	void set_age(int& age);
	//changes the age of the horse

	void photo_open();
	//opens the link of the horse, in a browser
};

