
for i in range(5+1):
    for j in range(5+1):
        print('*','\t',end='')


for i in range(1,5+1):
    for j in range(1,i+1):
        print('*','\t',end='')
    print()

for a in range(1,5+1):
    print('*'*(a))

n=100
for v in range(1,10+1):
    print(''*n,end ='')
    print('*'*(v))
    n-=1


n=100
for l in range(1,11):
    print(''*(n-l)+'*'*(l))


for i in range(1,6):                       # 1
    for j in range(1, i + 1):              # 1 2
        print(j, end='')                   # 1 2 3
    print()                                # 1 2 3 4


for i in range(1,5+1):                       # *
    for j in range(1,i+1):                   # * *
        print('*','\t',end='')               # * * *
    print()                                  # * * * *
