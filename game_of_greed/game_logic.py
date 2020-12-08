import random
from collections import Counter

scoring = {
    "Straight 1- 6": 1500,
    "Three Pairs": 1500,
    # 1 category
    (1, 1): 100,
    (1, 2): 200,
    (1, 3): 1000,
    (1, 4): 2000,
    (1, 5): 3000,
    (1, 6): 4000,
    # 2 category
    (2, 3): 200,
    (2, 4): 400,
    (2, 5): 600,
    (2, 6): 800,
    # 3 category
    (3, 3): 300,
    (3, 4): 600,
    (3, 5): 900,
    (3, 6): 1200,
    # 4 category
    (4, 3): 400,
    (4, 4): 800,
    (4, 5): 1200,
    (4, 6): 1600,
    # 5 category
    (5, 1): 50,
    (5, 2): 100,
    (5, 3): 500,
    (5, 4): 1000,
    (5, 5): 1500,
    (5, 6): 2000,
    # 6 category
    (6, 3): 600,
    (6, 4): 1200,
    (6, 5): 1800,
    (6, 6): 2400,
    }

#################################################################
class GameLogic:
    @staticmethod
    def roll_dice(times=6):
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
        # [1-6 cases]
        else:
            dice_length = len(dice.most_common())
        for i in range(dice_length):
            score += get_score((Counter(dice).most_common()[i]))
        return score


def get_score(dice_value):
    try:
        scoring[dice_value]
    except:
        return 0
    else:
        return scoring[dice_value]

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
        return self.balance

    def clear_shelf(self):
        self.shelved = 0

#################################################################
   
if __name__ == "__main__":
    game = GameLogic()
    dice = game.roll_dice(6)
    print (dice)
    print(game.calculate_score(dice))