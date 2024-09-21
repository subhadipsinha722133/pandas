import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv")
# The code `print(m.dropna(inplace=True))` is dropping any rows from the DataFrame `m` that contain
# missing values (NaN) and updating the DataFrame in place due to the `inplace=True` parameter.
print(m.dropna(inplace=True))
print()
print("------------------------")

print(m.fillna("python", limit=2))
