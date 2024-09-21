import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\new.csv")
print(m)
print("----------------------------------------------")
print()
print(m.replace(1, method="ffill"))
print()
print(m.replace(1, method="ffill", limit=2))


# print(m.interpolate())
