from my_lists import LinkedList
import pytest


def test_append():
    ll = LinkedList()
    ll.append(5)
    ll.append(3)
    ll.append(1)

    assert repr(ll) == '{5, 3, 1, }'
    
    
def test_prepend():
    ll = LinkedList()
    ll.append(5)
    ll.prepend(3)
    ll.prepend(1)
    
    assert repr(ll) == '{1, 3, 5, }'
    

def test_dump():
    ll = LinkedList()
    ll.dump(5,3,1)
    
    assert repr(ll) == '{5, 3, 1, }'


def test_len():
    ll = LinkedList()
    ll.dump(5,3,1)
    
    assert len(ll) == 3
    
    
def test_getitem():
    ll = LinkedList()
    ll.dump(5,3,1)
    
    assert ll[0] == 5
    assert ll[1] == 3
    assert ll[2] == 1
    
    
def test_indexerror_getitem():
    ll = LinkedList()
    ll.dump(5,3,1)

    with pytest.raises(IndexError):
        ll[234]
        
    with pytest.raises(IndexError):
        ll[3]
        
        
def test_pop():
    ll = LinkedList()
    ll.dump(5,3,1,0)
    
    assert ll.pop(0) == 5
    assert ll.pop(2) == 0
    assert ll.pop() == 1
    

def test_indexerror_pop():
    ll = LinkedList()
    ll.dump(5,3,1,0)
    
    with pytest.raises(IndexError):
        ll.pop(234)
    
    
def test_delitem():
    ll = LinkedList()
    ll.dump(5,3,1,0)
    ll2 = LinkedList()
    ll2.dump(3,1,0)
    
    del ll[0]
    assert ll == ll2
    
    
def test_indexerror_delitem():
    ll = LinkedList()
    ll.dump(5,3,1,0)

    with pytest.raises(IndexError):
        del ll[234]
        

def test_setitem():
    ll = LinkedList()
    ll.dump(5,3,1)
    ll[0] = 2
    ll[1] = 9
    ll[2] = 10
    
    assert ll[0] == 2
    assert ll[1] == 9
    assert ll[2] == 10
    

def test_indexerror_setitem():
    ll = LinkedList()
    ll.dump(5,3,1)
    
    with pytest.raises(IndexError):
        ll[430] = None
    

def test_insert():
    ll = LinkedList()
    ll.dump(5,3,1)
    ll.insert(0,0)
    

def test_indexerror_insert():
    ll = LinkedList()
    ll.dump(5,3,1)
    
    with pytest.raises(IndexError):
        ll.insert(6, 2)
        

def test_remove():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    ll.remove(1)
    ll.remove(5)
    
    ll2 = LinkedList()
    ll2.dump(4,3,2)
    
    assert repr(ll) == repr(ll2)
    
    
def test_valueerror_remove():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    with pytest.raises(ValueError):
        ll.remove(8)
    
def test_index():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    
    assert ll.index(5) == 1
    assert ll.index(3) == 3
    assert ll.index(1) == 5
    
    
def test_valueerror_index():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    
    with pytest.raises(ValueError):
        ll.index(100)
    
    
def test_lastitem():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    
    assert ll.lastitem() == 1
    assert ll.lastitem(True) == 5
    
    
def test_reverse():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    
    ll2 = LinkedList()
    ll2.dump(1,2,3,4,5)
    
    assert repr(ll.reverse()) == repr(ll2)
    

def test_count():
    ll = LinkedList()
    ll.dump(5,4,3,2,1,5,1,2,3,4,5)
    
    assert ll.count(1) == 2
    assert ll.count(5) == 3
    
    
def test_eq():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    
    ll2 = LinkedList()
    ll2.dump(5,4,3,2,1)
    
    assert ll == ll2
    
    
def test_add():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    
    ll2 = LinkedList()
    ll2.dump(5,4,3,2,1)
    
    ll3 = LinkedList()
    ll3.dump(5,4,3,2,1,5,4,3,2,1)
    
    assert repr(ll+ll2) == repr(ll3)
    assert repr(ll+ll) == repr(ll3)
    
    
def test_iter():
    ll = LinkedList()
    ll.dump(5,4,3,2,1)
    
    ll2 = LinkedList()
    
    for l in ll:
        ll2.append(l)
        
    assert ll == ll2
    
