import pandas as pd

var = pd.DataFrame(
    {
        "days": [1, 2, 3, 4, 5, 6],
        "eng": [10, 12, 14, 15, 16, 12],
        "maths": [17, 18, 19, 13, 14, 16],
    }
)
print(var)

print()
print(pd.melt(var))
print()
print(pd.melt(var, id_vars=["eng"]))

print()
print(var.melt(id_vars=["days"], var_name="python"))
