from random import randint
print("Welcome to the Game")
print("Do You Want Tutorial? (press y if you want)")
k = ("1","2","3","4","5","6","7","8","9","0")
j = (1,2,3,4,5)
if input()=='y':
    print("Tutorial : Computer Generates a random number \nYou Chose a number between 1 to 5 to subtract\nIf you make the number 1 you win\nNow Go and Play!")
x = randint(30,60)
r = 0
while x > 0:
    r = r +1   
    print("Round",r)
    print("The Number Is",x)
    print("Your Turn")
    print("Enter a number Between from 1 to 5")
    a = (input())
    if a in k:
        a = int(a)
    while a not in k:
        print("Please Enter a Number not letters")
        a = input("Wrong Value, Enter value From 1 to 5: ")
        if a in k:
            a = int(a)
        if a in j:
            break
    a = int(a)
    while a >5 or a<1:
        a = input("Wrong Value, Enter value From 1 to 5: ")
        
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


    
    
    
    
