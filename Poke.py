import random

Number1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
Number2 = ["♡", "♤", "♢", "♧"]

#-------------#
# Create Deck #
#-------------#
def Deck():
    temp = []
    for a in Number1:
        for b in Number2:
            temp.append(f"{a}{b}")
    return temp
GameDeck = Deck()

#Shuffle Deck
random.shuffle(GameDeck)

#Def (Draw Two Cards from Deck)
def CurrentGameDeck(GameDeck):
    return GameDeck.pop()

#Draw Two Cards from Deck
MyHand = []
for _ in range(2):
    MyHand.append(CurrentGameDeck(GameDeck))


print(MyHand)
print(GameDeck)