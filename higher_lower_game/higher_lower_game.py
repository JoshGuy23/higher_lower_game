import art  # Imports ASCII logos
import game_data    # Imports list of dictionaries of social media data to choose from
import random   # Imports random module to choose data to be displayed
import os   # Imports os module for clearing of the screen.

# This function displays the introduction ASCII logo.
def intro():
    """Displays intro ASCII art"""
    print(art.logo)

# This function deconstructs the dictionaries from the game data, then displays the chosen data and calls choice().
# choice_a is the first dictionary of data, while choice_b is the second.
def deconstruct_dictionaries(choice_a, choice_b):
    """Deconstructs the data from game data and gets the user to choose which data has more followers."""
    # Get the names from the data
    name_a = choice_a["name"]
    name_b = choice_b["name"]
    # Get the descriptions from the data
    description_a = choice_a["description"]
    description_b = choice_b["description"]
    # Get the follower count from the data
    followers_a = choice_a["follower_count"]
    followers_b = choice_b["follower_count"]
    # Get the country of origin from the data
    country_a = choice_a["country"]
    country_b = choice_b["country"]
    
    # Display all data except follower count for the user
    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    print(art.vs)
    print(f"Against B: {name_b}, a {description_b}, from {country_b}.")
    # Gets the user to choose which piece of data has the most followers.
    result = choice(followers_a, followers_b)
    # Return a number that's either 0 or 1.
    return result

# This function has the user choose which piece of data has the most followers.
# Both f_count arguments are the follower counts of both pieces of data.
# If the guess is correct, return 1. Otherwise, return 0.
def choice(f_count_a, f_count_b):
    """User chooses which entity has more followers."""
    # Determine the answer from the follower counts.
    answer = ""
    if f_count_a > f_count_b:
        answer = "a"
    elif f_count_a < f_count_b:
        answer = "b"
    else:
        answer = "c"
    
    # If the user guesses correctly or both follower counts are the same return 1.
    # Otherwise, return 0.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == answer or answer == "c":
        return 1
    else:
        return 0

# This function is the main game of Higher or Lower.
def game():
    """Main game of higher or lower."""
    playing = True
    score = 0
    # The game continues as long as the player guesses correctly.
    while playing:
        # Display the intro ASCII
        intro()
        
        # Display the current score on successive iterations.
        if score > 0:
            print(f"Youre right! Current score: {score}.")
        # Randomly choose the data for the round. Make sure both pieces of data are unique.
        compare_a = random.choice(game_data.data)
        compare_b = random.choice(game_data.data)
        while compare_b == compare_a:
            compare_b = random.choice(game_data.data)
        
        # Deconstruct the data and get the user to choose which one has more followers.
        result = deconstruct_dictionaries(compare_a, compare_b)
        # Add 1 or 0 to the score.
        score += result
        # If the user guessed incorrectly, the game should stop after this loop.
        if result == 0:
            playing = False
        # Clear the screen.
        os.system("cls" if os.name == "nt" else "clear")
    # Display the game over message.
    print(f"Sorry, that's wrong. Final score: {score}.")

# Play the game    
game()