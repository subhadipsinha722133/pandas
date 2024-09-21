import pandas as pd

var = pd.DataFrame(
    {
        "Name": ["a", "b", "c", "d", "a", "b", "a", "b", "a", "c", "c", "d"],
        "S_1": [12, 13, 14, 12, 13, 14, 15, 23, 25, 16, 10, 34],
        "S_2": [23, 24, 25, 26, 27, 28, 29, 30, 25, 34, 35, 56],
    }
)
print(var)
print()
v = var.groupby("Name")

print(v)
print()
for x, y in v:
    print(x)
    print(y)
    print()

print(v.get_group("a"))

print("------------------------------------")
print(v.min())


print("------------------------------------")
print(v.max())


print("------------------------------------")
print(v.mean())
print("------------------------------------")
print("------------------------------------")
li = list(v)
print(li)
