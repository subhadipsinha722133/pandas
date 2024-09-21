import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv")
print(m.loc[[2, 3], ["Age", "Purpose"]])


print()
print()
print()
print()


print(m.loc[:, ["Age", "Purpose"]])
print()
print()
print()
print()


print(m.loc[[2, 3], :])
