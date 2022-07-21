from hashtable.hashtable_utils import BLANK

class HashTable:
    def __init__(self, capacity: int):
        # fill a list of some length N and give it default values
        self.values: list[BLANK] = capacity * [BLANK]

    def __len__(self) -> int:
        return len(self.values)

    def __setitem__(self, key, value): # this implements the dict[key] = value
        '''
        You turn an arbitrary key into a numeric hash
        value and use the modulo operator to constrain the
        resulting index within the available address
        space. Great! Your test report lights up green
        again.
        '''
        index: int = self.__index(key)
        self.values[index] = value

    def __getitem__(self, key): # this implements the dict[key] returns value
        index: int = self.__index(key)
        value = self.values[index]
        if value is not BLANK:
            return value
        else:
            raise KeyError(key)

    def __contains__(self, key): # this lets us use the 'in' operator
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key): # this lets us use the del operator
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)

    def __index(self, key):
        return hash(key) % len(self)
        
        