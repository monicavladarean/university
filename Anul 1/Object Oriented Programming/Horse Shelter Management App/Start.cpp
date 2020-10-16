#include "Start.h"

Start::Start(Controller controller,QWidget *parent)
	: controller{ controller }, QWidget(parent)
{
	ui.setupUi(this);
	QObject::connect(this->ui.admin, &QPushButton::clicked, this, &Start::administrator);
	QObject::connect(this->ui.user, &QPushButton::clicked, this, &Start::user);

}

Start::~Start()
{
}

void Start::administrator()
{
	Moni_shelter* w1=new Moni_shelter{ controller };
	w1->show();
	this->hide();
}

void Start::user()
{
	User_gui* w2 = new User_gui{ controller };
	w2->show();
	this->hide();
}


