import pandas as pd
m=pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv" )
# The code `print(m[3:8])` is slicing the DataFrame `m` to display rows 3 to 7 (since Python uses
# 0-based indexing). This means it will display rows starting from the 4th row (index 3) up to the 8th
# row (index 7) in the DataFrame `m`.
print(m[3:8])


print()
print()
print(m[30:40])
