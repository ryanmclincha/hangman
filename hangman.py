import word_list


def play_hangman():
    # pull a word from a custom list
    answer_string = word_list.word_select()
    answer_string = answer_string.upper()

    # this is how many times the player can guess wrong
    while True:
        difficulty = input("Select difficulty easy(1) normal(2) hard(3): ")
        if difficulty == "1":
            lives = 10
            break
        elif difficulty == "2":
            lives = 7
            break
        elif difficulty == "3":
            lives = 5
            break

    # using "_" to indicate the amount of characters in the word
    display_list = []
    for char in answer_string:
        display_list.append("_ ")

    # create a string to display to the user so they know what they have gotten correct
    display_string = ""
    for letter in display_list:
        display_string += letter

    letters_guessed = " "

    while True:
        # Show game progress
        print("\n" + display_string)
        print("Your remaining lives:", lives)
        print("Guesses: " + letters_guessed)

        # users can guess the word or letter
        guess = input("guess a letter or the word: ")
        guess = guess.upper()

        if guess.isalpha() == False or guess == "":
            print("\nGuesses must be letters or words")
            continue
        if guess in letters_guessed:
            print("\nYou already guessed that!")
            continue

        if len(guess) == 1:
            letters_guessed += guess

        # if they guess a word and it is correct they win
        if guess == answer_string:
            print("\nYou won the game! The answer was: " + answer_string)
            result = True
            break
        # if they guess a character and it's in the string
        # the program will replace the corresponding  "_ " with the correct character
        elif guess in answer_string:
            index = 0
            for char in answer_string:
                if char == guess:
                    display_list[index] = guess + " "
                index += 1
            # no more "_ " means the player has solved the word
            if "_ " not in display_list:
                print("\nYou won the game! The answer was: " + answer_string)
                result = True
                break
        else:
            # incorrect guesses are handled here
            lives -= 1
            if lives == 0:
                print("\nYou lost the game! The answer was: " + answer_string)
                result = False
                break

        # converts the display list to a string for readability
        display_string = ""
        for letter in display_list:
            display_string += letter

    # dictionary of some game stats
    return {"result": result, "letters guessed": len(letters_guessed)}


def show_menu():
    print("           === Hangman ===")
    print("________________________________________")
    print()
    print("| 1. Play        | 2. Change User      |")
    print("________________________________________")
    print()
    print("| 3. Your stats  | 4. Leaderboard      |")
    print("________________________________________")
    print()
    print("|             5. Exit                  |")
    print("________________________________________")
    print()
