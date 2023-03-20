import random as r
def battleships():
    print("There are 3 Enemy Ships Hidden You Have To Find Them and Destroy them Before Your Missiles Run Out")
    Hiddenmap = ([" ","A","B","C","D","E"],[1,"O","O","O","O","O","O"],[2,"O","O","O","O","O","O"],[3,"O","O","O","O","O","O"],[4,"O","O","O","O","O","O"],[5,"O","O","O","O","O","O"])
    Displaymap = ([" ","A","B","C","D","E"],[1,"O","O","O","O","O","O"],[2,"O","O","O","O","O","O"],[3,"O","O","O","O","O","O"],[4,"O","O","O","O","O","O"],[5,"O","O","O","O","O","O"])


    d = {"A":1,"B":2,"C":3,"D":4,"E":5}
    t = ["1","2","3","4","5"]
    print("  ")
    print("  ")
    print("------------------------------------------------------")
    for i in Hiddenmap: 
        print(i[0],i[1],i[2],i[3],i[4],i[5])
    print("------------------------------------------------------")
    print("  ")
    print("  ")
    


    for i in range(3):
        col = r.randint(1,5)
        row = r.randint(1,5)
        Hiddenmap[col][row] = "x"

    '''for i in Hiddenmap: 
        print(i[0],i[1],i[2],i[3],i[4],i[5])'''

    shipcount = 0
    turns = 15
    while True:
        while True:
            trow = input("Enter Row (AB...)")
            tcol = input("Enter Column (12...)")

            if trow.upper() in "ABCDE" and trow.isalpha() and tcol in t:
                ucol = int(tcol)
                urow = trow.upper()
                if Displaymap[ucol][d[urow]] == "-":
                    print("You Already Checked That Place!")
                else:
                    break

            else:
                print("Invalid Input Try Again!..")


        if Hiddenmap[ucol][d[urow]] == "x":
            Displaymap[ucol][d[urow]] = "x"
            print("Hit! You Destroyed a Ship")
            shipcount += 1
            turns -= 1
            print("You Have",turns,"Missiles Remaining!")
            print("  ")
            print("  ")
            print("------------------------------------------------------")
            for i in Displaymap: 
                print(i[0],i[1],i[2],i[3],i[4],i[5])
            print("------------------------------------------------------")
            print("  ")
            print("  ")
            

        else:
            Displaymap[ucol][d[urow]] = "-"
            print("Miss! You Missed")
            turns -= 1
            print("You Have",turns,"Missiles Remaining!")
            print("  ")
            print("  ")
            print("------------------------------------------------------")
            for i in Displaymap: 
                print(i[0],i[1],i[2],i[3],i[4],i[5])
            print("------------------------------------------------------")
            print("  ")
            print("  ")


        if shipcount == 3:
            print("You Destroyed All The Ships, You Won !!")
            c = input("Enter X To Exit")
            if c == "X" or c == "x":
                break
            else:
                battleships()
        if turns == 0:
            print("You Used All Your Missiles, You Lost !!")
            print("Ships Were Here - ")
            print("  ")
            print("  ")
            print("------------------------------------------------------")
            for i in Hiddenmap: 
                print(i[0],i[1],i[2],i[3],i[4],i[5])
            print("------------------------------------------------------")
            print("  ")
            print("  ")
            c = input("Enter X To Exit")
            if c == "X" or c == "x":
                break
            else:
                battleships()

#main  
battleships()