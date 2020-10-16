#pragma once
#include "Repo.h"
#include <memory>
#include "UndoAction.h"

class Controller
{
private:
	Repo& repo;
	std::vector<UndoAction*> undo_actions;
	std::vector<UndoAction*> redo_actions;
public:
	Controller(Repo& repo);
	~Controller();

	void undo();
	void redo();

	void add_horse(const std::string breed, const std::string name, const std::string link, int age);
	//adds a horse to the repo

	int get_size();
	//returns the size of the repo
	int adoptions();
	TElem get_element(int i);
	Horse get_adoption(int i);
	//returns the horse situated at the position i in the list

	void delete_horse(int i);
	//deletes the horse situated at the position i in the list

	void update_age(int i, int elem);
	//updates the horse's age situated at the position i in the list

	void update_breed(int i, std::string elem);
	//updates the horse's breed situated at the position i in the list

	void update_link(int i, std::string elem);
	//updates the horse's link situated at the position i in the list

	void update_name(int i, std::string name);
	//updates the horse's name situated at the position i in the list

	void update(int i, std::string name, std::string breed, std::string link, int age);

	std::vector<Horse> sort();
	std::vector<Horse> shuffle();

	void add_adoption(int pos);

	Repo& get_repo();

};

