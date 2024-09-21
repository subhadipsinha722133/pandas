import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv")
print(m)
print()
print("------------------------")

# This code snippet is using the `dropna()` method in Pandas to remove rows with missing values in the
# column "sinha" from the DataFrame `m`.
print(m.dropna(subset=["subhadip"]))  # remove rows with missing values
