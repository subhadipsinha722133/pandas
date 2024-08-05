import pandas as pd

l = [1, 2, 34, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
var = pd.DataFrame(l)
print(var)


m = {"a": [1, 23, 4, 5, 6], "n": [465, 9, 0, 78, 5]}
var1 = pd.DataFrame(m)
print(var1)


p = {"a": [1, 23, 4, 5, 6], "n": [465, 9, 0, 78, 5], "c": [24, 56, 675678, 8, 56]}
var2 = pd.DataFrame(p, columns=["a", "c"])
print(var2)
