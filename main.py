match_run = True
groups = {
    "Group_A": {
        "Argentina": {"W": 2, "L": 0, "D": 1, "GF": 5, "GA": 2},
        "France": {"W": 2, "L": 1, "D": 0, "GF": 6, "GA": 3},
        "Brazil": {"W": 1, "L": 1, "D": 1, "GF": 4, "GA": 4},
        "Germany": {"W": 0, "L": 3, "D": 0, "GF": 2, "GA": 8}
    },
    "Group_B": {
        "Spain": {"W": 3, "L": 0, "D": 0, "GF": 7, "GA": 1},
        "Portugal": {"W": 2, "L": 1, "D": 0, "GF": 5, "GA": 3},
        "Uruguay": {"W": 1, "L": 2, "D": 0, "GF": 3, "GA": 5},
        "Japan": {"W": 0, "L": 3, "D": 0, "GF": 1, "GA": 7}
    },
    "Group_C": {
        "England": {"W": 2, "L": 0, "D": 1, "GF": 6, "GA": 2},
        "USA": {"W": 1, "L": 1, "D": 1, "GF": 3, "GA": 3},
        "Mexico": {"W": 1, "L": 2, "D": 0, "GF": 2, "GA": 5},
        "Italy": {"W": 0, "L": 2, "D": 1, "GF": 2, "GA": 5}
    }
}

def win_max(groupName):
    higher_win =0
    higher_team =""
    arr_higher = {}
    user_group = f"Group_{groupName}"
    for key, value in groups.items():
        if user_group == key:
            for team , win_rate in value.items():
                if win_rate["W"] >higher_win:
                    higher_win=win_rate["W"]
                    arr_higher[team] = win_rate["W"]
                elif higher_win == win_rate["W"]:
                    arr_higher[team]=win_rate["W"]

    print(arr_higher)


def worldCupTeams(userChoice):
    if userChoice == "1":
        for key, value in groups.items():
            print(key)
    elif userChoice == "2":
         group_a_teams =  groups["Group_A"]
         print("Group_A")
         for key, value in group_a_teams.items():
             print(key)
    elif userChoice == "3":
        print("--------")
        for key, value in groups.items():
            for country,score in value.items():
                print(f"{country}")
        print("--------")
    elif userChoice == "4":
        fifa_team  = input("Enter a team name :").title()
        for countries, value in groups.items():
            for team ,values in value.items():
                if team ==fifa_team:
                    print(f"{countries} win:{values['W']}, lose:{values['L']}, Draw:{values['D']}")
    elif userChoice =="5":
        group_status = input("Enter a group name :").title()
        GoalFor_total = 0
        for group, value in groups.items():
            user_group = f"Group_{group_status}"
            if group == user_group:
                for key, values in value.items():
                    GoalFor_total+=values['GF']
        print(GoalFor_total)
    elif userChoice =="6":
        max_group_win = input("Enter a group name :").title()
        win_max(max_group_win)
while match_run:
    user = input("**** Menu ****"
                 "\n1:Print all groups."
                 "\n2:Print all teams in 'Group_A'."
                 "\n3:Print only team names from all groups."
                 "\n4:Find total wins,lose,draw of 'any user choice team'."
                 "\n5:Find total goals scored (GF) by 'any group'."
                 "\n6:Find team with maximum wins in 'any group'."
                 "\n7:End  "
                 "\nPlease Enter your choice:")
    worldCupTeams(user)




