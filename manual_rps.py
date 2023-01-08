import random

def get_computer_choice():
    rps = (["Rock","Paper","Scissors"])
    computer_choice = random.choice(rps)
    return computer_choice

def get_user_choice():
    user_choice = input (" Please choose between Rock, Paper or Scissors!. ")
    return user_choice

get_computer_choice()