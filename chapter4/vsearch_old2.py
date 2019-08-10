#defining a function that utilizes the code in vowels7.py

def search4vowels(word):
    """ display any vowels found in a supplied word """
    vowels = {'a','e','i','o','u'} #or vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)