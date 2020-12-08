class Bag:

    # creates a new, empty Bag
    def __init__(self):
        self.elems=[]

    # adds a new element to the Bag
    def add(self, e):
        if self.search(e)==0:
            self.elems.append([e,1])
        else:
            for i in range(len(self.elems)):
                if self.elems[i][0]==e:
                    self.elems[i][1]+=1

    # removes one occurrence of an element from a Bag
    # returns True if an element was actually removed (the Bag contained the element e), or False if nothing was removed
    def remove(self, e):
        if self.search(e)==False:
            return False
        for i in range(len(self.elems)):
            if self.elems[i][0] == e:
                self.elems[i][1]-=1
                if self.elems[i][1]==0:
                    self.elems.pop(i)
                return True

    # searches for an element e in the Bag
    # returns True if the Bag contains the element, False otherwise
    def search(self, e):
        for i in range(len(self.elems)):
            if self.elems[i][0] == e:
                return True
        return False

    # counts and returns the number of times the element e appears in the bag
    def nrOccurrences(self, e):
        if self.search(e)==False:
            return 0
        for i in range(len(self.elems)):
            if self.elems[i][0] == e:
                return self.elems[i][1]

    # returns the size of the Bag (the number of elements)
    def size(self):
        s=0
        for i in range(len(self.elems)):
            s+=self.elems[i][1]
        return s

    # returns True if the Bag is empty, False otherwise
    def isEmpty(self):
        if len(self.elems)==0:
            return True
        return False

    # returns a BagIterator for the Bag
    def iterator(self):
        return BagIterator(self)

class BagIterator:

    #creates an iterator for the Bag b, set to the first element of the bag, or invalid if the Bag is empty
    def __init__(self, b):
        self.bag=b
        if len(self.bag.elems) == 0:
            self.iterator = -1
        self.iterator=0
        self.i=0

    # returns True if the iterator is valid
    def valid(self):
        if self.iterator<0 or self.iterator>=(self.bag.size())-1:
            return False
        return True

    # returns the current element from the iterator.
    # throws ValueError if the iterator is not valid
    def getCurrent(self):
        if self.valid()==True:
            return self.bag.elems[self.i][0]
        else:
            raise ValueError

    # moves the iterator to the next element
    #throws ValueError if the iterator is not valid
    def next(self):
        if self.valid()==True:
            self.iterator += 1
            self.i += 1
            if self.i>=len(self.bag.elems):
                self.i=0
        else:
            raise ValueError

    # sets the iterator to the first element from the Bag
    def first(self):
        self.iterator=0
        self.i = 0