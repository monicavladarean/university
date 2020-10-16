#include "vegetables.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Repo repo{};
	Controller ctrl{ repo };
	vegetables w{ ctrl };
	w.show();
	return a.exec();
}
