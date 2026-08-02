import random

target = random.randint(1,100)

while True:
    usernum = input("Guess the number or Quit(Q):")
    if (usernum == "Q"):
        break
    usernum = int(usernum)
    if (usernum == target):
        print("Success: You guessed the number!!!")
        break
    elif (usernum < target):
        print("The guessed number is too small. Take a bigger guess...")
    else:
        print("The gussed number is too large. Take a smaller guess...")


print("-----------GAME OVER-----------")
