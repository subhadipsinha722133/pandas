import pandas as pd

d1 = pd.DataFrame({"A": [1, 2, 3, 4], "B": [11, 12, 13, 14]})
d2 = pd.DataFrame({"A": [1, 2], "C": [21, 22]})

print(pd.concat([d1, d2], axis=1))
