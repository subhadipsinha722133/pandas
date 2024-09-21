import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv")
# The code `print(m.fillna(method="ffill"))` is filling missing values in the DataFrame `m` using the
# forward fill method.
print(m.fillna(method="ffill"))
print("------------------------")
print()
# The code `print(m.fillna(method="bfill"))` is filling missing values in the DataFrame `m` using the
# backward fill method. This means that missing values in the DataFrame will be filled with the next
# valid value along each column in a backward direction.
print(m.fillna(method="bfill"))

print()
print("------------------------")
# The code `print(m.fillna(method="bfill",axis=0))` is filling missing values in the DataFrame `m`
# using the backward fill method along the columns. This means that missing values in the DataFrame
# will be filled with the next valid value along each row in a backward direction. The `axis=0`
# parameter specifies that the filling should be done along the columns.
print(m.fillna(method="bfill", axis=0))

print()
print("------------------------")
print(m.fillna(method="ffill", axis=1))
