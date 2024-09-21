import pandas as pd

m = pd.read_csv("PANDAS\\CSV_FILE\\all_csv_file\\german.csv", names=["subhadip"])
print(m)

import pandas as pd

m = pd.read_csv(
    "PANDAS\\CSV_FILE\\all_csv_file\\german.csv", names=["subhadip", "sinha", "hello"]
)
print(m)
