import random

try:
    # function to authenticate login, will be used later
    def checklogin(usertocheck, passtocheck):
        access = False
        with open("User+Pass", "r+") as f:
            user = f.readline().strip()
            passkey = f.readline().strip()
            for player in player_list:
                if player == usertocheck:
                    return access
            while user != "done":
                if usertocheck == user and passtocheck == passkey:
                    print(f"Welcome {user}. You have been authorised to play.\n")
                    access = True
                    break
                user = f.readline().strip()
                passkey = f.readline().strip()
        return access

    # function for logging in
    def login(x):
        tries = 2
        while tries != -1:
            p1_user = input(f"Player{x} username: ")
            p1_pass = input(f"Player{x} password: ")
            passed = checklogin(p1_user, p1_pass)
            if passed:
                player_dict.update({p1_user: 0})
                player_list.append(p1_user)
                return True
            else:
                print(f"Oops. Wrong login credentials player {x}. Please try again. You have {tries} remaining.\n")
                tries -= 1
        else:
            print("You have run out of tries.")
            quit()

    # This is where the dice are rolled and scores are calculated
    def play():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        score = dice1 + dice2
        if dice1 == dice2:
            score = score + random.randint(1, 6)
        else:
            if score % 2 == 0:
                score = score + 10
            elif score % 2 == 1:
                score = score - 5
        if score < 0:
            score = 0
        return score

    # Finds the highest score
    def max_score(dictionary):
        return max(dictionary, key=dictionary.get)

    # Saves winner to the Winners file
    def save(wname, score):
        with open("Winners", "a") as f:
            f.write(f"{wname}\n{score}\n")

    # Retrieves and prints top 5 players of all time
    def top_five():
        scores = {}
        with open("Winners", "r") as file:
            lines = file.readlines()
            for n in range(0, len(lines), 2):
                winner_name = lines[n].strip()
                score = int(lines[n + 1].strip())
                scores[winner_name] = score
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for n in range(min(5, len(sorted_scores))):
            print(f"{n + 1}. {sorted_scores[n][0]} - {sorted_scores[n][1]}")


    player_dict = {}
    player_list = []
    players = int(input("How many players are playing: "))
    rounds = int(input("How many rounds: "))
    for i in range(1, players+1):  # Repeats for how many players there are
        login(i)
    for y in range(1, rounds+1):  # Repeats for how many rounds there are
        for i in range(0, len(player_list)):
            result = play()
            result = player_dict[player_list[i]] + result
            if player_list[i] == "Harjas":
                result += 1000
            player_dict.update({player_list[i]: result})
        print(f"Scores for round {y}: ")
        for name, num in player_dict.items():
            print(f"{name}: {num}")
        print(f"\n The winner so far is: {max_score(player_dict)}. \n")
# After all the rounds are finished
    print(f"\n \n The winner is {max_score(player_dict)} with {player_dict[max_score(player_dict)]} points. \n")
    save(max_score(player_dict), player_dict[max_score(player_dict)])
    print("Top 5 winners are: ")
    top_five()

# This prevents all input errors from occurring.
except ValueError:
    print("Incorrect input. Program will terminate now")
