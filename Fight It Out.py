import random as r
def fight():
    while True:
        NityaStats = ["Attack : 20-30","Health : 210","Accuracy : 90%"]
        Nitya = {"Attack":[20,30],"Health":210,"Accuracy":[1,1,1,1,0]}
        NHP = Nitya["Health"]

        MeetStats = ["Attack : 40-50","Health : 150","Accuracy : 60%"]
        Meet = {"Attack":[40,50],"Health":150,"Accuracy":[1,1,1,0,0]}
        MHP = Meet["Health"]

        AStats = ["Attack : 10-20","Health : 100","Accuracy : 50%"]
        Anashin = {"Attack":[10,20],"Health":100,"Accuracy":[1,1,1,0,0,0]}
        MHP = Anashin["Health"]


        print("character Stats - ")
        print(" ")
        print("----Nitya----")
        for i in NityaStats:
            print(i)
        print("----Meet-----")
        for i in MeetStats:
            print(i)
        print("---Anashin---")
        for i in AStats:
            print(i)
        print("-------------")

        HealP = [1,1,1,2]
        while True:
            User = input("Pick The Character You Want To Play With\n1 : Nitya\n2 : Meet\n3 : Anashin\n - ")
            if User != "1" and User != "2" and User != "3":
                print("Invalid Input! Please Try Again..")
            else:
                if User == "1":
                    print("You Picked : NITYA")
                    print("------------")
                    break
                if User == "2":
                    print("You Picked : MEET")
                    print("------------")
                    break
                if User == "3":
                    print("You Picked : ANASHIN")
                    print("------------")
                    break

        while True:
            Comp = input("Pick The CHarater You Want To Play Against\n1 : Nitya\n2 : Meet\n3 : Anashin\n -  ")
            if Comp != "1" and Comp != "2" and Comp != "3":
                print("Invalid Input! Please Try Again..")
            else:
                if Comp == "1":
                    print("Computer is : NITYA")
                    print("------------")
                    print("  ")
                    print("  ")
                    break
                if Comp == "2":
                    print("Computer is : MEET")
                    print("------------")
                    print("  ")
                    print("  ")            
                    break
                if Comp == "3":
                    print("Computer is : ANASHIN")
                    print("------------")
                    print("  ")
                    print("  ")
                    break


        if User == "1":
            UHP = Nitya["Health"]
        elif User == "2":
            UHP = Meet["Health"]
        elif User == "3":
            UHP = Anashin["Health"]


        if Comp == "1":
            CHP = Nitya["Health"]
        elif Comp == "2":
            CHP = Meet["Health"]
        elif Comp == "3":
            CHP = Anashin["Health"]
        


        while True:
            Nacc = r.choice(Nitya["Accuracy"])   
            ND = r.randint(Nitya["Attack"][0],Nitya["Attack"][1])

            Macc = r.choice(Meet["Accuracy"])   
            MD = r.randint(Meet["Attack"][0],Meet["Attack"][1])

            Aacc = r.choice(Anashin["Accuracy"])   
            AD = r.randint(Anashin["Attack"][0],Anashin["Attack"][1])

            if User == "1":
                Uacc = Nacc
                UD = ND
                U = "Nitya"

            elif User == "2":
                Uacc = Macc
                UD = MD
                U = "Meet"
            elif User == "3":
                Uacc = Aacc
                UD = AD
                U = "Anashin"


            if Comp == "1":
                Cacc = Nacc
                CD = ND
                C = "Nitya"

            elif Comp == "2":
                Cacc = Macc
                CD = MD
                C = "Meet"
            elif Comp == "3":
                Cacc = Aacc
                CD = AD
                C = "Anashin"


            print("Your Health : ",UHP)
            print(C,"'s Health : ",CHP)
            print("  ")
            print("  ")
            print("------------------------------------------------------")
            print("  ")
            print("  ")
            while True:
                c = input("Enter\n1 : To Attack\n2 : To Heal(20 Points)\n - ")
                print("  ")
                print("  ")
                print("------------------------------------------------------")
                if c != "1" and c != "2":
                    print("Invalid Input Try Again!..")
                else:
                    break
            if c == "1":
                if CHP > 0:
                    if Uacc == 1:
                        print("You Attacked And Caused..",UD,"Damage")
                        CHP -= UD
                    else:
                        print("You Missed..")

            elif c == "2":
                print("You Healed 20 Points")
                UHP += 20
            else:
                print("Invalid Input Try Again+")
            if CHP <=0:
                print(U,"Killed..",C)
                print(C,"Died You Won..")
                print("------------------------------------------------------")
                print("  ")
                print("  ")
                break



            c1 = r.choice(HealP)
            if c1 == 1:
                if UHP > 0:
                    if Cacc == 1:
                        print(C,"Attacked And Caused..",CD,"Damage")
                        UHP -= CD
                        print("------------------------------------------------------")
                        print("  ")
                        print("  ")
                    else:
                        print(C," Missed..")
                        print("------------------------------------------------------")
                        print("  ")
                        print("  ")


            elif c1 == 2:
                print(C,"Healed 20 Points")
                CHP += 20
                print("------------------------------------------------------")
                print("  ")
                print("  ")
            if UHP <=0:
                print(U,"Died You Lost..")
                print(C,"Killed..",U)
                print("------------------------------------------------------")
                print("  ")
                print("  ")
                break

        print("Thanks For Playing!\nEnter X to Exit Else Play Again")
        ex = input(" - ")
        print("x------------------------------------------------------------------x")
        if ex == "X" or ex == "x":
            break

fight()