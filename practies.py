# print("kghj")
# print("UYIUIY B IUGYi G HKVGJ")
# a=0
# print(a)

# A=67435627
# print( 'gsfadhjk',A,'io4upywer\n'"owhuierf" ,end="      "'fediohupjfds')

'''num=int(input('enter a no'))
if num==1:
          print("one")
if num==2:
     print('two')
elif  num==8:
     print('eihgt')
else:
    print("no N0mber")
# max=
# print(max)
# count=1
# while count<=90:
    # print(count)
    # count+=9

# print("fgjhc uvitg iulg(fans ,etc.)")print("Help! My computer doesn't work!")
done = False # Not done initially
while not done:
  print("Does the computer make any sounds (fans, etc.) ")
  choice = input("or show any lights? (y/n):")
# The troubleshooting control logic
  if choice == 'n': # The computer does not have power
     choice = input("Is it plugged in? (y/n):")
     if choice == 'n': # It is not plugged in, plug it in
       print("Plug it in.")
     else: # It is plugged in
        choice = input("Is the switch in the \"on\" position? (y/n):")
        if choice == 'n': # The switch is off, turn it on!
           print("Turn it on.")
        else: # The switch is on
             choice = input("Does the computer have a fuse? (y/n):")
             if choice == 'n': # No fuse
                 choice = input("Is the outlet OK? (y/n):")
             if choice == 'n': # Fix outlet
                     print("Check the outlet's circuit ")
                     print("breaker or fuse. Move to a")
                     print("new outlet, if necessary. ")
             else: # Beats me!
                  print("Please consult a service technician.")
                  done = True # Nothing else I can do
  else: # Check fuse
            print("Check the fuse. Replace if ")
            print("necessary.")
else: # The computer has power
     print("Please consult a service technician.")
     done = True # Nothing else I can do


a=1    
while a<=8:
    print ("i love u")

    a +=1
   

# a=1
# stop=int(input('a='))
# while a<=stop:
#     print(a)
#     a+=1

a=9
if a==9:
    print("nine")
elif a==5:
    print('five ')  
else:
    print("no nomber")      
print ('done')'


x=1
a=int(input("a="))
while x<=a:
    print("s")
    x+=1

num =23

print("sum is : ", (num%2+num/2%2+2))


a=12
b='dsa'
print(type(a))
print(type(b)) 

num1=int(input('enter a no= '))
num2=int(input('enter a no= '))
print( num1,'+',num2,'=',num1+num2)


print('please enter tha value',end='\n')

print('a',end='*')
print('s',end='*')
print('d',end='*')
print('f',end='*')
print('g',end='*')

print('\n')

print(25/4,4/25)

degreesF=float(input('enter temperature f ='))
degreesC=5/9*(degreesF- 32)
print (degreesC)

x=798
z=978
print ('x =',x,'z =',z)
diff=x-z
if diff<0:
    diff=-diff
if diff<0.76896 : 
    print('same')
else :
    print ('diff')       


month = int(input("Please enter the month as a number (1-12): "))
day = int(input("Please enter the day of the month: "))
# Translate month into English
if month == 1:
 print("January " ,end='')
elif month == 2:
 print("February ", end='')
elif month == 3:
 print("March ", end='')
elif month == 4:
 print("April ", end='')
elif month == 5:
 print("May ", end='')
elif month == 6:
 print("June ", end='')
elif month == 7:
 print("July ", end='')
elif month == 8:
 print("August ", end='')
elif month == 9:
 print("September ", end='')
elif month == 10:
 print("October ", end='')
elif month == 11:
 print("November ", end='')
else:
 print("December ", end='')
# Add the day
print(day, 'or', day, end='')
# Translate month into Spanish
if month == 1:
 print('de janu')
 print(" de febrero")
elif month == 3:
 print(" de marzo")
elif month == 4:
 print(" de abril")
elif month == 5:
 print(" de mayo")
elif month == 6:
 print(" de junio")
elif month == 7:
 print(" de julio")
elif month == 8:
 print(" de agosto")
elif month == 9:
 print(" de septiembre")
elif month == 10:
 print(" de octubre")
elif month == 11:
 print(" de noviembre")
else:
 print(" de diciembre")


n=int( input( 'enter a np ='))
print("|",n,'| =',(-n if n<0 else n ), sep='')


n=int( input( 'enter a np ='))
print("|",n,'| =',(n if n>=0 else -n ), sep='')

n=17
while n <=10:
    print (n*3)
    n+=1

a=False
while not a :
    entry= int(input())
    if entry ==999:
        a=True
    else :
        print( entry)    


for  n in range(21,0, -3):
    print (n, end =',')


# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
for row in range(1, size + 1):
    print("Row #", row)


s =int ( input(" enter  size ="))
for row in range (1,s+1):
    for colaum in range (1,s+1):
     c=row*colaum

    print( c, end ="  " )     
print( )




# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
for row in range(1, size + 1):
   for column in range(1, size + 1):
      product = row*column # Compute product
      print(product, end=' ') # Display product
print() # Move cursor to next row'''

'''
s=int(input("enter a number="))
print("  ", end='')
for column in range( 1,s+1):
    print('{0:4}'.format(column),end='')
print ( )
print ( " +", end='')
for column in range(1, s+1):
    print('----',end='')
print( )
for row in range ( 1, s+1):
    print('{0:3} |'.format(row), end=' ')
    for column in range(1,s+1):
     p=row*column
     print ('{0:4}'.format(p),end='')
    print()'''



# size = int(input("Please enter the table size: "))


# print(" ", end='')

# for column in range(1, size + 1):
#    print('{0:4}'.format(column), end='')
# print() 

# print(" +", end='')
# for column in range(1, size + 1):
#    print('----', end='')
# print() 

# for row in range(1, size + 1):
#    print('{0:3} |'.format(row), end='') 
#    for column in range(1, size + 1):
#     product = row*column 
#     print('{0:4}'.format(product), end='') 
#    print()

# a= str (input("enter name = "))
# for first in a:
#     for second in a:
#         if first !=second :
#             for third in a:
#                 for firth in a :
                #   if third !=second !=first !=firth :
                #     print(first + second +third + firth)


'''secend = int (input('enter secend ='))
# hour= secend//3600
menits1 = secend //60
secend1 = secend % 60
h = menits1 // 60
menits2 = menits1 % 60
print('hour =', h, 'menits=', menits2, 'secend2=',secend1)'''


'''
a=90
while a/8:
    print(a)
    a=a+1
'''

word=input('enter the word = ')
for letter in (word):
    print(letter)

for i in range (10):
    print (i,end='  ')
    if i==5:
        i=20
    print ('({})'.format(i),end='  ')
print()


























