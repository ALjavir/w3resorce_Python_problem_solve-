import itertools
l = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
l = list(set(l))
for i in itertools.combinations(l, 3):
    if sum(i) == 0:
        print(i)