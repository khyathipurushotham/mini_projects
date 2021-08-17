#break
while True:
    s=input("enter something")
    if s.lower()=='quite':
        break
    print("length of the given text is",len(s))
print("goodjob")
#continue
while True:
    s=input("enter something")
    if len(s)<3:
        print("too small text")
        continue
    if s.lower()=='quit':
        break
    print("length of the given string is",len(s))
print("done")
#break continue exit
students=0
while True:
    sum=0
    students+=1
    nsubjects=int(input("enter number of subjects:"))
    if nsubjects <=0:
        print("invalid entry")
        continue
    for i in range(1,nsubjects+1):
        marks=float(input("enter the marks: {}".format(i)))
        sum+=marks
    print("total marks obtained is{}",sum)
    avg=sum/nsubjects
    if avg >70:
        print("you got grade A")
        print("great work")
    elif avg <=50:
        print("you got grade B")
        print("work hard")
    else:
        print("you failed")
        print("work hard next time")
        choice =input("press E to end your program,press y to continue running and another key to exit!!")
        if choice.lower()=="y":
            pass
        elif choice.lower()=="e":
            break
        else:
            exit()
    print("thank you for using the program {}",format(students))
    exit()

        
    
