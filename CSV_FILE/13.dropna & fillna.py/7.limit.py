import pandas as pd
m=pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\3new_number.csv" )
print(m.fillna("python",limit=1))
print()
print('------------------------')