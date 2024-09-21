import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\new.csv")
print(m)
print("----------------------------------------------")
print()
print(m.replace({"subhadip", "[A-Za-z]"}, 90, regex=True))
