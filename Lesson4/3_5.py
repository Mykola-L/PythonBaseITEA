from collections import Counter

array = ["Bob", "Alex", "Bob", "John"]

c = Counter(array)

c
Counter({'Bob': 2, 'Alex': 1, 'John': 1})

c['Bob']
2

c['Unknown']
0

print(c)