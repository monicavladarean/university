
#include "Start.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	Repo repo{};
	Controller controller{ repo };
	QApplication a(argc, argv);
	//User_gui w{ controller };
	Start w{ controller };
	w.show();
	return a.exec();
}
