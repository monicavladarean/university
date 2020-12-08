#include "vegetables.h"

vegetables::vegetables(Controller ctrl,QWidget *parent)
	: ctrl{ ctrl },QMainWindow(parent)
{
	ui.setupUi(this);
	this->load_repo();
	QObject::connect(this->ui.repo_families,&QListWidget::itemClicked,this,&vegetables::load_vegetables);
	QObject::connect(this->ui.Search, &QPushButton::clicked, this, &vegetables::search);
}

void vegetables::load_repo()
{
	std::vector<Vegetable> aux = this->ctrl.get_sort();
	for (auto i : aux)
	{
		this->ui.repo_families->addItem(QString::fromStdString(i.get_fam()));
	}
}

void vegetables::load_vegetables()
{
	QString str=this->ui.repo_families->currentItem()->text();
	std::string fam = str.toStdString();
	std::vector<Vegetable> aux = this->ctrl.get_families(fam);
	this->ui.repo_vegetables_from_family->clear();
	for (auto i : aux)
	{
		this->ui.repo_vegetables_from_family->addItem(QString::fromStdString(i.get_name())+QString::fromStdString(",")+QString::fromStdString(i.get_parts()));
	}
}

void vegetables::search()
{
	QString str = this->ui.vegetable_name->text();
	std::string name = str.toStdString();
	this->ui.searched_vegetables->clear();
	this->ui.searched_vegetables->addItem(QString::fromStdString(this->ctrl.get_parts_of_veg(name).get_parts()));
}
