#pragma once
#include "Moni_shelter.h"
#include "User_gui.h"
#include <QWidget>
#include "Controller.h"
#include "ui_Start.h"
#include "View.h"

class Start : public QWidget
{
	Q_OBJECT

public:
	Start(Controller controller,QWidget *parent = Q_NULLPTR);
	~Start();
	void administrator();
	void user();


private:
	Ui::Start ui;
	Controller controller;
};
