#include "View.h"

View::View(My_Model* m,QWidget *parent)
	:model{ m },QWidget(parent)
{
	ui.setupUi(this);
	this->ui.tableView->setModel(this->model);
	this->ui.tableView->resizeColumnsToContents();
}

View::~View()
{
}
