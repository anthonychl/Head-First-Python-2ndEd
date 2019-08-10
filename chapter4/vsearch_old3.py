
def search4vowels(word):
    """ return any vowels found in a supplied word """
    vowels = set('aeiou')
    return vowels.intersection(set(word)) #return a set
    