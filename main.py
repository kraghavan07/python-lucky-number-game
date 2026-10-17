import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        user_num = int(input("Guess The Luck Number: "))

        if user_num == lucky_num:
            print("YOU WON. GAME OVER!!!")
            break
        elif user_num < lucky_num:
            print("TOO LOW")
        else:
            print("TOO HIGH")

    print("THANK YOU FOR PLAYING ")

play_game()