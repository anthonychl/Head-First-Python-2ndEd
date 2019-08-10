#defining a function that utilizes the code in vowels7.py

def search4vowels():
    """ display any vowels found in an asked-for word """
    vowels = {'a','e','i','o','u'} #or vowels = set('aeiou')
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)