from hashtable.hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_size_attr():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [None, None, None]