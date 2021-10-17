import os

# meat and potatoes of how the User game data is saved and handled
class User:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.games_played = 0
        self.letters_guessed = 0
        self.load_user()

    # checks if a user_data directory exists if not creates one
    # moves to the user directory and checks for file with username
    # if it exists the user data is udated for the class
    def load_user(self):
        if os.path.exists("user_data"):
            os.chdir("user_data")
            if os.path.exists(self.name + ".txt"):
                f = open(self.name + ".txt", "r")
                self.name = f.readline()[:-1]
                self.wins = int(f.readline()[:-1])
                self.losses = int(f.readline()[:-1])
                self.games_played = int(f.readline()[:-1])
                self.letters_guessed = int(f.readline()[:-1])
                f.close()
            os.chdir("../")
        return

    # similar to load user but for saving the data
    # each different class attribute is saved on a new line
    # if there was a save for a user already it will delete it and make an updated one
    def save_user(self):
        if os.path.exists("user_data"):
            os.chdir("user_data")
        else:
            os.mkdir("user_data")
            os.chdir("user_data")

        if os.path.exists(self.name + ".txt"):
            os.remove(self.name + ".txt")

        f = open(self.name + ".txt", "a")
        f.write(self.name + "\n")
        f.write(str(self.wins) + "\n")
        f.write(str(self.losses) + "\n")
        f.write(str(self.games_played) + "\n")
        f.write(str(self.letters_guessed) + "\n")
        f.close()

        os.chdir("../")

    # method for calculating win % not necessary to have this saved to file
    def win_percent(self):
        if self.losses == 0 and self.wins >= 0:
            return 100.0
        total_played = self.wins + self.losses
        percentage = "%.1f" % (self.wins / total_played * 100)
        return percentage

    # prints the current user's game stats
    def show_stats(self):
        print("Username:\t", self.name)
        print("Wins:\t\t", self.wins)
        print("Losses:\t\t", self.losses)
        print("Games played:\t", self.games_played)
        print("Win percentage:\t", str(self.win_percent()) + "%")
        print("Letters_guessed:", self.letters_guessed)
        print()


    def show_leaderboard(self):

        leaderboard = []

        os.chdir("user_data")

        # reads the user files and creates a dictionary for each user
        # appends each user dictionary to the leader board list
        for file in os.listdir(os.getcwd()):

            f = open(file, "r")
            name = f.readline()[:-1]
            wins = int(f.readline()[:-1])
            losses = int(f.readline()[:-1])
            games_played = int(f.readline()[:-1])
            letters_guessed = int(f.readline()[:-1])
            f.close()

            if losses == 0 and wins >= 0:
                win_per = 100.0
            else:
                total_played = wins + losses
                win_per = float(wins / total_played * 100)

            data = {
                "name": name,
                "wins": wins,
                "losses": losses,
                "games_played": games_played,
                "win_percent": "%.1f" % win_per,
                "letters_guessed": letters_guessed
            }

            leaderboard.append(data)

        os.chdir("../")

        # using a lambda function to sort a list of dictionaries
        leaderboard = sorted(
            leaderboard, key=lambda i: float(i["win_percent"]), reverse=True)

        # display sorted leaderboard for the user
        print("Name\tWins\tLosses\tGames\tWin\tLetters")
        print("\t\t\tPlayed\tPercent\tGuessed")
        for entry in leaderboard:
            print(
                entry["name"] + "\t" + str(entry["wins"]) + "\t" + str(entry["losses"]) + "\t" +
                str(entry["games_played"]) + "\t" +
                str(entry["win_percent"]) + "\t" +
                str(entry["letters_guessed"])
            )
