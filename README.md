Part1 PR: https://github.com/batoolmalkawii/game-of-greed/pull/3

Part2 PR: https://github.com/batoolmalkawii/game-of-greed/pull/4
Part3 PR: https://github.com/batoolmalkawii/game-of-greed/pull/5

* Game of Greed is a Dice game, aka _Farkle_. In part1, we implemented the following:

**GameLogic** class:

`calculate_score`: returns the round score according the _game rules_.

`roll_dice`: returns a tuple with random values between 1 and 6.

**Banker** class:
                
`shelf`: tracks unbanked points 

`bank`: adds unbanked points to total and return the deposited amount.

`clear_shelf`: removes any unbanked points, resetting to zero.

* **Game Rules**:

        # 1 cases
        # if dice[1] == 1:
        #     score += scoring["1x1"]
        # if dice[1] == 2:
        #     score += scoring["2x1"]
        # if dice[1] == 3:
        #     score += scoring["3x1"]
        # if dice[1] == 4:
        #     score += scoring["4x1"]
        # if dice[1] == 5:
        #     score += scoring["5x1"]
        # if dice[1] == 6:
        #     score += scoring["6x1"]
        # # 2 cases
        # if dice[2] == 3:
        #     score += scoring["3x2"]
        # if dice[2] == 4:
        #     score += scoring["4x2"]
        # if dice[2] == 5:
        #     score += scoring["5x2"]
        # if dice[2] == 6:
        #     score += scoring["6x2"]
        # # 3 cases
        # if dice[3] == 3:
        #     score += scoring["3x3"]
        # if dice[3] == 4:
        #     score += scoring["4x3"]
        # if dice[3] == 5:
        #     score += scoring["5x3"]
        # if dice[3] == 6:
        #     score += scoring["6x3"]
        # # 4 cases
        # if dice[4] == 3:
        #     score += scoring["3x4"]
        # if dice[4] == 4:
        #     score += scoring["4x4"]
        # if dice[4] == 5:
        #     score += scoring["5x4"]
        # if dice[4] == 6:
        #     score += scoring["6x4"]
        # # 5 cases
        # if dice[5] == 1:
        #     score += scoring["1x5"]
        # if dice[5] == 2:
        #     score += scoring["2x5"]
        # if dice[5] == 3:
        #     score += scoring["3x5"]
        # if dice[5] == 4:
        #     score += scoring["4x5"]
        # if dice[5] == 5:
        #     score += scoring["5x5"]
        # if dice[5] == 6:
        #     score += scoring["6x5"]
        # # 6 cases
        # if dice[6] == 3:
        #     score += scoring["3x6"]
        # if dice[6] == 4:
        #     score += scoring["4x6"]
        # if dice[6] == 5:
        #     score += scoring["5x6"]
        # if dice[6] == 6:
        #     score += scoring["6x6"]
        # else:
        #     score += 0
        # return(score)
