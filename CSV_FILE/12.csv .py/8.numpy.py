import pandas as pd
import numpy as np

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv")
print(m.to_numpy())
print()
n = np.asarray(m)
print(n)
