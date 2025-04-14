# Import modules
import random
from art import logo, vs
from game_data import data

score = 0
game_on = True

choice_a = random.choice(data)
choice_b = random.choice(data)
data.remove(choice_a)
data.remove(choice_b)
choices = {'A':choice_a, 'B':choice_b}
print(logo)
print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
print(vs)
print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
choice = input("Who has more followers? Type 'A' or 'B': ").upper()
choice_count = choices[choice]['follower_count']
del choices[choice]
not_chosen = [key for key in choices.keys()][0]
other_count = choices[not_chosen]['follower_count']

while game_on:
    if choice_count > other_count:
        score+=1
        print("\n" * 5)
        print(f"You're right! Current score: {score}")
        choice_a = choice_b
        choice_b = random.choice(data)
        if choice_a in data:
            data.remove(choice_a)
        if choice_b in data:
            data.remove(choice_b)
        choices = {'A':choice_a, 'B':choice_b}
        print(logo)
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
        print(vs)
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        choice_count = choices[choice]['follower_count']
        del choices[choice]
        not_chosen = [key for key in choices.keys()][0]
        other_count = choices[not_chosen]['follower_count']
    else:
        print("\n" * 10)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False







