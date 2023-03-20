def guessword():
    while True:
        print("Select Difficulty : \n Enter 1 : 3 letters \n Enter 2 : 4 letters \n Enter 3 : 5 lettes \n Enter 4 : 6 letters \n Enter 5 : 7 letters \n Enter 6 : 8 Letters" )
        choice = input(" - ")
        print("------------------------------------------------------")
        print("  ")
        print("  ")
        validinput = ('1','2','3','4','5','6')
        if choice not in validinput:
            print("Please Enter Appropriate Value!")
        else:
            break

    if choice == '1':
        difficulty = 3
    if choice == '2':
        difficulty = 4
    elif choice == '3':
        difficulty = 5
    elif choice == '4':
        difficulty = 6
    elif choice == '5':
        difficulty = 7
    elif choice == '6':
        difficulty = 8

    guesslist = []
    for i in range(difficulty):
        guesslist.append("_")

    wronglist = []
    temp = 0

    lines = open("words.txt").read() 
    line = lines[0:] 
    words = line.split() 

    while True:
        word = r.choice(words)
        word = word.upper()
        if len(word) == difficulty:
            break

    wordlist = list(word)
    rounds = 0
    while True:      
        guess1 = input("Guess a Letter: ")
        guess=guess1.upper()
        
        while guess.isalpha() == False:
            print("Please Enter only Alphabets")
            temp = input("Enter Again : ")
            guess = temp.upper()
            if guess.isalpha():
                break
            
        while len(guess) != 1:
            print("Please Enter only One Letter")
            temp = input("Enter Again : ")
            guess = temp.upper()
            if len(guess) == 1:
                break
               
        if guess in wordlist:
            n = 0
            print("  ")
            print("------------------------------------------------------")
            print("You Guessed Correctly")
            print(guess,"Is Present In The Word")
            print("------------------------------------------------------")
            print("  ")
            for i in wordlist:
                if i == guess:
                    guesslist[n] = i 
                n+=1
            for i in guesslist:
                print(i,end=" ")
            print()
            print("   ")
        else:
            print("  ")
            print("------------------------------------------------------")            
            print("Wrong Guess",guess,"Is not Present In")
            print("------------------------------------------------------")
            print("  ")
            temp = 1
            if guess not in wronglist:
                wronglist.append(guess)
        if temp != 0:
            print("These Letters are not Present in The Word")
            print("------------------------------------------------------")
            for i in wronglist:
                print(i,end=" ")
            print()
            print("------------------------------------------------------")
            print("  ")

        guessword1 = input("Guess The Word or Enter 0 Give Up: ")
        guessword = guessword1.upper()

        if guessword == word:
            print("Correct You Guessed The Word! in ",rounds,"rounds\nThank You For Playing" )
            print("  ")
            n = input("Enter X to Exit : ")
            if n == "X" or n == "x":
                break
            else:
                guessword()
        elif guessword == "0":
            print("The Word Was : ",word," :\nThank You For Playing")
            print(" ")
            n = input("Enter X to Exit : ")
            if n == "X" or n == "x":
                break
            else:
                guessword()
        else:
            print("Wrong Word")
            print("  ")


#main
guessword()




    

