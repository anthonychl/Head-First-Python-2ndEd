#same exercise but taking advantage of sets and its methods

vowels = {'a','e','i','o','u'} #or vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")

found = vowels.intersection(set(word))

for vowel in found:
    print(vowel)