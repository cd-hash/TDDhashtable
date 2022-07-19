# hashtable.py

class HashTable:
    def __init__(self, capacity: int):
        # fill a list of some length N and give it default values
        self.values: list[None] = capacity * [None]

    def __len__(self):
        return len(self.values)