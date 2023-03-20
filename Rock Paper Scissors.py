import random as r
def rps():
    CompChoice = ("Rock","Paper","Scissors")
    ValidInput = ("1","2","3")
    cwin = 0
    uwin = 0
    username = input("Enter Your Name : ")
    c = False

    while True:
        while c == False:
            points = input("Enter Maximum Number Of Points : ")
            if points.isdigit():
                maxp = int(points)
                c = True
                break
            else: 
                print("Please Enter Only Numbers")
            
        while True:
            comp = r.choice(CompChoice)
            user = input("Enter 1 : Rock\nEnter 2 : Paper\nEnter 3 : Scissors\n- ")
            if user in ValidInput:
                break
            else:
                print("Invalid Input Try Again : ")
                print("   ")

        if user == "1":
            print("  ")
            print("  ")
            print("------------------------------------------------------")
            print("You Chose Rock!")
            print("Computer Chose",comp)
            if comp == "Rock":
                print("Its A Tie")
                print("------------------------------------------------------")
                print("  ")
                print("  ")
            elif comp == "Paper":
                print("You Lost!")
                print("------------------------------------------------------")
                print("  ")
                print("  ")
                cwin += 1           
            elif comp == "Scissors":
                print("You Won!")
                print("------------------------------------------------------")
                print("  ")
                print("  ")
                uwin += 1
        elif user == "2":
            print("  ")
            print("  ")
            print("------------------------------------------------------")
            print("You Chose Paper!")
            print("Computer Chose",comp)
            if comp == "Paper":
                print("Its A Tie")
                print("------------------------------------------------------")
                print("  ")
                print("  ")
            elif comp == "Scissors":
                print("You Lost!")
                cwin += 1
                print("------------------------------------------------------")
                print("  ")
                print("  ")
            elif comp == "Rock":
                print("You Won!")
                uwin += 1
                print("------------------------------------------------------")
                print("  ")
                print("  ")

        elif user == "3":
            print("  ")
            print("  ")
            print("------------------------------------------------------")
            print("You Chose Scissors!")
            print("Computer Chose",comp)
            if comp == "Scissors":
                print("Its A Tie")
                print("------------------------------------------------------")
                print("  ")
                print("  ")
                print(" ")
            elif comp == "Rock":
                print("You Lost!")
                print("------------------------------------------------------")
                print("  ")
                print("  ")
                cwin += 1
                print(" ")
            elif comp == "Paper":
                print("You Won!")
                print("------------------------------------------------------")
                print("  ")
                print("  ")
                uwin += 1
                print(" ")
        print("------------------------------------------------------")
        print("Score\nComputer :- ",cwin,"\nYou :-",uwin)
        print("------------------------------------------------------")
        print("  ")
        print("  ")
        if uwin == maxp:
            print("------------------------------------------------------")
            print("The Winner Is...",username)
            print("------------------------------------------------------")
            print("Enter X to Exit")
            cwin = 0
            uwin = 0
            c = False
            i = input(" - ")
            print(" ")
            print(" ")
            if i == "X" or i == "x":
                cwin = 0
                uwin = 0
                c = False
                break
        if cwin == maxp:
            print("------------------------------------------------------")
            print("The Winner Is...Computer")
            print("------------------------------------------------------")
            print("Enter X to Exit")
            cwin = 0
            uwin = 0
            c = False
            i = input(" - ")
            print(" ")
            print(" ")
            if i == "X" or i == "x":
                cwin = 0
                uwin = 0
                c = False
                break

    
    
    
    
