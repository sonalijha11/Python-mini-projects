#Random passward generator
import random
import string

lenght = int(input("Enter the lenght of passward (4-12):"))


characters = string.ascii_letters + string.digits

passward = ""

if lenght < 4 or lenght > 12:
    print("Invalid lenght of passward. Please select between (4 - 12)")

else:
    for value in range(lenght):
        passward += random.choice(characters)

    print("Random passward:", passward)

