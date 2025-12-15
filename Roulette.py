import random
import time

Amount = 0
Balance = 10000

Number = ["00 - Green", "0 - Green", "1 - Red", "2 - Black", "3 - Red", "4 - Black", 
        "5 - Red", "6 - Black", "7 - Red", "8 - Black", "9 - Red", "10 - Black",
        "11 - Black", "12 - Red", "13 - Black", "14 - Red", "15 - Black", 
        "16 - Red", "17 - Black", "18 - Red", "19 - Red", "20 - Black",
        "21 - Red", "22 - Black", "23 - Red", "24 - Black", "25 - Red", 
        "26 - Black", "27 - Red", "28 - Black", "29 - Black", "30 - Red",
        "31 Black", "32 - Red", "33 - Black", "34 - Red", "35 - Black", "36 - Red"]

Red = ["1 - Red", "3 - Red", "5 - Red", "7 - Red", "9 - Red", "12 - Red", "14 - Red", "16 - Red", 
       "18 - Red", "19 - Red", "21 - Red", "23 - Red", "25 - Red", "27 - Red", "30 - Red", 
       "32 - Red", "34 - Red", "36 - Red"]
Black = ["2 - Black", "4 - Black", "6 - Black", "8 - Black", "10 - Black", "11 - Black", "13 - Black", 
        "15 - Black", "17 - Black", "20 - Black", "22 - Black", "24 - Black", "26 - Black", "28 - Black", 
        "29 - Black", "31 - Black", "33 - Black", "35 - Black"]
Green = ["0 - Green", "00 - Green"]

#------------------------#
#|      Spinning        |#
#------------------------#
def Spinning():
    print("Spinning the wheel...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("The ball landed on:", WheelSpin[0])

#------------------------#
#| Welcome to Roulette! |#
#------------------------#
def Welcome():
    global Amount, Bet
    print("Welcome to Roulette!")
    print("-----------------------")
    print("Place your bet on Red, Black, or Green, ")
    print("You can also bet on Odd or Even numbers, ")
    Bet = input("Or you could try to guess the exact number (0-36, 00) \nRed or Black/Number (0-36, 00)/Odd or Even: ")
    Bet = Bet.strip().lower()
    Amount = input("Enter the amount you want to bet: $")

#------------------------#
#|     Play Again       |#
#------------------------#
def PlayAgain():
    global Number
    print("Do you want to play again? (yes/no)")
    yesorno = input().lower().strip()
    if yesorno == 'yes':
        random.shuffle(Number)
    elif yesorno == 'no':
        print("Thanks for playing!")
        exit()

#------------------------#
#|       Betting        |#
#------------------------#
def Betting():
    if Bet == 'red':
        if WheelSpin[0] in Red:
            print(f"You win! +{Amount}")
            print(f"Your new balance is: ${Balance + int(Amount)}")

    elif Bet == 'black':
        if WheelSpin[0] in Black:
            print(f"You win! +{Amount}")
            print(f"Your new balance is: ${Balance + int(Amount)}")

    elif Bet == 'green':
        if WheelSpin[0] in Green:
            print(f"You win! +{Amount * 14}")
            print(f"Your new balance is: ${Balance + int(Amount * 14)}")

    elif Bet == 'odd':
        if (WheelSpin[0] & 1) != 0:
            print(f"You win! +{Amount}")
            print(f"Your new balance is: ${Balance + int(Amount)}")

    elif Bet == 'even':
        if (WheelSpin[0] & 1) == 0:
            print(f"You win! +{Amount}")
            print(f"Your new balance is: ${Balance + int(Amount)}")
    
    elif Bet in WheelSpin[0]:
        print(f"You win! +{Amount * 36}")
        print(f"Your new balance is: ${Balance + int(Amount * 36)}")


#------------------------#
#|       Roulette       |#
#------------------------#
while True:
    random.shuffle(Number)

    def SpinWheel(Number):
        return Number.pop()

    WheelSpin = []
    for _ in range(1):
        WheelSpin.append(SpinWheel(Number))
    Welcome()
    Betting()
    PlayAgain()
    continue

