# challenge turn "Don't panic" into "on tap"

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):   # remove 'nic!' at the end
    plist.pop()
plist.pop(0)        # remove 'D' at the start
plist.remove("'")   # remove the apostrophe
plist.extend([plist.pop(),plist.pop()])  # swap 'p' and 'a' by popping them and then extending them to the list
plist.insert(2, plist.pop(3))  # pop the space and insert it in the new position: 2

new_phrase = ''.join(plist)  # turn plist into a string again
print(plist)
print(new_phrase)