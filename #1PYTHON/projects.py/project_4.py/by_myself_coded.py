#  Guess game # 1 project written all by myself!
import random
print("Computer has randomly chosen a number! Now it is your turn")
print("Guess a number from 0 to 5")
rn = random.randint(0,5) # also includes (a,b) b
i = 0
while True:
    try:
        user = int(input("What is your guess?\n"))
        if user < rn:
            print("Try a little higher")
            i+= 1
                
        elif user > rn :
            print("Try a little lower")
            i+=1
                
        elif user == rn:
            print("CONGRATULATIONS! YOU HAVE GUESSED IT CORRECT\n")
            i+=1
                
            print(f"TOTAL NUMBER OF GUESSES ARE {i}")
        if user == rn:
            break
    except Exception as e:
        print(f"Your input is invalid {e}")