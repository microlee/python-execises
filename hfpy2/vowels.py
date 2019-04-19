vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please provide a word to search for vowels: ")
test = list()

for letter in word:
    if letter in vowels:
        if letter not in test:
            test.append(letter)
for x in test:
    print(x)
