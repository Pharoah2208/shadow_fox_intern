import random

# Hangman stages
HANGMAN = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Word list
WORDS = [
    'python', 'javascript', 'computer', 'programming', 'keyboard',
    'monitor', 'internet', 'database', 'algorithm', 'function',
    'variable', 'software', 'hardware', 'developer', 'github'
]

def get_word():
    """Pick a random word from the list."""
    return random.choice(WORDS).upper()

def get_hint(word, guessed):
    """Get a hint - reveal a random unguessed letter."""
    unguessed = [letter for letter in word if letter not in guessed]
    if unguessed:
        return random.choice(unguessed)
    return None

def display_game(wrong, word, guessed, hints_used):
    """Show current game state."""
    print("\n" + HANGMAN[wrong])
    print(f"Wrong guesses: {wrong}/{len(HANGMAN)-1}")
    print(f"Hints used: {hints_used}/2")
    
    # Show the word with guessed letters
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    
    print(f"\nWord: {display}")
    print(f"Guessed letters: {', '.join(sorted(guessed))}")

def play_game():
    """Main game function."""
    word = get_word()
    guessed = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN) - 1
    hints_used = 0
    max_hints = 2
    
    print("\n🎮 HANGMAN GAME")
    print("=" * 40)
    print("Guess the word letter by letter!")
    print(f"The word has {len(word)} letters.")
    print(f"💡 You can use up to {max_hints} hints!")
    
    # Game loop
    while wrong_guesses < max_wrong:
        display_game(wrong_guesses, word, guessed, hints_used)
        
        # Check if won
        if all(letter in guessed for letter in word):
            print("\n🎉 YOU WON! The word was:", word)
            return True
        
        # Get player input
        print("\nType a letter to guess, or 'hint' for a hint")
        guess = input("Your choice: ").upper()
        
        # Check for hint request
        if guess == 'HINT':
            if hints_used >= max_hints:
                print("❌ No hints left!")
                continue
            
            hint_letter = get_hint(word, guessed)
            if hint_letter:
                print(f"💡 Hint: The word contains the letter '{hint_letter}'")
                guessed.add(hint_letter)
                hints_used += 1
            else:
                print("⚠️ No more letters to reveal!")
            continue
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!")
            continue
        
        if guess in guessed:
            print("⚠️ You already guessed that letter!")
            continue
        
        # Add to guessed letters
        guessed.add(guess)
        
        # Check if correct
        if guess in word:
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess!")
            wrong_guesses += 1
    
    # Game over - lost
    display_game(wrong_guesses, word, guessed, hints_used)
    print("\n💀 GAME OVER! The word was:", word)
    return False

def main():
    """Run the game with play again option."""
    print("\n" + "=" * 40)
    print("     WELCOME TO HANGMAN!")
    print("=" * 40)
    
    while True:
        play_game()
        
        # Play again?
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye! 👋")
            break

# Run the game
if __name__ == "__main__":
    main()
