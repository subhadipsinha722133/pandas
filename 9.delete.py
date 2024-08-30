import pandas as pd

print("old data")
var = pd.DataFrame(
    {
        "A": [1, 2, 35, 67, 7, 8],
        "B": [10, 20, 350, 670, 0, 4],
        "C": [180, 2, 30, 67, 3, 4],
    }
)
print(var)

print()
print("deleted data is")
var1 = var.pop("B")
print(var1)


print()
print("new data")
print(var)

print()
del var["A"]
print(var)
