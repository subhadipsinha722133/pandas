import pandas as pd 
var = pd.DataFrame({"A":[1,2,35,67],"B":[10,20,350,670]})
print(var)

print()
var.insert(1,"Python",var["A"])
print(var)


print()
var.insert(2,"Python_1",[10,2,6,9])
print(var)

print()
var.insert(1,"Python_2",[100,200,600,900])
print(var)
