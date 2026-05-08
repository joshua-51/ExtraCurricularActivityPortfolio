import random
import string

def load_words():
    try:
        # Common path for dictionary on Unix-based systems
        with open('/usr/share/dict/words', 'r') as f:
            return set(word.strip().lower() for word in f if len(word.strip()) > 2)
    except FileNotFoundError:
        print("Note: System dictionary not found. Using a small local fallback.")
        return {"python", "coding", "language", "game", "apple", "banana", "bread"}

def generate_letters(count=10):
    #Generates a mix of vowels and consonants for playability.
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    
    # Ensure at least 3 vowels so the player can actually make words
    hand = [random.choice(vowels) for _ in range(3)]
    hand += [random.choice(consonants) for _ in range(count - 3)]
    random.shuffle(hand)
    return hand

def play_game():
    dictionary = load_words()
    game_letters = generate_letters(9)
    score = 0
    found_words = set()

    print("--- MEGA WORD SCRAMBLE ---")
    print(f"YOUR LETTERS: {' '.join(game_letters).upper()}")
    print("Commands: 'quit' to exit, 'score' to check points.\n")

    while True:
        guess = input("Enter word: ").strip().lower()

        if guess == 'quit':
            break
        if guess == 'score':
            print(f"Current Score: {score}")
            continue
        
        # Check if the user is reusing a word
        if guess in found_words:
            print("Already found that one!")
            continue

        # Check if the word is in our loaded dictionary
        if guess not in dictionary:
            print("That's not a recognized word.")
            continue

        # Check if the word can be built from the hand
        temp_hand = game_letters.copy()
        is_valid = True
        for letter in guess:
            if letter in temp_hand:
                temp_hand.remove(letter)
            else:
                is_valid = False
                break
        
        if is_valid:
            # Scoring Logic
            length = len(guess)
            points = length * 10 if length < 5 else length * 20
            score += points
            found_words.add(guess)
            print(f"Nice! '{guess.upper()}' is worth {points} points.")
        else:
            print(f"You can't make '{guess}' with those letters!")

    print("\n" + "="*20)
    print(f"FINAL SCORE: {score}")
    print(f"WORDS FOUND: {', '.join(sorted(found_words))}")
    print("="*20)

if __name__ == "__main__":
    play_game()