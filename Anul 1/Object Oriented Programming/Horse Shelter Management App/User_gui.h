#pragma once
#include "Controller.h"
#include "View.h"
#include <QWidget>
#include "ui_User_gui.h"

class User_gui : public QWidget
{
	Q_OBJECT

public:
	User_gui(Controller controller, QWidget *parent = Q_NULLPTR);
	~User_gui();
	void initialize_repo();
	void load_repo_list();
	void adopt();
	void open_lista();
private:
	Ui::User_gui ui;
	Controller controller;
};
