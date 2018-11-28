"""
create hash functions for character-based items such as strings.
"""
def hash(astring,tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum % tablesize

"""
When using this hash function, anagrams will always be given the same hash value. 
To remedy this, we could use the position of the character as a weight. 
One possible way to use the positional value as a weighting factor. 
"""
def hashwithWeight(astring,tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])*(pos+1)
    return sum % tablesize

print(hashwithWeight('cat',11))