#include "Map.h"
#include "MapIterator.h"
#include<iostream>
using namespace std;


DLLNode::DLLNode(TElem info)
{
	this->next = NULL;
	this->prev = NULL;
	this->info = info;
}

DLLNode::DLLNode()
{
	this->info.first = -1000;
	this->info.second = -1000;
	this->prev = NULL;
	this->next = NULL;
}

void DLLNode::toStr()
{
	std::cout << "elem:" <<"("<< this->info.first << this->info.second<<")" << "\n";
}

TElem DLLNode::get_info() { return this->info; }
DLLNode* DLLNode::get_next() { return this->next; }
DLLNode* DLLNode::get_prev() { return this->prev; };
void DLLNode::set_info(TElem i) { this->info = i; }
void DLLNode::set_next(DLLNode* next) { this->next = next; }
void DLLNode::set_prev(DLLNode* prev) { this->prev = prev; }

DLLNode& DLLNode::operator=(const DLLNode& node)
{
	//first verify if the node = this
	if (this == &node)
		return *this;
	//we copy the params
	this->info = node.info;
	//we return the new node
	return *this;

}

DLLNode::~DLLNode() {
}


Map::Map()
{
	this->head = NULL;
	this->tail= NULL;
	/*DLLNode* elNew = new DLLNode;
	elNew->set_next(NULL);
	elNew->set_prev(NULL);
	this->head = elNew;
	DLLNode* elNew2 = new DLLNode;
	elNew2->set_next(NULL);
	elNew2->set_prev(NULL);
	this->tail = elNew2;*/
}

TValue Map::add(TKey c, TValue v)
{
	
	if (this->isEmpty())
	{
		TElem x= std::make_pair(c, v);
		this->head = new DLLNode;
		this->head->set_info(x);
		this->head->set_prev(NULL);
		this->head->set_next(NULL);
		this->tail = this->head;
		return NULL_TVALUE;
	}
	else
	{
		if (this->search(c) != NULL_TVALUE)
		{
			DLLNode *p = this->head;
			while (p->get_next() != NULL)
			{
				if (p->get_info().first == c)
				{
					TValue r = p->get_info().second;
					p->set_info(make_pair(c, v));
					return r;
				}
				p = p->get_next();
			}
			if (p->get_info().first == c)
			{
				TValue r = p->get_info().second;
				p->set_info(make_pair(c,v));
				return r;
			}
		}
		else
		{
			DLLNode *p = new DLLNode;
			p->set_next(NULL);
			p->set_prev(this->tail);
			p->set_info(make_pair(c,v));
			this->tail->set_next(p);
			this->tail = p;
			return NULL_TVALUE;
		}
	}
	return NULL_TVALUE;
}

TValue Map::search(TKey c) const
{
	DLLNode *p = this->head;
	while (p != NULL)
	{
		if (p->get_info().first == c)
			return p->get_info().second;
		p = p->get_next();
	}
	return NULL_TVALUE;
}

TValue Map::remove(TKey c)
{
	if (this->search(c) == NULL_TVALUE)
		return NULL_TVALUE;
	if (this->head->get_info().first == c)
	{
		int v = this->head->get_info().second;
		this->head = this->head->get_next();
		this->head->set_prev(NULL);
		return v;
	}
	if (this->tail->get_info().first == c)
	{
		int v = this->tail->get_info().second;
		this->tail = this->tail->get_prev();
		this->tail->set_next(NULL);
		return v;
	}
	DLLNode *p = this->head;
	while (p != NULL)
	{
		int v = p->get_info().second;
		if (p->get_info().first == c)
		{
			p->get_prev()->set_next(p->get_next());
			p->get_next()->set_prev(p->get_prev());
			return v;
		}
		p = p->get_next();
	}
	
	return NULL_TVALUE;
}

int Map::size() const
{
	if (this->head==NULL)
		return 0;
	else 
	{
		int size = 0;
		DLLNode *p = this->head;
		while (p != NULL)
		{
			size++;
			p=p->get_next();
		}

		return size;
	}
}

bool Map::isEmpty() const
{
	if (this->head==NULL)
		return true;
	return false;
}

MapIterator Map::iterator() const
{
	return MapIterator(*this);
}

Map::~Map()
{
}
