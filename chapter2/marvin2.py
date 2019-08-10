#iterating over slices

paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)

for char in letters[:6]:  #first six letters
    print('\t', char)

for char in letters[-7:]: #last seven letters
    print('\t'*2, char)   #using the multiplication operator to insert 2 tabs before the char

for char in letters[12:20]:  # an inner slice
    print('\t'*3, char)