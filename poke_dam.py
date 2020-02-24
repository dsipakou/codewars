def calc(your_type, opponent_type, attack, defense):
    type = {
        "fire": {
            "grass": 2,
            "electric": 1,
            "water": 0.5,
            "fire": 0.5
        },
        "grass": {
            "water": 2,
            "electric": 1,
            "fire": 0.5,
            "grass": 0.5
        },
        "water": {
            "fire": 2,
            "electric": 0.5,
            "grass": 0.5,
            "water": 0.5
        },
        "electric": {
            "water": 2,
            "grass": 1,
            "fire": 1,
            "electric": 0.5
        }
    }
    return int(50 * (attack / defense) * type[your_type][opponent_type])

print(calc("fire", "water", 100, 100))
