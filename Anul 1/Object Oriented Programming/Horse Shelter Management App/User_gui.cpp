#include "User_gui.h"
#include <fstream>
User_gui::User_gui(Controller controller, QWidget *parent)
	: controller{ controller }, QWidget(parent)
{
	//this->initialize_repo();
	ui.setupUi(this);
	this->load_repo_list();
	QObject::connect(this->ui.Adopt, &QPushButton::clicked, this, &User_gui::adopt);
	QObject::connect(this->ui.open_list, &QPushButton::clicked, this, &User_gui::open_lista);
}

void User_gui::open_lista()
{
	My_Model* model = new My_Model{ this->controller.get_repo()};
	View* p=new View{ model };
	p->show();
}


void User_gui::initialize_repo()
{
	std::ifstream fin("TextFile2.txt");
	std::string name, breed, link;
	int age;
	while (fin >> name >> breed >> link >> age)
		this->controller.add_horse(name, breed, link, age);
}

void User_gui::load_repo_list()
{
	for (int i = 0; i < this->controller.get_size(); i++)
	{
		Horse aux = this->controller.get_element(i);
		QString string = QString::fromStdString(aux.get_name()) + " , " + QString::fromStdString(aux.get_breed()) + " , " + QString::number(aux.get_age()) + " , " + QString::fromStdString(aux.get_link());
		this->ui.horses->addItem(string);
	}
}

void User_gui::adopt()
{
	int pos = this->ui.horses->currentRow();
	this->controller.add_adoption(pos);
	this->ui.adopted_horses->clear();
	for (int i = 0; i < this->controller.adoptions(); i++)
	{
		Horse aux = this->controller.get_adoption(i);
		QString string = QString::fromStdString(aux.get_name()) + " , " + QString::fromStdString(aux.get_breed()) + " , " + QString::number(aux.get_age()) + " , " + QString::fromStdString(aux.get_link());
		this->ui.adopted_horses->addItem(string);
	}
	this->ui.horses->clear();
	this->load_repo_list();
}

User_gui::~User_gui()
{
}
