/********************************************************************************
** Form generated from reading UI file 'vegetables.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_VEGETABLES_H
#define UI_VEGETABLES_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_vegetablesClass
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout_2;
    QGridLayout *gridLayout;
    QListWidget *searched_vegetables;
    QListWidget *repo_families;
    QListWidget *repo_vegetables_from_family;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLineEdit *vegetable_name;
    QPushButton *Search;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *vegetablesClass)
    {
        if (vegetablesClass->objectName().isEmpty())
            vegetablesClass->setObjectName(QString::fromUtf8("vegetablesClass"));
        vegetablesClass->resize(726, 387);
        centralWidget = new QWidget(vegetablesClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayout_2 = new QVBoxLayout(centralWidget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        searched_vegetables = new QListWidget(centralWidget);
        searched_vegetables->setObjectName(QString::fromUtf8("searched_vegetables"));

        gridLayout->addWidget(searched_vegetables, 2, 0, 1, 1);

        repo_families = new QListWidget(centralWidget);
        repo_families->setObjectName(QString::fromUtf8("repo_families"));

        gridLayout->addWidget(repo_families, 0, 0, 1, 1);

        repo_vegetables_from_family = new QListWidget(centralWidget);
        repo_vegetables_from_family->setObjectName(QString::fromUtf8("repo_vegetables_from_family"));

        gridLayout->addWidget(repo_vegetables_from_family, 0, 1, 1, 1);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        vegetable_name = new QLineEdit(centralWidget);
        vegetable_name->setObjectName(QString::fromUtf8("vegetable_name"));

        horizontalLayout->addWidget(vegetable_name);


        verticalLayout->addLayout(horizontalLayout);

        Search = new QPushButton(centralWidget);
        Search->setObjectName(QString::fromUtf8("Search"));

        verticalLayout->addWidget(Search);


        gridLayout->addLayout(verticalLayout, 2, 1, 1, 1);


        verticalLayout_2->addLayout(gridLayout);

        vegetablesClass->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(vegetablesClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 726, 26));
        vegetablesClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(vegetablesClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        vegetablesClass->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(vegetablesClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        vegetablesClass->setStatusBar(statusBar);

        retranslateUi(vegetablesClass);

        QMetaObject::connectSlotsByName(vegetablesClass);
    } // setupUi

    void retranslateUi(QMainWindow *vegetablesClass)
    {
        vegetablesClass->setWindowTitle(QApplication::translate("vegetablesClass", "vegetables", nullptr));
        label->setText(QApplication::translate("vegetablesClass", "Name", nullptr));
        Search->setText(QApplication::translate("vegetablesClass", "Search", nullptr));
    } // retranslateUi

};

namespace Ui {
    class vegetablesClass: public Ui_vegetablesClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_VEGETABLES_H
