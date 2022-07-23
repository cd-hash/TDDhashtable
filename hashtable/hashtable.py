from hashtable.hashtable_utils import Pair

class HashTable:
    def __init__(self, capacity: int):
        # fill a list of some length N and give it default values
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        self._slots: list[None] = capacity * [None]

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __len__(self) -> int:
        return len(self.pairs)

    def __setitem__(self, key, value): # this implements the dict[key] = value
        '''
        You turn an arbitrary key into a numeric hash
        value and use the modulo operator to constrain the
        resulting index within the available address
        space. Great! Your test report lights up green
        again.
        '''
        self._slots[self._index(key)] = Pair(key, value)

    def __getitem__(self, key): # this implements the dict[key] returns value
        pair = self._slots[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, key): # this lets us use the 'in' operator
        try:
            self[self._index(key)]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[self._index(key)]
        except KeyError:
            return default

    def __delitem__(self, key): # this lets us use the del operator
        if key in self:
            self._slots[self._index(key)] = None
        else:
            raise KeyError(key)

    def __iter__(self):
        yield from self.keys

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)

    def _index(self, key):
        return hash(key) % self.capacity

    @property
    def values(self):
        return [pair.value for pair in self.pairs]

    @property
    def pairs(self):
        return {pair for pair in self._slots if pair}

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}

    @property
    def capacity(self):
        return len(self._slots)
