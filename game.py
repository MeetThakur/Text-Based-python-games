from random import randint
print("Welcome to the Game")
print("Do You How To play? (y/n)")
if input()=='n':
    print("Tutorial : Computer Generates a random number \nYou Chose a number between 1 to 5 to subtract\nIf you make the number 1 you win\nNow Go and Play!")
x = randint(30,60)
r = 0
while x > 0:
    r = r +1   
    print("Round",r)
    print("The Number Is",x)
    print("Your Turn")
    print("Enter a number Between from 1 to 5")
    a = int(input())
    while a > 5 or a <=0:
        print("Please Enter a Appropriate Value")
        a = int(input("Wrong Value, Enter value From 1 to 5: "))
        if a <= 5 and a >=0:
            break
    print("Your Choose : ",a)
    x = x - a
    if x == 1:
        print("You Won!!")
        print("Thanks For Playing")
        print("Enter 0 to exit")
        if input()==0:
            break
    print("Now the Number is",x)
    b = randint(1,5)
    print("Computer's turn\ncomputer Chose : ",b)
    x = x - b
    print("Now the Number is",x)
    if x <= 1:
        print("Computer Won")
        print("Thanks For Playing")
        print("Enter 0 to exit")
        if input()==0:
            break


    
    
    
    