from hashtable.hashtable import HashTable

dictionary = {"hola": "hello", 98.6: 37, False: True}

hash_table = HashTable.from_dict(dictionary)

assert hash_table.capacity == len(dictionary) * 10
assert hash_table.keys == set(dictionary.keys())
assert hash_table.pairs == set(dictionary.items())
assert unordered(hash_table.values) == list(dictionary.values())