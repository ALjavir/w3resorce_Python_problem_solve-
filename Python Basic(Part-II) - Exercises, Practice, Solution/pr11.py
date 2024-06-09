X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70

from itertools import product
combo=[i for i in product(X,Y,Z) if sum(i)==T]
print(combo)