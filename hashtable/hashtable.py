from hashtable.hashtable_utils import Pair

class HashTable:
    def __init__(self, capacity: int):
        # fill a list of some length N and give it default values
        self.pairs: list[None] = capacity * [None]

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
        self.pairs[self.__index(key)] = Pair(key, value)

    def __getitem__(self, key): # this implements the dict[key] returns value
        pair = self.pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, key): # this lets us use the 'in' operator
        try:
            self[self.__index(key)]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[self.__index(key)]
        except KeyError:
            return default

    def __delitem__(self, key): # this lets us use the del operator
        if key in self:
            self[self.__index(key)] = None
        else:
            raise KeyError(key)

    def __index(self, key):
        return hash(key) % len(self)
        
        