import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv")
print(m)

print()
print()
print("------------------------")

# `print(m.dropna())` is removing any rows from the DataFrame `m` that contain missing values (NaN)
# and then printing the resulting DataFrame without those rows.
print(m.dropna())

print()
print()
print("------------------------")

# `print(m.dropna(axis=1))` is removing any columns from the DataFrame `m` that contain missing values
# (NaN) and then printing the resulting DataFrame without those columns. The `axis=1` parameter
# specifies that the operation should be performed on columns instead of rows.
print(m.dropna(axis=1))

print()
print("------------------------")

# `print(m.dropna(axis=0))` is removing any rows from the DataFrame `m` that contain missing values
# (NaN) and then printing the resulting DataFrame without those rows. The `axis=0` parameter specifies
# that the operation should be performed on rows.
print(m.dropna(axis=0))

print()
print("------------------------")

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv")
print(m.dropna(how="any"))  # If there are any NaNs in a row, drop the whole row


# https://youtu.be/rnL312mXb2I?si=XvX5KOEx0y8pXlQm    =============youtub link

print()
print("------------------------")

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv")
print(m.dropna(how="all"))
