#sum the ordinal values of text to pseudo hash
def sum_hash(text):
    return sum(ord(char) for char in repr(text))