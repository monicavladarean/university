#include "Moni_shelter.h"
#include <fstream>
Moni_shelter::Moni_shelter(Controller controller, QWidget *parent)
	: controller{ controller }, QMainWindow(parent)
{
	//this->initialize_repo();
	ui.setupUi(this);
	this->initialize_gui();
	this->load_repo_list();
	QObject::connect(this->sort_button, &QRadioButton::clicked, this, &Moni_shelter::sort);
	QObject::connect(this->shuffle_button, &QRadioButton::clicked, this, &Moni_shelter::shuffle);

	QObject::connect(this->add, &QPushButton::clicked, this, &Moni_shelter::add1);
	QObject::connect(this->remove, &QPushButton::clicked, this, &Moni_shelter::remove1);
	QObject::connect(this->update, &QPushButton::clicked, this, &Moni_shelter::update1);

	QObject::connect(this->undo, &QPushButton::clicked, this, &Moni_shelter::undo1);

	QObject::connect(this->redo, &QPushButton::clicked, this, &Moni_shelter::redo1);

}

void Moni_shelter::initialize_repo()
{
	std::ifstream fin("TextFile2.txt");
	std::string name, breed, link;
	int age;
	while (fin >> name >> breed >> link >> age)
		this->controller.add_horse(name, breed, link, age);
}

void Moni_shelter::load_repo_list()
{
	for (int i = 0; i < this->controller.get_size(); i++)
	{
		Horse aux = this->controller.get_element(i);
		QString string = QString::fromStdString(aux.get_name()) + " , " + QString::fromStdString(aux.get_breed()) + " , " + QString::number(aux.get_age()) + " , " + QString::fromStdString(aux.get_link());
		this->list->addItem(string);
	}
}

void Moni_shelter::sort()
{
	this->list->clear();
	std::vector<Horse> horses = this->controller.sort();
	for (int i = 0; i < horses.size(); i++)
	{
		Horse aux = horses.at(i);
		QString string = QString::fromStdString(aux.get_name()) + " , " + QString::fromStdString(aux.get_breed()) + " , " + QString::number(aux.get_age()) + " , " + QString::fromStdString(aux.get_link());
		this->list->addItem(string);
	}
	
}

void Moni_shelter::shuffle()
{
	this->list->clear();
	std::vector<Horse> horses = this->controller.shuffle();
	for (int i = 0; i < horses.size(); i++)
	{
		Horse aux = horses.at(i);
		QString string = QString::fromStdString(aux.get_name()) + " , " + QString::fromStdString(aux.get_breed()) + " , " + QString::number(aux.get_age()) + " , " + QString::fromStdString(aux.get_link());
		this->list->addItem(string);
	}

}

void Moni_shelter::add1()
{
	QString string1 = this->name_text->text();
	std::string name=string1.toStdString();
	QString string2 = this->age_text->text();
	std::string age = string2.toStdString();
	int age0 = std::stoi(age);
	QString string3 = this->link_text->text();
	std::string link = string3.toStdString();
	QString string4 = this->breed_text->text();
	std::string breed = string4.toStdString();
	this->controller.add_horse(breed, name, link, age0);
	this->list->clear();
	this->load_repo_list();
}

void Moni_shelter::remove1()
{
	QString string1 = this->name_text->text();
	std::string name = string1.toStdString();
	for(int i=0;i<controller.get_size();i++)
		if(this->controller.get_element(i).get_name()==name)
			this->controller.delete_horse(i);
	this->list->clear();
	this->load_repo_list();
}

void Moni_shelter::update1()
{
	QString string1 = this->name_text->text();
	std::string name = string1.toStdString();
	QString string2 = this->age_text->text();
	std::string age = string2.toStdString();
	int age0 = std::stoi(age);
	QString string3 = this->link_text->text();
	std::string link = string3.toStdString();
	QString string4 = this->breed_text->text();
	std::string breed = string4.toStdString();
	for (int i = 0; i < controller.get_size(); i++)
		if (this->controller.get_element(i).get_name() == name)
		{
			this->controller.update(i,name, breed, link, age0);
		}
	this->list->clear();
	this->load_repo_list();
}

void Moni_shelter::undo1()
{
	this->controller.undo();
	this->list->clear();
	this->load_repo_list();
}

void Moni_shelter::redo1()
{
	this->controller.redo();
	this->list->clear();
	this->load_repo_list();
}

void Moni_shelter::initialize_gui()
{
	QWidget* window = new QWidget();
	setCentralWidget(window);
	QHBoxLayout* big_layout = new QHBoxLayout();
	list = new QListWidget();
	window->setLayout(big_layout);
	big_layout->addWidget(list);

	QWidget* window_right_layout = new QWidget();
	QVBoxLayout * right_layout = new QVBoxLayout();
	window_right_layout->setLayout(right_layout);

	QWidget* name_window = new QWidget();
	QHBoxLayout * name_layout = new QHBoxLayout();
	name_window->setLayout(name_layout);

	right_layout->addWidget(name_window);

	QLabel* name_label = new QLabel("Name: ");
	this->name_text = new QLineEdit();
	name_layout->addWidget(name_label);
	name_layout->addWidget(name_text);

	QWidget* breed_window = new QWidget();
	QHBoxLayout * breed_layout = new QHBoxLayout();
	breed_window->setLayout(breed_layout);

	right_layout->addWidget(breed_window);

	QLabel* breed_label = new QLabel("Breed: ");
	this->breed_text = new QLineEdit();
	breed_layout->addWidget(breed_label);
	breed_layout->addWidget(breed_text);

	QWidget* age_window = new QWidget();
	QHBoxLayout * age_layout = new QHBoxLayout();
	age_window->setLayout(age_layout);

	right_layout->addWidget(age_window);

	QLabel* age_label = new QLabel("Age: ");
	this->age_text = new QLineEdit();
	age_layout->addWidget(age_label);
	age_layout->addWidget(age_text);

	QWidget* link_window = new QWidget();
	QHBoxLayout * link_layout = new QHBoxLayout();
	link_window->setLayout(link_layout);

	right_layout->addWidget(link_window);

	QLabel* link_label = new QLabel("Link: ");
	this->link_text = new QLineEdit();
	link_layout->addWidget(link_label);
	link_layout->addWidget(link_text);

	add = new QPushButton("Add");
	right_layout->addWidget(add);

	remove = new QPushButton("Remove");
	right_layout->addWidget(remove);

	update = new QPushButton("Update");
	right_layout->addWidget(update);

	undo = new QPushButton("Undo");
	right_layout->addWidget(undo);

	redo = new QPushButton("Redo");
	right_layout->addWidget(redo);

	shuffle_button = new QRadioButton("Shuffle");
	right_layout->addWidget(shuffle_button);

	sort_button = new QRadioButton("Sort");
	right_layout->addWidget(sort_button);

	big_layout->addWidget(window_right_layout);
}
