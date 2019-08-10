# this is pep8 compliant code
# (compare it to vsearch_old4.py)


def search4vowels(phrase: str)->set:
    """ return any vowels found in a supplied phrase """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))  # return a set


# in this function we let the user provide the letters to search for
# and the phrase to search in
# and we set a default value for 'letters'
def search4letters(phrase: str, letters: str='aeiou') -> set:
    """ return a set of the 'letters' found in a 'phrase' """
    return set(letters).intersection(set(phrase))
