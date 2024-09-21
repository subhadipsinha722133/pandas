import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv")
print(m)
print()
print(m.replace(to_replace=10, value=400))

print()
print("------------------------")
print(m.replace(to_replace=2, value="hi"))

print()
print("------------------------")

print(m.replace([2, 10, 7, 8, 60, 94, 670], 0))
