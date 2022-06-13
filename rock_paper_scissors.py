import random
# r for rock, p for paper, s for scissors
options = ["R", "P", "S"]
print("Welcome to the Rock, Paper, Scissors game!")
user = input("Enter your name: ")

check = input("Enter yes to play or quit to end the game: ").lower()

while check == "yes":
    s = random.randint(0, 2)
    UserData = input("Enter R for Rock, P for Paper, or S for Scissors: ")

    if UserData not in options:
        print("You didn't enter any of the options given")
        check = input("Enter yes to play or quit to end the game: ").lower()

    else:
        print("computer picks {}".format(options[s].title()))
        if options[s] == UserData.upper():
            print("It's a tie")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif options[s] == "R" and UserData.upper() == "S":
            print("Computer wins!")
            print("Rock smashes Scissors")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif options[s] == "R" and UserData.upper() == "P":
            print("You win!")
            print("Paper covers Rock")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif options[s] == "P" and UserData.upper() == "R":
            print("Computer wins!")
            print("Paper covers Rock")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif options[s] == "P" and UserData.upper() == "S":
            print("You win!")
            print("Scissors cuts Paper")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif options[s] == "S" and UserData.upper() == "R":
            print("You win!")
            print("Rock smashes Scissors")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()

        elif options[s] == "S" and UserData.upper() == "P":
            print("Computer wins!")
            print("Scissors cuts Paper")
            check = input("Enter yes to keep playing or quit to end the game: ").lower()
