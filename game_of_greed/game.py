from game_of_greed.game_logic import GameLogic, Banker
#from game_logic import GameLogic, Banker

""" instance of banker to store score """
banker = Banker()

""" helper functions """
########################
def RepresentsInt(s):
    """
    checks if the user input represents a string 
    - input: str
    - output: true if int, false if not int
    """
    try: 
        int_s = int(s)
        return True
    except ValueError:
        return False

def does_exist(dice, input):
    """
    checks if the values inputted by the user exist in the dice roll.
    - input: generated dice, user input.
    - output: true if user input in dice, false if not.
    """
    dice = list(dice)
    if len(input) > len(dice):
        return False
    for val in input:
        if int(val) not in dice:
            return False
        dice.remove(int(val))
    return True

def get_remaining_dice(dice, input):
    """
    gets the number of remaining dice to use in the next roll.
    - input: dice, input.
    - output: number of remaining dice.
    """
    return (len(dice) - len(input))

def str_to_tuple(str):
    """
    converts strings to tuples
    - input: string
    - output: tuple of characters of that string
    """
    res = []
    for char in str:
        res.append(int(char))
    res = tuple(res)
    return(res)

class Game:
    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice
        self.round = 1

    def print_roll(self, roll):
        """
        prints the dice roll as a string separated by commas.
        - input: (1, 2, 3, 4)
        - output: 1,2,3,4
        """
        print(','.join([str(i) for i in roll]))

    def get_dice_to_keep (self):
        """
        takes the number of dices to keep as an input from the user.
        - input: None
        - output: dice
        """
        return(input('Enter dice to keep (no spaces), or (q)uit: '))

    def quit_game(self):
        print(f'Total score is {banker.balance} points')
        print(f'Thanks for playing. You earned {banker.balance} points')
        banker.balance = 0
        banker.shelved = 0

    def is_zilch(self, roll):
        if GameLogic.calculate_score(roll) == 0:
            return True
        else:
            return False
    
    def take_action(self, roll, dice_to_keep):
        remaining_dice = get_remaining_dice(roll, dice_to_keep)
        dice_to_keep = str_to_tuple(dice_to_keep)
        to_bank = banker.shelf(GameLogic.calculate_score(dice_to_keep))
        print(f"You have {to_bank} unbanked points and {remaining_dice} dice remaining")
        roll_bank_quit = input ("(r)oll again, (b)ank your points or (q)uit ")
        if (roll_bank_quit == 'b'):
            self.banking(to_bank)
            self.round += 1
            self.new_round()
        elif (roll_bank_quit == 'r'):
            if remaining_dice == 0:
                remaining_dice = 6
            self.repeat_round(remaining_dice)
        elif (roll_bank_quit == 'q'):
            self.quit_game()


    def banking(self, to_bank):
        print(f"You banked {to_bank} points in round {self.round}")
        balance = banker.bank()
        print(f"Total score is {balance} points")

    def clear_round_after_zilch(self):
        print(f"You banked 0 points in round {self.round}")
        print(f"Total score is {banker.balance} points")




    
    def new_round(self):
        print(f'Starting round {self.round}')
        self.start_round(6)
    
    def repeat_round(self, remaining_dice):
        self.start_round(remaining_dice)
        
    def start_round(self, remaining_dice):
        print(f'Rolling {remaining_dice} dice...')
        roll = self.roller(remaining_dice)
        self.print_roll(roll)
        if(self.is_zilch(roll)):
            print("Zilch!!! Round over")
            self.clear_round_after_zilch()
            self.round += 1
            self.new_round()
        else:
            dice_to_keep = self.get_dice_to_keep()
            is_int = RepresentsInt(dice_to_keep)
            if dice_to_keep == 'q':
                self.quit_game() 
            else:
                #check if integer
                while(is_int == False):
                    dice_to_keep = self.get_dice_to_keep()
                    is_int = RepresentsInt(dice_to_keep)
                #check if all values are in dice
                exists = does_exist(roll, dice_to_keep)
                while(exists == False):
                    print("Cheater!!! Or possibly made a typo...")
                    self.print_roll(roll)
                    self.get_dice_to_keep()
                    exists = does_exist(roll, dice_to_keep)
                self.take_action(roll, dice_to_keep)

    def play(self):
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')
        elif res == 'y':           
            self.new_round()
    


if __name__ == '__main__':
    game = Game()
    game.play()
