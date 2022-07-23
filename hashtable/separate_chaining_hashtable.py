from hashtable.hashtable_utils import Pair
from collections import deque

class HashTable:
    """
    this hash table implements the separate
    chaining hash collision resolution technique. 
    Create buckets (doubly linked lists) at empty slots
    that will now house the values. If the list is sufficiently
    large (ours resizes) then you should be able to have O(1) lookup
    insertion and deletion
    """
    def __init__(self, capacity=8, load_factor_threshold=0.6):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("Load factor must be a number between (0, 1]")
        # fill a list of some length N and give it default values
        self._buckets = [deque() for _ in range(capacity)]
        self._load_factor_threshold = load_factor_threshold

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary))
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
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                bucket[index] = Pair(key, value)
                break
        else:
            bucket.append(Pair(key, value))

    def __getitem__(self, key): # this implements the dict[key] returns value
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair.key == key:
                return pair.value
        raise KeyError(key)

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
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[index]
                break
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

    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._buckets = copy._buckets

    @property
    def values(self):
        return [pair.value for pair in self.pairs]

    @property
    def pairs(self):
        return {pair for bucket in self._buckets for pair in bucket}

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}

    @property
    def capacity(self):
        return len(self._buckets)

    @property
    def load_factor(self):
        return len(self) / self.capacity
