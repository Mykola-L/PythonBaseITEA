#str = "python java c c++ javascript pascal php"

str = input('Please enter a string (words are separated by a space) ')
print(str)

listWords = str.split()

idLongestWord = 0

for i in range(1,len(listWords)):
    if len(listWords[idLongestWord]) < len(listWords[i]):
        idLongestWord = i

print(listWords[idLongestWord])