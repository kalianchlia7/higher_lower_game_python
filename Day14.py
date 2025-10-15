import random

from game_data import game_data
# from file import name of dictionary

from artlogo import logo
from artlogo import vs 



def higher_lower ():
    current_score = 0
    while True:
        print(logo)
        random_a = random.randint(0, len(game_data) - 1)
        key_a = game_data[random_a]
        print(f"Compare A: {key_a['name']}, a {key_a['description']}, from {key_a['country']}")

        print(vs)
        random_b = random.randint(0, len(game_data)-1)
        if random_b == random_a:
            random_b = random.randint(0, len(game_data)-1)
        key_b = game_data[random_b]
        print(f"Against B: {key_b['name']}, a {key_b['description']}, from {key_b['country']}")

        choice=input("Who has more followers? Type 'A' or 'B': ")

        if key_a['follower_count'] > key_b['follower_count'] and choice == 'A':
            current_score+=1
            print(f"You’re right! Current score: {current_score}")
        elif key_b['follower_count'] > key_a['follower_count'] and choice == 'B':
            current_score+=1
            print(f"You’re right! Current score: {current_score}")
        else: 
            print(f"Sorry, that’s wrong. Final Score: {current_score}")
            break
        
higher_lower()
       