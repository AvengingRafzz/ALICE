# File to play games with ALICE

# Import necessary modules
import ai_speak  # Module for AI voice output
import random  # Module for random number generation


# Function to play Rock Paper Scissor game
def play_rps():
    # Print welcome message and instructions
    print("Welcome to Rock Paper Scissor Game!")
    ai_speak.speak("Welcome to Rock Paper Scissor Game!")
    options = ['rock', 'paper', 'scissor']
    # Get user's choice
    user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()
    ai_choice = random.choice(options)

    print(f"AI chose: {ai_choice}")

    if user_choice not in options:
        print("Invalid choice. Please choose either rock, paper, or scissor.")
        ai_speak.speak("Invalid choice. Please choose either rock, paper, or scissor.")
        return

    # Determine winner
    if user_choice == ai_choice:
        print("It's a tie!")
        ai_speak.speak("It's a tie!")
    elif (user_choice == 'rock' and ai_choice == 'scissor') or \
            (user_choice == 'paper' and ai_choice == 'rock') or \
            (user_choice == 'scissor' and ai_choice == 'paper'):
        print("You win!")
        ai_speak.speak("You win!")
    else:
        print("AI wins!")
        ai_speak.speak("AI wins!")


# Function to play Number Guessing Game
def play_ngg():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    ai_speak.speak("Welcome to the Number Guessing Game!")
    ai_speak.speak("I'm thinking of a number between 1 and 100. Can you guess it?")

    secret_number = random.randint(1, 100)
    attempts = 0

    # Loop until user guesses the correct number
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
            ai_speak.speak("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
            ai_speak.speak("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            ai_speak.speak(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break


# Function to choose a word for Hangman game
def choose_word():
    words = ["python", "programming", "hangman", "computer", "code", "alice", "rafan", "mehul"]
    return random.choice(words)


# Function to display the word in Hangman game
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


# Function to play Hangman game
def play_hangman():
    print("Welcome to Hangman!")
    ai_speak.speak("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 10

    # Loop until user guesses the word or runs out of attempts
    while attempts > 0:
        print(display_word(word, guessed_letters))
        ai_speak.speak(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            ai_speak.speak("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            ai_speak.speak("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess not in word:
            attempts -= 1
            print(f"Incorrect guess! You have {attempts} attempts left.")
            ai_speak.speak(f"Incorrect guess! You have {attempts} attempts left.")
            if attempts == 0:
                print(f"Sorry, you ran out of attempts. The word was '{word}'.")
                ai_speak.speak(f"Sorry, you ran out of attempts. The word was '{word}'.")
                break
        else:
            print("Correct guess!")
            ai_speak.speak("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word '{word}' correctly!")
                ai_speak.speak(f"Congratulations! You guessed the word '{word}' correctly!")
                break
