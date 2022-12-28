import random
from collections import Counter
class GameLogic:

    @staticmethod
    def calculate_score(dice_roll):
        # accepts a tuple of the dice from roll dice()
        dice_counter = Counter(dice_roll)
        most_common_dice = dice_counter.most_common()
        score = 0

        for dice in most_common_dice:
            if dice[1] == 3 and dice[0] != 1:
                score += dice[0]*100
            if dice[1] == 3 and dice[0] == 1:
                score += 1000

            if dice[1] == 4 and dice[0] != 1:
                score += dice[0]*100 * 2
            if dice[1] == 4 and dice[0] == 1:
                score += 1000 * 2

            if dice[1] == 5 and dice[0] != 1:
                score += dice[0]*100 * 3
            if dice[1] == 5 and dice[0] == 1:
                score += 1000 * 3

            if dice[1] == 6 and dice[0] != 1:
                score += dice[0]*100 * 4
            if dice[1] == 6 and dice[0] == 1:
                score += 1000 * 4

        if len(most_common_dice) == 6:
            score += 1500
        elif len(most_common_dice) == 3:
            if most_common_dice[0][1] == 2 and most_common_dice[1][1] == 2 and most_common_dice[2][1] == 2:
                score += 1500
        else:
            for dice in most_common_dice:
                if dice[1] == 2:
                    if dice[0] == 5:
                        score += 100
                    if dice[0] == 1:
                        score += 200
                if dice[1] == 1:
                    if dice[0] == 5:
                        score += 50
                    if dice[0] == 1:
                        score += 100

        return score








        # outputs an integer of the roll's score according to rule of games


    @staticmethod
    def roll_dice(num_dice):
        """
        INPUT >> Integer - a number between 1 and 6
        OUTPUT >> Tuple - with length of input with numbers between 1 and 6
        """

        dice_list = []

        for dice in range(num_dice):
            dice_list.append(random.randint(1,6))

        return tuple(dice_list)
