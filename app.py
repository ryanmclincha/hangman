from hangman import play_hangman, show_menu
from user import User

while True:
    # Get user this is not case sensitive and can take numbers
    player = input("User: ")
    player = player.capitalize()
    if len(player) > 6 or player == "":
        print("User names must be 1-6 characters.")
        continue
    user = User(player)
    break

while True:
    print()
    show_menu()
    print("User:", user.name, "\n")
    user_choice = input("Choose an option: ")

    # Launches the hangman game and gets win result
    if user_choice == "1":
        result = play_hangman()
        user.letters_guessed += int(result["letters guessed"])
        if result["result"] is True:
            user.wins += 1
        else:
            user.losses += 1
        user.games_played += 1
        user.save_user()
    # changes user and saves current user to txt file
    elif user_choice == "2":
        while True:
            player = input("User: ")
            player = player.capitalize()
            if len(player) > 6 or player == "":
                print("User names must be 1-6 characters.")
                continue
            user.save_user()
            user = User(player)
            break
    # shows individual stats for games played
    elif user_choice == "3":
        user.show_stats()
    # shows a leaderboard organized by win %
    elif user_choice == "4":
        user.show_leaderboard()
    # exits the program
    elif user_choice == "5":
        print("GoodBye", user.name + "!")
        user.save_user()
        quit()
    else:
        print("Please select and option 1-5")
