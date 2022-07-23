from hashtable.hashtable import HashTable

def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

hash_table = hash_table()

assert "hola" in hash_table
assert ("hola", "hello") in hash_table.pairs
assert len(hash_table) == 3

print(hash_table.pairs)
del hash_table["hola"]
print(hash_table.pairs)
assert "hola" not in hash_table

assert ("hola", "hello") not in hash_table.pairs
assert len(hash_table) == 2