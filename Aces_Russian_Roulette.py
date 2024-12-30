import random

def generate_npc_description(name, gender):
    """Generates a random description for an NPC."""
    age = random.randint(20, 50)
    personality_traits = ["unpredictable", "fierce", "quiet", "nervous", "brooding"]
    appearances = [
        "has a scar over their left eye", 
        "has a nervous tick", 
        "has a sharp wit",
        "always looks over their shoulder",
        "has a brooding expression"
    ]
    builds = ["a stocky build", "a lean build", "a tall build", "an average build"]

    hair_colors = ["black", "blonde", "dark brown", "red"]
    eye_colors = ["brown", "blue", "green", "hazel"]

    trait = random.choice(personality_traits)
    appearance = random.choice(appearances)
    build = random.choice(builds)
    hair_color = random.choice(hair_colors)
    eye_color = random.choice(eye_colors)

    pronoun = "He" if gender == "male" else "She"
    return (
        f"{name}, a {age}-year-old {trait} individual who {appearance}. "
        f"{pronoun} has {hair_color} hair, {eye_color} eyes, and {build}."
    )

def russian_roulette():
    """Main game logic."""
    print("You enter a dimly lit local bar, the sound of laughter and clinking glasses fills the air.")
    print("You walk up to the counter and sit down. The bartender nods at you, and you feel like tonight could be interesting.")
    print("Suddenly, a group of hardened faces approach, and they challenge you to a game. It's Russian Roulette.")
    print("The stakes are high. Will you survive the game, or will it be your last drink?\n")

    player_name = input("What is your name, brave soul? ")

    print("\nSelect game mode:")
    print("1. Traditional 1v1 (Player vs Player)")
    print("2. Multiplayer (Player vs up to 3 players)")
    game_mode = int(input("Enter 1 or 2: "))

    if game_mode == 2:
        num_npcs = int(input("\nHow many other players (up to 3)? "))
        npc_names = ["Dmitri", "Olga", "Viktor", "Svetlana"]
        genders = ["male", "female", "male", "female"]
        selected_npcs = random.sample(list(zip(npc_names, genders)), num_npcs)

        print(f"\n{num_npcs} people walk up to you, and you can tell they're not here for small talk...\n")
        players = [
            {"name": player_name, "is_alive": True, "is_player": True}
        ]
        for npc_name, gender in selected_npcs:
            description = generate_npc_description(npc_name, gender)
            print(description)
            players.append({"name": npc_name, "is_alive": True, "is_player": False})

        print(f"\n{', '.join([npc['name'] for npc in players if not npc['is_player']])} step forward and ask, \"Well, {player_name}, are you brave enough to play with us? A round of Russian Roulette?\"\n")
        consent = input("Do you want to play? (yes/no): ").lower()

        if consent != "yes":
            print("You decided to leave the bar. Congratulations on making the smart choice not to play a game with a lethal firearm!")
            return
    else:
        players = [
            {"name": player_name, "is_alive": True, "is_player": True},
            {"name": "Dmitri", "is_alive": True, "is_player": False}
        ]
        print("\nDmitri steps forward and asks, \"Well, are you brave enough to play with me?\"\n")
        consent = input("Do you want to play? (yes/no): ").lower()

        if consent != "yes":
            print("You decided to leave the bar. Congratulations on making the smart choice not to play a game with a lethal firearm!")
            return

    print("\nAlex agrees to the challenge. The game begins...\n")

    # Determine who starts
    current_index = random.randint(0, len(players) - 1)
    print(f"The players spin the gun, and it lands on {players[current_index]['name']} to start the game.\n")

    chamber_position = 0
    bullet_position = random.randint(0, 5)
    max_chambers = 6

    while sum(player["is_alive"] for player in players) > 1:
        current_player = players[current_index]

        if not current_player["is_alive"]:
            current_index = (current_index + 1) % len(players)
            continue

        if current_player["is_player"]:
            print("You pull the trigger...")
        else:
            print(f"{current_player['name']} pulls the trigger...")

        if chamber_position == bullet_position:
            print("BANG!")
            current_player["is_alive"] = False
            if current_player["is_player"]:
                print("Oh well. I suppose that’s what you get for playing with firearms.")
                return
        else:
            print("Click...")
            if not current_player["is_player"]:
                pronoun = "He" if current_player["name"] in ["Dmitri", "Viktor"] else "She"
                reaction = random.choice([
                    f"{pronoun} laughs nervously.",
                    f"{pronoun} wipes sweat from their brow.",
                    f"{pronoun} smirks, trying to hide their fear."
                ])
                print(reaction)

        chamber_position = (chamber_position + 1) % max_chambers
        current_index = (current_index + 1) % len(players)

        if sum(player["is_alive"] for player in players) > 1:
            print("\nThe game continues...\n")

    winner = next(player for player in players if player["is_alive"])
    if winner["is_player"]:
        print(f"Congratulations, {player_name}, you won! You have a feeling that you won’t be quite the same person after playing this game.")
    else:
        print(f"{winner['name']} won the game. Maybe it's best to avoid bars for a while.")

