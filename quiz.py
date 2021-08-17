name=str(input("enter your name:" ))
print("welcome !"+name)
playing =input("are u intrested to play my quiz!!!" )
if playing.lower() != "yes":
    quit()
else:
    print("shall we begin")
    score = 0
answer =input("What element does 'O' represent on the periodic table?" )
if answer.lower()=="oxygen":
    print("correct")
    score +=1
else:
    print("incorrect")
answer=input("what is the fullform of cpu" )
if answer.lower()=="central processing unit":
    print("correct")
    score +=1
else:
    print("incorrect")
answer=input("What element does 'na' represent on the periodic table?" )
if answer.lower()=="sodium":
    print("correct")
    score +=1
else:
    print("incorrect")
answer=input("name a language of computer starts with p?" )
if answer.lower()=="python":
    print("correct")
    score += 1
else:
    print("incorrect")
print(score)
print("your done with the quiz")
print("you got"+str(score)+"quetion correct")
print("your average was"+str((score/4)*100)+"correct!")
print("well done many more to come your way !! have a great day")
e=input("press any k to exit")
if e == "k":
    quit()






                     
