# PF-Exer-28

# This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    count1 = 0
    count2 = 0
    while (len(match_tuple) <= 3):
        for i in range(len(match_tuple)):
            if (match_tuple[i] == "Team1"):
                count1 = count1 + 1
            elif (match_tuple[i] == "Team2"):
                count2 = count2 + 1
        if (count1 > count2):
            x = "Team1"
            return x
        elif (count1 < count2):
            x = "Team2"
            return x
        elif (count1 == count2):
            x = "Tie"
            return x
    s = ""
    return s


# Invoke the function with each of the print statements given below
# print(find_winner_of_the_day("Team1","Team2","Team1"))
print(find_winner_of_the_day("Team1", "Team2", "Team1", "Team2"))

