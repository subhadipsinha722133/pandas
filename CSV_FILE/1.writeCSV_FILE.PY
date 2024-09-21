import pandas as pd
dis={"A":[1,2,35,67,7,8],"B":[10,20,350,670,60,94],"C":[180,2,350,670,0,4]}

var = pd.DataFrame(dis)
print(var)
var.to_csv("PANDAS\CSV_FILE\\all_csv_file\\1new_number.csv")