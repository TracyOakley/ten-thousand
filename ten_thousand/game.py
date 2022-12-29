from ten_thousand.game_logic import GameLogic

round_ = 1
total_score = 0
unbanked = 0
dice_left = 6


def welcome():
    print("""Welcome to Ten Thousand
(y)es to play or (n)o to decline""")
    choice = input("> ")
    if choice == "y" or choice =="n":
        if choice == "y":
            display_dice_roll(6)
        if choice == "n":
            print("OK. Maybe another time")


def display_dice_roll(numOfDice):
    print(f"Starting round {round_}")
    print(f"Rolling {numOfDice} dice...")
    DiceTuple = GameLogic.roll_dice(numOfDice)
    DiceToDisplay = [str(val) for val in DiceTuple]
    print(f"*** {' '.join(DiceToDisplay)} ***")
    while True:
        print("Enter dice to keep, or (q)uit:")
        choice = input("> ")
        if choice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break
        elif int(choice) <= 666666 and int(choice) >= 1:
            handle_dice_to_keep(choice, DiceTuple)
            break


def handle_dice_to_keep(choice, current_roll):
    #accept a string of numbers and makes sure checks with current roll and outputs the score
    global dice_left
    dice_leftover = dice_left - len(choice)

    #need to implement the check**********************************

    tuple_to_score = []
    for num in choice:
        tuple_to_score.append(int(num))

    tuple_to_score = tuple(tuple_to_score)
    score_this_round = GameLogic.calculate_score(tuple_to_score)
    global unbanked
    unbanked += score_this_round
    print(f"You have {unbanked} unbanked points and {dice_leftover} dice remaining")

    while True:
        print("(r)oll again, (b)ank your points or (q)uit:")
        next_choice = input("> ")

        if next_choice == "r":
            dice_left = dice_leftover
            display_dice_roll(dice_leftover)
        elif next_choice == "b":
            handle_bank()
            break
        elif next_choice == "q":
            print(f"Thanks for playing. You earned {total_score} points")
            break


def handle_bank():
    global total_score
    global unbanked
    global round_
    global dice_left
    print(f"You banked {unbanked} in round {round_}")

    total_score += unbanked
    print(f"Total score is {total_score} points")
    unbanked = 0
    round_ += 1
    dice_left = 6

    display_dice_roll(dice_left)

if __name__ == '__main__':
    welcome()
