import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
while True:
    start = input("Play or Not? (Y/N)").upper()
    if start == "Y":
        user = input("Enter your choice (rock, paper, scissors): ").lower()
        print()
    if start == "N":
        print("Goodbye!")
        break

    if user in choices:
        print("Computer vs User")
        print(computer, "vs", user)
    if user not in choices:
        print("Wrong input!")
        print()
        continue

    if user == computer:
        print("tie!")
        print()
    elif user == "rock":
        if computer == "scissors":
            print("User wins!")
            print()
        if computer == "paper":
            print("Computer wins!")
            print()
    elif user == "paper":
        if computer == "rock":
            print("User wins!")
            print()
        if computer == "scissors":
            print("Computer wins!")
            print()
    elif user == "scissors":
        if computer == "paper":
            print("User wins!")
            print()
        if computer == "rock":
            print("Computer wins!")
            print()
    else:
        break