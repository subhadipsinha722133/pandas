import pandas as pd

var = pd.DataFrame({"A": [1, 2, 35, 67, 7, 8], "B": [10, 20, 350, 670, 0, 4]})
print(var)
print()

var["python"] = var["A"][:3]
print(var)
