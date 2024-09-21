import pandas as pd
m=pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv", skiprows=[0,1])
print(m)


print()
print()

m=pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv", skiprows=[1,3,4,2])
print(m)
