#pragma once
#include<QAbstractTableModel>
//#include<QTableView>
#include "Repo.h"

class My_Model : public QAbstractTableModel
{
	Q_OBJECT
private:
	Repo& repo;
public:
	My_Model(Repo& repo);
	~My_Model();

	int QAbstractItemModel::rowCount(const QModelIndex &parent = QModelIndex()) const override;
	int QAbstractItemModel::columnCount(const QModelIndex &parent = QModelIndex()) const override;
	QVariant QAbstractItemModel::data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
	QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;
};

