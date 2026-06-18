#number gassing game
import random
import time
from colorama import Fore, init
init(autoreset=True)

numbers = list(range(1, 11))
score = 0

print("--- Welcome to the Number Guessing Game ---")
print("Rules: Guess a number between 1 and 10. Enter 0 at any time to quit.")

while True:
    # Pick a new random number at the start of every round
    computer_choice = random.choice(numbers)
    user_choice = int(input("\nEnter a number between 1 and 10: "))
    
    # Check for exit code first
    if user_choice == 0:
        break
        
    # Validate the input bounds
    if user_choice > 10 or user_choice < 1:
        print("Number should be between 1 and 10.")
        continue

    # Reveal choices
    print(f"Computer Choice: {computer_choice}")
    print(f"Your Choice: {user_choice}")

    # Check the guess
    if user_choice == computer_choice:
        print(f"🎉 {Fore.GREEN} Lucky draw! You got it right!")
        score += 1
    else:
        print(f"❌ {Fore.RED} Sorry, try again..")
    
    # Ask the user if they want to try again
    play_again = input("Do you want to try again? (yes/no): ").strip().lower()
    
    # If they say anything other than 'yes' or 'y', break the loop
    if play_again not in ['yes', 'y']:
        break

# --- Loading Animation Section ---
print("\nCalculating your final results...")
for i in range(1, 6):
    time.sleep(1)  
    print(f"\rwaiting ....{i} {Fore.LIGHTGREEN_EX}sec", end='', flush=True)

print() # This moves the cursor to a new line so the score prints perfectly below the animation

# The final score prints once outside the loop at the very end
print("\n--- Game Over ---")
print(f"Your final score is: {Fore.GREEN}{score}")
print("Thanks for playing!")
