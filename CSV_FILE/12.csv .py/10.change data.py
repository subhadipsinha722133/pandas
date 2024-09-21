import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv")
m["Age"][0] = "SUBHADIP"
print(m)


print()
print()
m.loc[3, "Age"] = "Sinha"
print(m)

print()
print()
