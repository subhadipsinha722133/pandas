from array import *
x=array('i',[20,3,45,78,98,2,00])

y=x[1:3]
print(y)

y=x[:4]
print(y)

y=x[-4:]
print(y)

y=x[-4:-1]
print(y)

y=x[0:6:2]
print(y)


from array import *
a=array('i',[4,5,6,7,8,9,3,0,1,2,20,10,30,40,80,60])
for i in a[2:9]:
    print(i)
