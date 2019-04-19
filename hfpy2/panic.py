phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist = plist[1:7]
plist[2] = " "
plist[-2] = 'a'

new_phrase = "".join(plist)
print(plist)
print(new_phrase)