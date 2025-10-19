def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Enter (A,B,C, or D!)").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print("---------------------------------------------")
    print("Results")
    print("---------------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    print("Your score is: " + str(correct_guesses) + "/" + str(len(questions)))
    if correct_guesses >= len(questions) * 0.7:
        print("Congratulations, you pass!")
    if correct_guesses <= 2:
        print("Sorry, you fail!")
    

def play_again():
    play_again = input("Would you like to play again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again = input("Would you like to play again? (yes/no): ").lower()
    
    return play_again == "yes"

questions = {
    "Bumi bulat?: ": "A",
    "1+1 = ?": "B",
    "Hewan mamalia, kecuali?: ": "C",
    "Hewan yang paling cepat?: ": "D"
}

options = [["A. Ya", "B. Tidak", "C. Mungkin", "D. Mungkin Tidak"],
          ["A. 1", "B. 2", "C. 3", "D. 4"],
          ["A. Singa", "B. Gajah", "C. Ular", "D. Harimau"],
          ["A. Gajah", "B. Ular", "C. Harimau", "D. Cheetah"]]

new_game()

while play_again():
    new_game()
print("BYE!")