import pandas as pd
m=pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv", usecols=["Age", "Sex"])
print(m)



print()
print()
#Selecting rows base index conditions:
import pandas as pd
m=pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv", usecols=[2,4])
print(m)