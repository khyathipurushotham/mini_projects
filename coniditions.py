#conditions
#if statement
a=int(input("enter the number:"))
b=int(input("ënter the number:"))
if a>b:
    print("a is greater")
print("thank you for using the program")
#elif statement
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if a>b:
    print("a is greater")
elif a<b:
    print("b is greater than b")
else:
    print("a and b are equal")
#else statement
a=int(input("enter the number:"))
b=int(input("enter the number:"))
if a>b:
    print("a is greater")
else:
    print("b is greater")
#nested if
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a>=b:
    if a>=c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>=c:
        print("b is greater")

    else:
        print("c is greater")
print("finished")
#while
number=int(input("enter the number"))
while number <200:
    print(number)
    number =number*2
#for
for x in range(1,6):
    print (x)
print("squared is",x*x)
#range
for x in range(5,0,-1):
    print (x)
print("blastoff")
#for loop
for somevariable in range (10):
    print(somevariable)
print("printing first 10 natural numbers:")
for somvariable in range (10):
    print(somevariable+1)
print("printing first 10 natural numbers:")
for somevariable in range (10):
    print(somvariable*2)
#range has two numbers
for somevariable in range (1,11):
    print(somevariable)
print("printing odd number below 10:")
for somevariable in range (1,10,2):
    print(somevariable)
print("printing first 10 natural numbers")
startno = 0
while startno <10:
    startno=startno+1
    print(startno)
#nested loop
    for i in range(5):
        for j in range (5):
            print("I =",i,"J =" ,j)


    
