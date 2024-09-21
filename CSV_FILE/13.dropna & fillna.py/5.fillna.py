import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv")
print(m)
print("------------------------")
print()
# The `print(m.fillna("python"))` statement is filling any missing values in the DataFrame `m` with
# the string "python". The `fillna()` method in pandas is used to fill NA/NaN values with a specified
# value. In this case, it will replace any missing values in the DataFrame `m` with the string
# "python" and then print the updated DataFrame.
print(m.fillna("python"))
print("------------------------")
print()
print("------------------------")
print()
# The statement `print(m.fillna({"3000":"hello"}))` is filling any missing values in the DataFrame `m`
# specifically in the column labeled "3000" with the string "hello".
print(m.fillna({"3000": "hello"}))
print("------------------------")
print()

print(m.fillna({"3000": "hello", "2000": "hi"}))
