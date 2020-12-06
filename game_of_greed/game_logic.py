import random
from collections import Counter

scoring = {
    "Straight 1- 6": 1500,
    "Three Pairs": 1500,
    ######
    "1x1": 100,
    "2x1": 200,
    "3x1": 1000,
    "4x1": 2000,
    "5x1": 3000,
    "6x1": 4000,
    ######
    "3x2": 200,
    "4x2": 400,
    "5x2": 600,
    "6x2": 800,
    ######
    "3x3": 300,
    "4x3": 600,
    "5x3": 900,
    "6x3": 1200,
    ######
    "3x4": 400,
    "4x4": 800,
    "5x4": 1200,
    "6x4": 1600,
    ######
    "1x5": 50,
    "2x5": 100,
    "3x5": 500,
    "4x5": 1000,
    "5x5": 1500,
    "6x5": 2000,
    ######
    "3x6": 600,
    "4x6": 1200,
    "5x6": 1800,
    "6x6": 2400
    }

#################################################################
class GameLogic:
    @staticmethod
    def roll_dice(times):
        return tuple(random.randint(1,6) for i in range (times))

    @staticmethod
    def calculate_score(dice):
        score = 0
        pairs = 0
        dice = Counter(dice)
        # if straight
        if len(dice) == 0:
            return(score)
        if (dice.most_common(1)[0][1] == 1) and len(dice) == 6:
            print("HI")
            score += scoring["Straight 1- 6"]
            return (score)
        # three pairs
        for value, count in dice.items():
            if count == 2:
                pairs += 1
        if pairs == 3:
            score += scoring["Three Pairs"]
            return(score)
        # 1 cases
        if dice[1] == 1:
            score += scoring["1x1"]
        if dice[1] == 2:
            score += scoring["2x1"]
        if dice[1] == 3:
            score += scoring["3x1"]
        if dice[1] == 4:
            score += scoring["4x1"]
        if dice[1] == 5:
            score += scoring["5x1"]
        if dice[1] == 6:
            score += scoring["6x1"]
        # 2 cases
        if dice[2] == 3:
            score += scoring["3x2"]
        if dice[2] == 4:
            score += scoring["4x2"]
        if dice[2] == 5:
            score += scoring["5x2"]
        if dice[2] == 6:
            score += scoring["6x2"]
        # 3 cases
        if dice[3] == 3:
            score += scoring["3x3"]
        if dice[3] == 4:
            score += scoring["4x3"]
        if dice[3] == 5:
            score += scoring["5x3"]
        if dice[3] == 6:
            score += scoring["6x3"]
        # 4 cases
        if dice[4] == 3:
            score += scoring["3x4"]
        if dice[4] == 4:
            score += scoring["4x4"]
        if dice[4] == 5:
            score += scoring["5x4"]
        if dice[4] == 6:
            score += scoring["6x4"]
        # 5 cases
        if dice[5] == 1:
            score += scoring["1x5"]
        if dice[5] == 2:
            score += scoring["2x5"]
        if dice[5] == 3:
            score += scoring["3x5"]
        if dice[5] == 4:
            score += scoring["4x5"]
        if dice[5] == 5:
            score += scoring["5x5"]
        if dice[5] == 6:
            score += scoring["6x5"]
        # 6 cases
        if dice[6] == 3:
            score += scoring["3x6"]
        if dice[6] == 4:
            score += scoring["4x6"]
        if dice[6] == 5:
            score += scoring["5x6"]
        if dice[6] == 6:
            score += scoring["6x6"]
        else:
            score += 0
        return(score)
#################################################################

class Banker:
    def __init__(self):
        self.shelved = 0 #round
        self.balance = 0 #total
    
    def shelf(self, score):
        self.shelved += score
        return(self.shelved)

    def bank (self):
        self.balance += self.shelved
        self.clear_shelf()
    def clear_shelf(self):
        self.shelved = 0

#################################################################
   
if __name__ == "__main__":
    game = GameLogic()
    dice = game.roll_dice(6)
    print (dice)
    print(game.calculate_score(dice))