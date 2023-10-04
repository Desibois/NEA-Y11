import random


def login(usertocheck, passtocheck):
    access = False
    f = open("User+Pass", "r+")
    user = f.readline().strip()
    passkey = f.readline().strip()
    while user != "done":
        if usertocheck == user and passtocheck == passkey:
            print(f"Welcome {user}. You have been authorised to play.\n")
            access = True
            break
        user = f.readline().strip()
        passkey = f.readline().strip()
    return access


def checklogin(x):
    tries = 2
    while tries != -1:
        p1_user = input("Player " + str(x) + " username: ")
        p1_pass = input("Player " + str(x) + " password: ")
        passed = login(p1_user, p1_pass)
        if passed:
            player_dict.update({p1_user: 0})
            return True
        elif not passed:
            print(f"Oops. Wrong login credentials player {x}. Please try again. You have {tries} remaining.\n")
            tries -= 1
    else:
        print("You have run out of tries.")
        quit()


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


def max_score(dictionary):
    val = max(dictionary, key=dictionary.get)
    return val


def save(wname, score):
    f = open("Winners", "a")
    f.write(wname + "\n")
    f.write(str(score) + "\n")
    f.close()


def top_five():
    f = open("Winners", "r")
    unordered_leaderboard = {}
    ordered_leaderboard = {}
    top_name = f.readline().strip()
    top_score = f.readline().strip()
    unordered_leaderboard.update({top_name: top_score})
    while top_name != "":
        top_name = f.readline().strip()
        top_score = f.readline().strip()
        unordered_leaderboard.update({top_name: top_score})
    for x in range(0, 5):
        while top_score != "":
            toppest_name = max_score(unordered_leaderboard)
            toppest_score = unordered_leaderboard[toppest_name]
            del unordered_leaderboard[toppest_name]
            ordered_leaderboard.update({toppest_name: toppest_score})
    return ordered_leaderboard


player_dict = {}
players = int(input("How many players are playing: "))
rounds = int(input("How many rounds: "))
for i in range(1, players+1):
    checklogin(i)
player_list = list(player_dict.keys())
print(player_list)
for y in range(1, rounds+1):
    for i in range(0, len(player_list)):
        output = play()
        output = player_dict[player_list[i]] + output
        player_dict.update({player_list[i]: output})
        i += 1
    print(f"Scores for round {y}: ")
    for name, num in player_dict.items():
        print(f"{name}: {num}")
    print(f"\n The winner so far is: {max_score(player_dict)}.")

print(f"\n \n The winner is {max_score(player_dict)} with {player_dict[max_score(player_dict)]} points.")
save(max_score(player_dict), player_dict[max_score(player_dict)])
print("Top 5 players are")
place = 1
for name in top_five():
    print(f"{place}. {name} ")
    place += 1
