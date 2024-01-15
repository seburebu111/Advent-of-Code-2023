from typing import List

# hand types can be distinguished by the product of all the non-null the number of 
# appearances of each card and the number of different cards
# 7. five of a kind: 5, 1
# 6. four of a kind: 4, 2
# 5. full house: 6, 2
# 4. three of a kind: 3, 3
# 3. two pair: 4, 3
# 2. one pair: 2, 4
# 1. high card: 1, 5
# the number of jokers will be added to the highest card count

map = {"J":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "Q":11, "K":12, "A":13}

def getType(hand:str) -> List[int]:    
    # create an array of appearances of each card, starting from 0
    app = [0]*13
    for card in hand:
        app[map[card]-1] += 1
    cardProd = 1
    cardCount = 0
        
    if app[0] == 5:
        return 7    # there are 5 jokers
    # finding where to add the jokers
    maxx, maxi = app[2], 2
    for i in range(1,13):
        if app[i] > maxx:
            maxx = app[i]
            maxi = i
    app[maxi] += app[0]  # add the jokers to the highest card count
    
    # differing between the types, as mentioned above, but without the jokers
    for i in range(1,13):
        if app[i] != 0:
            cardCount += 1
            cardProd *= app[i]
    if cardProd == 1:
        return 1
    elif cardProd == 2:
        return 2
    elif cardProd == 4:
        if cardCount == 3:
            return 3
        else:
            return 6
    elif cardProd == 3:
        return 4
    elif cardProd == 6:
        return 5
    return 7

def getCardsAsInts(hand:str) -> List[int]:    # create an array of the cards in the hand
    cards = []
    for card in hand:
        cards.append(map[card])
    return cards


# opne the input file and convert its lines into a List[str]
file = open("input.txt")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

# an array of the form:
# [(rankDefiner, firstCardRank, value), (rankDefiner, value), ...]
hands = []
for i in range(len(lines)):
    line = lines[i]
    hands.append((getType(line.split(" ")[0]), getCardsAsInts(line.split(" ")[0]), int(line.split(" ")[1])))

hands.sort()    # sort the hands by their rankDefiner
winnings = 0
for i in range(len(hands)):
    winnings += hands[i][2] * (i+1)
print(winnings)
    
        
