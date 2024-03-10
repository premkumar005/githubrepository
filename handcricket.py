import random

total_runs=0
computer_total_runs = 0

def user_toss_win():
    print("You are the batsman.")

    global total_runs

    while True:
        try:
            user_input = int(input("Enter your choice (1-6): "))

            if user_input < 1 or user_input > 6:
                print("Invalid input! Choose a number between 1 and 6.")
                continue

            computer_bowl = random.randint(1, 6)
            print("Computer bowls:", computer_bowl)

            if user_input == computer_bowl:
                print("Out! Your total runs:", total_runs)
                break
            else:
                total_runs += user_input
                print("You scored", user_input, "runs. Total runs:", total_runs)


        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")


def computer_toss_win():


    global computer_total_runs

    while True:
        try:
            computer_input = random.randint(1, 6)

            if computer_input < 1 or computer_input > 6:
                print("Invalid input! Choose a number between 1 and 6.")
                continue

            user_bowl = int(input("Enter your choice (1-6): "))
            print("user bowls:", user_bowl)

            if computer_input == user_bowl:
                print("computer choice", computer_input, "runs. Total runs:", computer_total_runs)
                print("Out! computer total runs:", computer_total_runs)
                break
            else:
                computer_total_runs += computer_input
                print("computer choice", computer_input, "runs. Total runs:", computer_total_runs)


        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")


def play():
    string = ("odd", "even")
    user = input("enter odd or even ")

    print('user:', user)
    if user == "odd":
        print("computer value: even")
    else:
        print("computer value: odd")
    n = int(input("typeno.btw 1 to 6: "))
    print("ur value is", n)
    rando = random.randint(1, 6)
    print("computer value is ", rando)
    if user == "even":
        if ((n + rando) % 2 == 0):
            print("user won the toss")
            o = input("choose batting or bowling")
            if o == "batting":
                print("user chose batting")
                print("computer plays bowling")
                user_toss_win()
                computer_toss_win()
            else:
                print("user chose bowling")
                print("computer plays batting")
            computer_toss_win()
            user_toss_win()
        else:
            print("computer won the toss")
            s = ("batting", "bowling")
            rando_c = random.choice(s)
            if rando_c == "batting":
                print("computer chose", rando_c)
                print("user plays bowling")
                computer_toss_win()
                user_toss_win()
            else:
                print("computer chose bowling")
                print("user plays batting")
                user_toss_win()
                computer_toss_win()




    else :

        if ((n + rando) % 2 != 0):
            print("user won the toss")
            r = input("choose batting or bowling ")
            if r == 'batting':
                print("user chose batting")
                print("computer plays bowling")
                user_toss_win()
                computer_toss_win()
            else:
                print("user chose bowlig")
                print("computer plays batting")
            user_toss_win()
            computer_toss_win()
        else:
            print("computer won the toss")
            p = ("batting", "bowling")
            rando_p = random.choice(p)
            if rando_p == "batting":
                print("computer chose", rando_p)
                print("user plays bowling")
                computer_toss_win()
                user_toss_win()
            else:
                print("computer chose bowling")
                print("user plays batting")
                user_toss_win()
                computer_toss_win()

def finalscore():
    global total_runs, computer_total_runs  # Access the global total_runs and computer_total_runs variables
    condition = total_runs < computer_total_runs
    if condition :
        print("computer scores", computer_total_runs)
        print("user scores", total_runs)
        print("computer won")
    else:
        print("computer scores", computer_total_runs)
        print("user scores", total_runs)
        print("you won")


play()
finalscore()

