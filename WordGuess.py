import random 
print("Select Difficulty : \n Press Any Key : East : 3-4 letters \n Press 2 : Medium : 5 letters \n Press 3 : Hard : 6 lettes \n Press 4 : Insane : 7 letters")
x = input()
l = 4
if x == '2':
    l = 5
elif x == '3':
    l = 6
elif x == '4':
    l = 7
lines = open("words.txt").read() 
line = lines[0:] 
words = line.split() 
while True:
    w = random.choice(words)
    if len(w) == l:
        break
li = list(w)
n = 0
while True:
    n += 1
    g = input("Guess a Letter : ")
    while len(g) != 1:
        print("Please Enter only One Letter")
        z = input("Enter Again : ")
        g = z
        if len(g) == 1:
            break
    if g in li:
        dex =li.index(g)
        print("You Guessed Correctly")
        print(g,"Is Present In The Word at position",dex+1,"from left")
    else:
        print("Wrong Guess",g,"Is not Present In")
    q = input("Guess The Word : ")
    if q == w:
        print("You Guessed The Word! in just",n,"rounds" )
        break
    else:
        print("Wrong Word")




    

