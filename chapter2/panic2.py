# challenge turn "Don't panic" into "on tap" using slices

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])  
new_phrase = new_phrase + ''.join( [plist[5],plist[4],plist[7],plist[6]] ) #join takes only one argument so we make a list

print(plist)
print(new_phrase)