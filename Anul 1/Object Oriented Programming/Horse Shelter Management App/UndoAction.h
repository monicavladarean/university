#pragma once
#include "Horse.h"
#include "Repo.h"
class UndoAction
{
public:
	UndoAction();
	virtual void execute_undo() = 0;
	virtual ~UndoAction();
};



class UndoAdd : public UndoAction
{
private:
	Horse added_horse;
	Repo& repo;
public:
	UndoAdd(Horse added_horse, Repo& repo);
	void execute_undo() override;
	~UndoAdd();
};


class UndoRemove : public UndoAction
{
private:
	Horse deleted_horse;
	Repo& repo;
public:
	UndoRemove(Horse deleted_horse, Repo& repo);
	void execute_undo() override;
	~UndoRemove();
};

class UndoUpdate : public UndoAction
{
private:
	Horse updated_horse;
	Horse first_horse;
	Repo& repo;
public:
	UndoUpdate(Horse updated_horse, Horse first_horse, Repo& repo);
	void execute_undo() override;
	~UndoUpdate();
};
