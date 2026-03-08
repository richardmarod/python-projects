"""
Game Session Tracker

Allows a user to add, view and save gaming sessions.
Tracks game name, date, hours played, and platform.
"""

from game_session import GameSession

#Save / Load

def save_sessions(filename, sessions):
    f = open(filename, "w", encoding = "utf-8")
    for s in sessions:
        line = f"{s.game}|{s.date}|{s.get_hours()}|{s.platform}"
        f.write(line + "\n")
    f.close()

def load_sessions(filename):
    sessions = []

    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        return sessions
    else:
        for line in f:
            line = line.strip()
            if line != "":
                parts = line. split("|")
                game = parts [0]
                date = parts[1]
                hours = float(parts[2])
                platform = parts[3]
                sessions.append(GameSession(game, date, hours, platform)
                 )
        f.close()

    return sessions

#Stats

def get_stats(sessions):
    unique_games = set()
    hours_by_game = {}
    platform_count = {}

    total_hours = 0.0

    for s in sessions:
        unique_games.add(s.game)
        total_hours += s.get_hours()

        # hours per game
        if s.game not in hours_by_game:
            hours_by_game[s.game] = 0.0
        hours_by_game[s.game] += s.get_hours()

        # count platforms
        if s.platform not in platform_count:
            platform_count[s.platform] = 0
        platform_count[s.platform] += 1

    most_played = "None"
    most_hours = 0.0

    for game in hours_by_game:
        if hours_by_game[game] > most_hours:
            most_hours = hours_by_game[game]
            most_played = game

    most_used_platform = "None"
    most_platform_count = 0

    for p in platform_count:
        if platform_count[p] > most_platform_count:
            most_platform_count = platform_count[p]
            most_used_platform = p

    return (total_hours, most_played, len(unique_games), most_used_platform)

# Menu Actions

def add_session(sessions):
    game = input("Game name: ").strip()
    date = input("date (YYYY-MM-DD): ").strip()

    try:
        hours = float(input("Hours played (ex: 2.5): "))
        platform = input("Platform (PC/Console/Mobile): ").strip()
    except ValueError:
        print("Invalid input. \n")
        return
    else:
        sessions.append(
            GameSession(game, date, hours, platform)
        )
        print("Session added!\n")

def view_sessions(sessions):
    if len(sessions) == 0:
        print("No sessions yet.\n")
        return

    for s in sessions:
        print(s)
    print()

def view_stats(sessions):
    total, most_played, unique, top_platform = get_stats(sessions)

    print("---- Stats ----")
    print("Total hours:", total)
    print("Most played game:", most_played)
    print("Unique games:", unique)
    print("Most used platform:", top_platform)
    print()

# Unit Tests

def run_tests():
    print("\nRunning tests...")

    s1 = GameSession("Final Fantasy 14", "2026-02-26", 2.5, "PC")
    assert s1.get_hours() == 2.5

    ok = s1.set_hours(4.0)
    assert ok is True
    assert s1.get_hours() ==4.0

    s2 = GameSession("Pokemon Leaf Green", "2026-02-27", 3.0, "Console")

    print("All tests passed!\n")

# Main Program

def main():
    """Main program loop."""
    filename = "sessions.txt"
    sessions = load_sessions(filename)

    while True:
        print("1) Add Session")
        print("2) View Sessions")
        print("3) View Stats")
        print("4) Save")
        print("5) Run Unit Tests")
        print("6) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            view_sessions(sessions)
        elif choice == "3":
            view_stats(sessions)
        elif choice == "4":
            save_sessions(filename, sessions)
            print("Saved!\n")
        elif choice == "5":
            run_tests()
        elif choice == "6":
            save_sessions(filename, sessions)
            print("Saved. See you next time!\n")
            break
        else:
            print("Invalid choice.\n")

main()

















































    
