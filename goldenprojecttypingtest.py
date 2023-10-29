import random
import time

# Function to get a random word for typing
def get_random_word():
    words = ["python", "programming", "challenge", "keyboard", "developer", "speed", "typing", "test", "code"]
    return random.choice(words)

# Function to conduct the speed typing test
def speed_typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    # Get a random word for typing
    word_to_type = get_random_word()
    print(f"\nType the word: {word_to_type}")

    # Record the start time
    start_time = time.time()

    # User types the word
    user_input = input("Your typing: ")

    # Record the end time
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    # Check if the user input matches the random word
    if user_input.strip().lower() == word_to_type:
        # Calculate and display typing speed
        word_per_minute = len(word_to_type) / elapsed_time * 60
        print(f"\nCongratulations! Your typing speed: {word_per_minute:.2f} words per minute.")
    else:
        # Display if the input is incorrect
        print("\nIncorrect. Try again.")

# Run the speed typing test when the script is executed
if __name__ == "__main__":
    speed_typing_test()


