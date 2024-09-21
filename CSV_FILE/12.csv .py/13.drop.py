import pandas as pd
m=pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv" )
# The code `print(m.drop("Purpose",axis=1))` is dropping the column named "Purpose" from the DataFrame
# `m`. The `drop()` function in pandas is used to remove rows or columns from a DataFrame. In this
# case, `axis=1` specifies that we are dropping a column (as opposed to dropping a row), and "Purpose"
# is the name of the column being dropped. The result of this operation is then printed using the
# `print()` function.
print(m.drop("Purpose",axis=1))



print()
print()
print()
# The code `print(m.drop(0,axis=0))` is dropping the row with index 0 from the DataFrame `m`.
print(m.drop(0,axis=0))
