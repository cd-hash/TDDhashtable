from hashtable.hashtable_utils import BLANK

class HashTable:
    def __init__(self, capacity: int):
        # fill a list of some length N and give it default values
        self.values: list[BLANK] = capacity * [BLANK]

    def __len__(self) -> int:
        return len(self.values)

    def __setitem__(self, key, value):
        '''
        You turn an arbitrary key into a numeric hash
        value and use the modulo operator to constrain the
        resulting index within the available address
        space. Great! Your test report lights up green
        again.
        '''
        index: int = hash(key) % len(self)
        self.values[index] = value