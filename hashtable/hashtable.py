from hashtable.hashtable_utils import Pair

class HashTable:
    def __init__(self, capacity: int):
        # fill a list of some length N and give it default values
        self._pairs: list[None] = capacity * [None]

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
        self._pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key): # this implements the dict[key] returns value
        pair = self._pairs[self._index(key)]
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
            self._pairs[self._index(key)] = None
        else:
            raise KeyError(key)

    def _index(self, key):
        return hash(key) % len(self._pairs)

    @property
    def values(self):
        return [pair.value for pair in self.pairs]

    @property
    def pairs(self):
        return {pair for pair in self._pairs if pair}

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}
