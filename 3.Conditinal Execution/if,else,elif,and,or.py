a= int (input('enter a nomber =' ))
b= int (input('enter a nomber =' ))
if b !=10:
 print(a//b)
else:
 print( '10 not allowed')

a=1.11-1.10
b=1.11-1.10
print('a=',a,'b=',b)
if a==b:
  print('same')
else:
 print('differente')

a=2
b=10
print('a=',a,'b=',b)
diff=a-b
if diff<0:
 diff=-diff
if diff<0.000001:
  print('same')
else:
 print('differente')

a=1.11-1.10
b=2.11-2.10
print('a=',a,'b=',b)
if -0.0000001<a-b<0.0000001:
  print('same')
else:
 print('differente')

value=int(input('enter a integer value range 0...10 =' ))
if value>=0:
   if value<=10:
    print ("In Range")
print("dane")

value=int(input('enter a integer value range 0...10 =' ))
if value<=0 and  value<=10:
 print("in range")
print( "done")


value=int(input('enter a integer value range 0...10 =' ))
if value>=0:
   if value<=10:
    print (value,"In Range")
   else:
    print (value,"In too Large")
else:
  print (value,"In too small")
print("dane")

a=int (input('enter a no-'))
if a<0:
    print("too small")
elif a==1:
    print('one')
elif a==2:
    print("two")
elif a==3:
    print("three")        
elif a==4:
    print("four ")        
elif a==5:
    print("five")        
else:
    print("too larg")

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


a=2
b=4
if a<b:
    print("true")
if a==b:
    print("not")
if a!=b:
    print("hi")
if a>b:
    print("me")
print('done')

num=int(input('enter a no-'))
if num==1:
    print('one')
elif num==2:
    print('two')
elif num==3:
    print('three')
elif num==4:
    print('four')
else:
    print('larg no')

value = int(input("Please enter an integer in the range 0...5: "))
answer = "not in range" # Default answer
if value == 0:
 answer = "zero"
elif value == 1:
 answer = "one"
elif value == 2:
 answer = "two"
elif value == 3:
 amswer = "three"
elif value == 4:
 answer = "four"
elif value == 5:
 answer = "five"
print("The number you entered was", answer)

print('enter a integer value-')
num1=int(input('enter a no-'))
num2=int(input('enter a no-'))
num3=int(input('enter a no-'))
num4=int(input('enter a no-'))
if num1>=num2 and num1>=num3 and num1>=num4 :
  max =num1
elif num2>=num1 and num2>=num3 and num2>=num4 :
  max=num2
elif num3>=num1 and num3>=num2 and num3>=num4 :
 max=num3
elif num4>=num1 and num4>=num2 and num4>=num3 :
  max = num4
print('the maxsimam nomber is-',max)


x=20
a=30
print(x!=20 and a!=30)
print(x==20 and a!=30)
print(x!=20 and a==30)
print(x==20 and a==30)

print(x!=20 or a!=30)
print(x==20 or a!=30)
print(x!=20 or a==30)
print(x==20 or a==30)

n=int( input( 'enter a np ='))
print("|",n,'| =',(-n if n<0 else n ), sep='')


n=int( input( 'enter a np ='))
print("|",n,'| =',(n if n>=0 else -n ), sep='')






























































































