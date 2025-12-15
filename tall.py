import random
import time
import colorama

Antall = 0

while True:
    time.sleep(0.025)
    Antall += 1
    Randomtall = random.randint(1, 100000)
    if Randomtall == 1:
        print(f"{Randomtall}")
        print(f"You got the number 1, it took {Antall} tries!")
        break

    elif Randomtall >=2:
        print(f"{Randomtall} - {Antall}") 

        if Randomtall == 2:
            print(f"\033[31m{Randomtall} - {Antall} \033[0m")

    else: 
        continue