import pandas as pd
m=pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv" )
print(m.tail())

# `print(m.tail())` is displaying the last 5 rows of the DataFrame `m`. The `tail()` function in
# pandas is used to display the last n rows of a DataFrame, where n is the number of rows specified
# (default is 5 if no value is provided).


print()
print(m.tail(2))