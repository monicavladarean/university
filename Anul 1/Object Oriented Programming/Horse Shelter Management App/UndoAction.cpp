#include "UndoAction.h"

UndoAction::UndoAction()
{
}


UndoAction::~UndoAction()
{
}


UndoAdd::UndoAdd(Horse added_horse, Repo & repo):
	added_horse{ added_horse }, repo{ repo }
{
}

void UndoAdd::execute_undo()
{
	this->repo.delete_horse_2(this->added_horse);
}


UndoRemove::UndoRemove(Horse deleted_horse, Repo & repo):
	deleted_horse{deleted_horse},repo{repo}
{
}

void UndoRemove::execute_undo()
{
	this->repo.add_horse(this->deleted_horse);
}

UndoRemove::~UndoRemove()
{
}

UndoAdd::~UndoAdd()
{
}

UndoUpdate::UndoUpdate(Horse updated_horse, Horse first_horse,Repo & repo):
	updated_horse{ updated_horse }, repo{ repo },first_horse{first_horse}
{
}

void UndoUpdate::execute_undo()
{
	this->repo.delete_horse_2(this->updated_horse);
	this->repo.add_horse(this->first_horse);
}

UndoUpdate::~UndoUpdate()
{
}
