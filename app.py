import random

suites = ['♡', '♢', '♤', '♧']
numbers =['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q','K']

def get_random_card():
    random_suite = random.choice(suites) #will pick a random suite for me
    random_number = random.choice(numbers) #pick a random numbers from numbers
    combine_random_suite_and_number = f"Hello Finallgirll {random_number}{random_suite}" #combines random suite and random number
    return combine_random_suite_and_number #all functions must return something if you want it to work and "display"

#prints your function in terminal
print(get_random_card())