import art
import game_data
import random

def intro():
    """Displays intro ASCII art"""
    print(art.logo)
    
def game():
    playing = True
    while playing:
        intro()
        compare_a = random.choice(game_data.data)
        compare_b = random.choice(game_data.data)
        while compare_b == compare_a:
            compare_b = random.choice(game_data.data)