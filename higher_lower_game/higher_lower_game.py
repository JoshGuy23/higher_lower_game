import art
import game_data
import random

def intro():
    """Displays intro ASCII art"""
    print(art.logo)

def deconstruct_dictionaries(choice_a, choice_b, score):
    name_a = choice_a["name"] # put all this into a function
    name_b = choice_b["name"]
    description_a = choice_a["description"]
    description_b = choice_b["description"]
    followers_a = choice_a["follower_count"]
    followers_b = choice_b["follower_count"]
    country_a = choice_a["country"]
    country_b = choice_b["country"]
    
    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    print(art.vs)
    print(f"Against B: {name_b}, a {description_b}, from {country_b}.")
    result = choice(followers_a, followers_b, score)
    return result

def choice(f_count_a, f_count_b, p_score):
    answer = ""
    if f_count_a > f_count_b:
        answer = "a"
    elif f_count_a < f_count_b:
        answer = "b"
    else:
        answer = "c"
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == answer or answer == "c":
        print(f"You're right! Current score: {p_score + 1}.")
        return 1
    else:
        return 0

def game():
    playing = True
    score = 0
    while playing:
        
        intro()
        compare_a = random.choice(game_data.data)
        compare_b = random.choice(game_data.data)
        while compare_b == compare_a:
            compare_b = random.choice(game_data.data)
        
        result = deconstruct_dictionaries(compare_a, compare_b, score)
        
        score += result
        if result == 0:
            playing = False