# =========>  DICE GAME
# By Mohamed Moetaz Boughalmi

import random


# function to get Players names
def names():
    print("           ****PLEASE THE PLAYERS MUST REPRESENT THEMSELVES TO START**** ")
    print("            ____________________________________________________________  ")
    p1_name = input("Player 1 name: ")
    p2_name = input("Player 2 name: ")
    while (p1_name == "" or p2_name == ""):
        print("Both players must print their names!   THANK YOU")
        p1_name = input("Player 1 name: ")
        p2_name = input("Player 2 name: ")
    return p1_name, p2_name  # Returning names
    '''p1 stands for Player 1 & p2 stands for Player2'''


# function returning random numbers
def random_num():
    return random.randint(1, 6)  # getting random numbers when rolling the dice


# function play: In this function we'll include all game conditions
def play():
    # getting the names from the function above
    p1_name, p2_name = names()

    greeting = f'''                              Welcome {p1_name}
                              Welcome {p2_name}
                    The One who reach 50 first win the game   
                                 READY UP!
                            _____________________
                            **** Let's START ... ****'''
    # adding the greeting part.
    print(greeting)

    # Using 2 variables to stock players score
    p1_score = 0
    p2_score = 0

    inter1 = 0  # intermediate variable to reset the score to last number smaller than the required number
    inter2 = 0  # intermediate variable 2

    while (p1_score != 50 and p2_score != 50):
        inter1 = p1_score
        inter2 = p2_score

        # First player
        if (p1_score < 50):  # rolling the dice until getting the required number or getting near it
            input(f"{p1_name} Press Enter to roll the dice ...")
            roll_dice = random_num()
            p1_score += roll_dice
            print(f"_DICE 1 :{roll_dice}")
            print(f"_Player1 SCORE:{p1_score}\n\n\n")
            if (p1_score > 50):  # The player must have exactly the required number
                p1_score = inter1
                print(f"\nDear {p1_name} SCORE should be exactly ==> 50! SO Your score now is reset to {p1_score} \n\n")

            if (p1_score == 50):  # if the player reach the required number he win the game
                print(f"\t\t\t*********************** {p1_name} IS WINNER !! ***********************")
                break
        # Second player
        if (p2_score < 50):
            input(f"{p2_name} Press Enter to roll the dice ...")
            roll_dice = random_num()
            p2_score += roll_dice
            print(f"_DICE 2 :{roll_dice}")
            print(f"_Player2 SCORE:{p2_score}\n\n\n")
            if (p2_score > 50):
                p2_score = inter2
                print(f"\nDear {p2_name} SCORE should be exactly ==> 50! SO Your score now is reset to {p2_score} \n\n")
            if (p2_score == 50):
                print(f"\t\t\t*********************** {p2_name} IS WINNER !! ***********************")
                break

#  Main
if __name__ == "__main__":
    play()