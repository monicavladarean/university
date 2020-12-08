#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_vegetables.h"
#include "Controller.h"

class vegetables : public QMainWindow
{
	Q_OBJECT
private:
	Controller ctrl;
public:
	vegetables(Controller ctrl,QWidget *parent = Q_NULLPTR);
	void load_repo();
	void load_vegetables();
	void search();
private:
	Ui::vegetablesClass ui;
};
