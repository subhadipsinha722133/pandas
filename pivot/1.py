import pandas as pd

var = pd.DataFrame(
    {
        "days": [1, 3, 1, 9, 2, 2],
        "st_name": ["a", "b", "c", "a", "b", "c"],
        "eng": [10, 12, 14, 15, 16, 12],
        "maths": [17, 18, 19, 13, 14, 16],
    }
)
print(var)

print()
print(var.pivot(index="days", columns="st_name"))
print()
print(var.pivot(index="days", columns="st_name", values="eng"))

print("-----------------------")
print(var.pivot_table(index="st_name", columns="days", aggfunc="sum"))
print("-----------------------")
print(var.pivot_table(index="st_name", columns="days", aggfunc="mean"))
