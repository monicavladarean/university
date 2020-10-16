#pragma once
#include "DynamicVector.h"
#include<fstream>
#include <vector>
class Repo
{
private:
	std::vector<TElem> repo;
	std::vector<Horse> adoption_list;
public:
	Repo();
	~Repo();
	int adoptions_size();
	std::vector<Horse> get_all();

	void initialize();

	std::vector<Horse> get_adoptions() const;

	int get_adoption_size();

	Horse get_adoption(int i);
	int size() const;
	//returns the size of the horse's list

	void add_horse(const TElem element);
	//adds a horse to the list

	TElem get_element(int i);
	//returns the horse situated at the position i in the list

	void delete_horse(int i);
	void delete_horse_2(Horse horse);
	//deletes the horse situated at the position i in the list

	void update_age(int i, int elem);
	//updates the horse's age situated at the position i in the list

	void update_breed(int i, std::string elem);
	//updates the horse's breed situated at the position i in the list

	void update_link(int i, std::string elem);
	//updates the horse's link situated at the position i in the list

	void update_name(int i, std::string name);
	//updates the horse's name situated at the position i in the list

	void add_adoption(int pos);

};

