import collections
import pprint
a = input("Enter the file name: ")
with open(a, "r") as info:
    c = collections.Counter(info.read().upper())
    v = pprint.pformat(c)
    print(v)