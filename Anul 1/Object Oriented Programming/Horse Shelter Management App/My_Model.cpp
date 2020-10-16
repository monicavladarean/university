#include "My_Model.h"


My_Model::My_Model(Repo& repo):
	repo{repo}
{
}


My_Model::~My_Model()
{
}

int My_Model::rowCount(const QModelIndex & parent) const
{
	return this->repo.get_adoption_size();
}

int My_Model::columnCount(const QModelIndex & parent) const
{
	return 4;
}

QVariant My_Model::data(const QModelIndex & index, int role) const
{
	int row = index.row();
	int col = index.column();

	Horse horse = this->repo.get_adoption(row);

	if (role == Qt::DisplayRole)
	{
		switch (col)
		{
		case 0:
			return QString::fromStdString(horse.get_name());
		case 1:
			return QString::fromStdString(horse.get_breed());
		case 2:
			return QString::fromStdString(std::to_string(horse.get_age()));
		case 3:
			return QString::fromStdString(horse.get_link());
		default:
			break;
		}
	}
	return QVariant();
}

QVariant My_Model::headerData(int section, Qt::Orientation orientation, int role) const
{
	if (role == Qt::DisplayRole && orientation == Qt::Horizontal)
	{
		switch (section)
		{
		case 0:
			return "Name";
		case 1:
			return "Breed";
		case 2:
			return "Age";
		case 3:
			return "Link";
		default:
			break;
		}
	}

	return QVariant();
}
