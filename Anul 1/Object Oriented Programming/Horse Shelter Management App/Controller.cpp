#include "Controller.h"
#include <algorithm>



Controller::Controller(Repo& repo) :
	repo{ repo }
{
}


Controller::~Controller()
{
}

void Controller::undo()
{
	this->undo_actions.at(this->undo_actions.size() - 1)->execute_undo();
	this->undo_actions.pop_back();
}

void Controller::redo()
{
	this->redo_actions.at(this->redo_actions.size() - 1)->execute_undo();
	this->redo_actions.pop_back();
}

void Controller::add_horse(const std::string breed, const std::string name, const std::string link, int age)
{
	Horse horse{ breed,name,link,age };
	Horse aux = horse;
	this->repo.add_horse(horse);

	UndoAction* p = new UndoAdd{ aux,this->repo };
	this->undo_actions.push_back(p);

	UndoAction* p1 = new UndoRemove{ aux,this->repo };
	this->redo_actions.push_back(p1);
}

int Controller::get_size()
{
	return this->repo.size();
}

int Controller::adoptions()
{
	return this->repo.adoptions_size();
}

TElem Controller::get_element(int i)
{
	return this->repo.get_element(i);
}

Horse Controller::get_adoption(int i)
{
	return this->repo.get_adoption(i);
}

void Controller::delete_horse(int i)
{
	Horse horse = this->repo.get_element(i);
	this->repo.delete_horse(i);

	UndoAction* p1 = new UndoRemove{ horse,this->repo };
	this->undo_actions.push_back(p1);

	UndoAction* p = new UndoAdd{ horse,this->repo };
	this->redo_actions.push_back(p);
}

void Controller::update_age(int i, int elem)
{
	this->repo.update_age(i, elem);
}

void Controller::update_breed(int i, std::string elem)
{
	this->repo.update_breed(i, elem);
}

void Controller::update_link(int i, std::string elem)
{
	this->repo.update_link(i, elem);
}

void Controller::update_name(int i, std::string name)
{
	this->repo.update_name(i, name);
}

void Controller::update(int i, std::string name, std::string breed, std::string link, int age)
{
	Horse horse = this->repo.get_element(i);

	this->update_age(i, age);
	this->update_name(i,name);
	this->update_link(i, link);
	this->update_breed(i, breed);

	Horse new_horse = this->repo.get_element(i);

	UndoAction* p1 = new UndoUpdate{new_horse,horse,this->repo };
	this->undo_actions.push_back(p1);

	UndoAction* p = new UndoUpdate{horse,new_horse,this->repo };
	this->redo_actions.push_back(p);

}

std::vector<Horse> Controller::sort()
{
	std::vector<Horse> horses=this->repo.get_all();
	for(int i=0;i<horses.size()-1;i++)
		for (int j = i+1; j < horses.size(); j++)
			if (horses.at(i).get_age() > horses.at(j).get_age())
			{
				std::swap(horses.at(i), horses.at(j));
			}
	return horses;
}

std::vector<Horse> Controller::shuffle()
{
	std::vector<Horse> horses = this->repo.get_all();
	std::random_shuffle(horses.begin(), horses.end());
	return horses;
}

void Controller::add_adoption(int pos)
{
	this->repo.add_adoption(pos);
}

Repo& Controller::get_repo() 
{
	return this->repo;
}
