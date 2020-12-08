from datetime import *

class DataStructure:
    def __init__(self,lista):
        self.index=0
        self.data=lista

    def append(self,item):
        self.data.append(item)

    def __setitem__(self,index,value):
        self.data[index]=value

    def __getitem__(self,index):
        return self.data[index]

    def __delitem__(self, index):
        del self.data[index]

    def __len__(self):
        return len(self.data)

    def __next__(self):
        if self.index>=len(self.data):
            self.index=0
            raise StopIteration
        index=self.index
        self.index=self.index+1
        return self.data[index]

    def __iter__(self):
        return self

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data==other

def gnome_sort(array,order):
    length=len(array)
    index = 0
    while index < length:
        if index == 0:
            index = index + 1
        if order=="ascendent" and array[index] >= array[index - 1]:
            index = index + 1
        elif order=="descendent" and array[index] <= array[index - 1]:
            index = index + 1
        else:
            array[index], array[index-1] = array[index-1], array[index]
            index = index - 1
  
    return array

import unittest

class Test(unittest.TestCase):
    def test_sort(self):
        arr = DataStructure([1, 9, 7, -2])
        gnome_sort(arr,"ascendent")
        self.assertEqual(arr,[-2,1,7,9])

        arr = DataStructure([1, 9, 7, -2])
        gnome_sort(arr, "descendent")
        self.assertEqual(arr, [9,7,1,-2])

def filter(array,case):
    filtered_list=[]
    for i in range(len(array)):
        if case=="passed_date_movies":
            if array[i].returned_date_get() == None and array[i].due_date_get() < datetime.today():
                filtered_list.append(array[i])
    return filtered_list



