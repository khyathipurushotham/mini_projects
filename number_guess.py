import random
print("hey welcome!")
k=input("are you intrested to play this game?" )
if k.lower()!="yes":
    quit()
else:
    print("let's play")
top_of_range=input("enter a number:")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
elif top_of_range<=0:
    print("type a number greater than 0")
else:
    print("enter number next time")
    quit()
random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses +=1
    user_guess=input("enter your guess")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    if user_guess == random_number:
        print("you got number correct!")
        break
    elif user_guess>random_number:
        print("you were above the number!")
    else:
        print("you were below the number!!!")
print("you got it in",guesses,"guesses")

    
    
