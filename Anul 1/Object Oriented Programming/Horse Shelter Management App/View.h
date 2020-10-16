#pragma once

#include <QWidget>
#include "ui_View.h"
#include "My_Model.h"

class View : public QWidget
{
	Q_OBJECT
private:
	My_Model* model;
public:
	View(My_Model* m,QWidget *parent = Q_NULLPTR);
	~View();

private:
	Ui::View ui;
};
