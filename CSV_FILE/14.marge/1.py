import pandas as pd 
v= pd.DataFrame({"A":[1,2,5,6,7,8],"B":[10,20,350,670,60,94]})
vv= pd.DataFrame({"A":[1,2,5,6,7,8],"C":[10,20,50,60,6,94]})

o=pd.DataFrame({"A":[1,20,5,6,70,80],"D":[10,2,35,60,60,9]})

print(v)
print()
print()
print(vv)
print()
print()
print(o)
print('-----------------------------------------')
print()
M=pd.merge(v,vv,on="A")
print(M)
print()
print()
print(pd.merge(v,o,on="A"))