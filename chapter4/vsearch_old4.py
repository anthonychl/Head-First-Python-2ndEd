# using annotations

def search4vowels(phrase:str)->set:
    """ return any vowels found in a supplied phrase """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))  # return a set

# in this function we let the user provide the letters to search for and the phrase to search in
def search4letters(phrase:str, letters:str='aeiou') -> set: # and we set a default value for 'letters'
    """ return a set of the 'letters' found in a 'phrase' """
    return set(letters).intersection(set(phrase))
