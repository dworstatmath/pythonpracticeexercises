import random
random_num=random.randint(0,100)
i=0
while True:
    guess=int(input("guess a number \n"))
    i+=1
    if guess<random_num:
        print("the number is higher")
    elif guess>random_num:
        print("the number is lower")
    else:
        print("you found the number in "+str(i)+" guesses!")
        break