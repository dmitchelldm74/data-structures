import random

class LinkedList:

    def __init__(self,value=None,nextitem=None):
        """Creates empty LinkedList"""
        self._value = value
        self._next_item = nextitem
        
    def prepend(self,val):
        self.__init__(val, LinkedList(self._value, self._next_item))

    def append(self, val):
        if self._value is None:
            self._value = val
            self._next_item = LinkedList()
        else:
            self._next_item.append(val)
            
    def extend(self,extension):
        if self._next_item._value == None:
            self._next_item = extension
        elif isinstance(extension, LinkedList):
            self._next_item.extend(extension)
        else:
            self._extend_from_iteratable_object(extension)
            
    def swap(self,index1,index2):
        self[index1], self[index2] = self[index2], self[index1]
            
    def _extend_from_iteratable_object(self,iter_object):
        for l in linkedlist:
            self.append(l)
            
    def dump(self,*items):
        for i in items:
            self.append(i)

    def __len__(self):
        if self._value == None:
            return 0
        else:
            return 1 + len(self._next_item)
            
    def __add__(self, other):
        #if other._next_item != None:
            new = LinkedList()
            for i in self:
                if new != None:
                    new.append(i)            
            new.extend(other)
            return new
        #return self

    def __getitem__(self, index):
        if isinstance(index,slice):
            stop = index.stop
            length = len(self)
            if stop > length or stop == None:
                stop = length
            step = index.step
            step = step if step != None else 1
            start = index.start
            start = start if start != None else 0
            return self._slice(start,stop,step)
        else:
            return self.get(index)._value
        
    def get(self, index):
        if index == 0 and self._value != None:
            return self
        elif self._next_item != None:
            return self._next_item.get(index-1)
        raise IndexError
        
    def _slice(self,start,stop,step):
        ll = LinkedList()
        for x in range(start,stop,step):
            ll.append(self[x])
        return ll
        
    def __setitem__(self, index, val):
        if index == 0:
            self._value = val
        elif self._next_item != None:
            self._next_item[index-1] = val
        else:
            raise IndexError # ("Index %r not in 'LinkedList'"%(index))
            
    def __delitem__(self, index):
        self.pop(index)

    def insert(self, index, val):
        if index == 0:
            ll = LinkedList()
            ll._value = self._value
            ll._next_item = self._next_item
            self._value = val
            self._next_item = ll
        elif self._next_item != None:
            self._next_item.insert(index-1,val)
        else:
            raise IndexError # ("Index %r not in 'LinkedList'"%(index))
                
    def pop(self,index=None):
        if index == None:
            return self._pop(len(self)-1)
        return self._pop(index)
            
    def _pop(self,index=0):
        if index == 0:
            value = self._value
            self.__init__(self._next_item._value, self._next_item._next_item)
            return value
        elif self._next_item != None:
            return self._next_item._pop(index-1)
        raise IndexError # ("Index %r not in 'LinkedList'"%(index))
        
    def remove(self,equivalent): 
        if self._next_item != None:
            if equivalent == self._next_item._value:
                self._next_item = self._next_item._next_item
            elif equivalent == self._value:
                self.pop(0)
            else:
                self._next_item.remove(equivalent)      
        else:
            raise ValueError("There is no element equal to %r in 'LinkedList'"%(equivalent))
            
    def reverse(self):
        reversed_list = LinkedList()
        for x in self:
            if x != None:
                reversed_list.prepend(x)
        return reversed_list
        
    def update(self,linkedlist):
        self.__init__(linkedlist._value, linkedlist._next_item)
            
    def index(self,equivalent,i=0):
        if self._next_item != None:
            if equivalent == self._value:
                return i+1
            else:
                return self._next_item.index(equivalent,i=i+1)
        raise ValueError("There is no element equal to %r in 'LinkedList'"%(equivalent))
        
    def count(self,item,count=0):
        if self._next_item != None:
            if item == self._value:
                count += 1
            return self._next_item.count(item,count=count)
        return count
        
    def lastitem(self,index=False,i=0): # get the last item without calling len, can get index if True is passed in to args.
        if self._next_item._value == None:
            if index == True:
                return i+1
            return self._value
        else:
            return self._next_item.lastitem(i=i+1,index=index)
        
    def __eq__(self, equivalent): # for now, not testing bc I have not fully implemented it yet
        return repr(self) == repr(equivalent)

    def __repr__(self):
        if self._value is None:
            return "{}"
        else:
            return "{%r, %s}" % (self._value, self._next_item._repr())
            
    def _repr(self):
        if self._value is None:
            return ""
        else:
            return "%r, %s" % (self._value, self._next_item._repr())
            
    def __iter__(self):
        self._iter_next_item = self
        return self
        
    def __next__(self):
        return self.next()
        
    def next(self):
        if self._iter_next_item != None and self._iter_next_item._value != None:
            val = self._iter_next_item._value
            self._iter_next_item = self._iter_next_item._next_item
            return val
        else:
            raise StopIteration
            
    def sort(self,reverse=False,bubble=False):
        if bubble:
            self._bubblesort(reverse=reverse)
        li = self._quicksort(self)
        if reverse == True:
            li = li.reverse()
        self.update(li)
        
    
    def _bubblesort(self,reverse=False):
        for num in range(len(self)-1,0,-1):
            for i in range(num):
                if ((not reverse) and self[i] > self[i+1]) or (reverse and self[i] < self[i+1]):
                    self.swap(i,i+1)
                    
    def _quicksort(self,li): # li for list
        if len(li) < 2:
            return li
        else:
            p = li[0]
            less, greater = LinkedList(), LinkedList()
            for i in li[1:]:
                if i <= p:
                    less.append(i)
                elif i > p:
                    greater.append(i)
            return self._quicksort(less) + LinkedList(p) + self._quicksort(greater)
    
    def jumble(self):
        random.shuffle(self)
        return self
            
    # Other methods to consider:
    #   pop, index, remove, reverse
