for i in range (10):
    print (i,end='  ')
    if i==5:
        i=20
    print ('({})'.format(i),end='  ')
print()



for c in 'ABCDEF':
  print('[', c, ']', end='', sep='')
print()






size=int (input('enter a value='))
for row in range(1,size+1):
   for coloum in range(1,size+1):
    # b=row*coloum
    print('({0:3})'.format(row*coloum ),end=' ')                   
   print()     
   