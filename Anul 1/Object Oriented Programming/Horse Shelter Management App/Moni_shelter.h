#pragma once
#include "Controller.h"
#include <QtWidgets/QMainWindow>
#include "ui_Moni_shelter.h"
#include <QWidget>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QString>
#include <QListWidget>
#include <QWidgetList>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QRadioButton>
#include <QKeyEvent>
class Moni_shelter : public QMainWindow
{
	Q_OBJECT

public:
	Moni_shelter(Controller controller, QWidget *parent = Q_NULLPTR);
	void initialize_gui();
	void initialize_repo();
	void load_repo_list();
	void sort();
	void shuffle();

	void add1();
	void remove1();
	void update1();

	void undo1();
	void redo1();

	void keyPressEvent(QKeyEvent *event) override
	{
		if (event->matches(QKeySequence::Undo))
		{
			this->undo1();
		}
		else if (event->matches(QKeySequence::Redo))
		{
			this->redo1();
		}
	}

private:
	Ui::Moni_shelterClass ui;
	Controller controller;
	QListWidget* list;
	QLineEdit* name_text;
	QLineEdit* breed_text;
	QLineEdit* age_text;
	QLineEdit* link_text;
	QPushButton* add;
	QPushButton* undo;
	QPushButton* redo;
	QPushButton* remove;
	QPushButton* update;
	QRadioButton* sort_button;
	QRadioButton* shuffle_button;
};
