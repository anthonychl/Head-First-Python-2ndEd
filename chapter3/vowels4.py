#variant of the code using dictionaries

vowels = ['a','e','i','o','u']
word = input("Provide a word to search for variables: ")

found = {}     #creating a dictionary this time instead of a list
found['a']=0   #adding keys and values to the dict
found['e']=0
found['i']=0
found['o']=0
found['u']=0

for letter in word:
    if letter in vowels:
        found[letter]+=1
for k,v in sorted(found.items()):
    print(k, 'was found',v, ' time(s)')