import random

options = ("sunny,rainy,cold")

while True:
    user_input = input("What's the weather like today? (sunny/rainy/cold) ").lower()
    
    if user_input not in options:
        print("Sorry, I don't have recommendations for this weather.")
        continue
    
    if user_input == 'sunny':
        print("Wear a t-shirt and sunglasses.")
        break
