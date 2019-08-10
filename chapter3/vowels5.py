#variant of the code using the setdefault method

vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")

found = {}  #now we only initialize the dict, we dont have to add key/values as it is done later w/ setdefault

for letter in word:
    if letter in vowels:
        found.setdefault(letter,0) # use the set default method to avoid KeyError exceptions
        found[letter]+=1
for k,v in sorted(found.items()):
    print(k, 'was found',v, ' time(s)')