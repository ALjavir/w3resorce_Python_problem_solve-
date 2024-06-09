#1. Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
a = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
b = sorted(a.items(),key = operator.itemgetter(1))
c = sorted(a.items(),key = operator.itemgetter(1),reverse=True)
print(c)
print(b)