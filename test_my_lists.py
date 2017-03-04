from my_lists import LinkedList


def test_append():
    ll = LinkedList()
    ll.append(5)
    ll.append(3)
    ll.append(1)

    assert repr(ll) == '(5, (3, (1, ())))'
