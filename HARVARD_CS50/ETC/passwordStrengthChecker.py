import re

def check_password_strength(password):
    """
    Analyzes password strength based on length and character variety.
    Returns a score, a rating, and feedback.
    """
    score = 0
    feedback = []
    
    # Criterion 1: Length
    if len(password) < 8:
        feedback.append("• Make it at least 8 characters long.")
    else:
        score += 1
        
    # Criterion 2: Uppercase Letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add uppercase letters (A-Z).")

    # Criterion 3: Lowercase Letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("• Add lowercase letters (a-z).")

    # Criterion 4: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("• Add numbers (0-9).")

    # Criterion 5: Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("• Add special characters (!@#$...).")

    # Determine Rating
    if score == 5:
        rating = "STRONG"
    elif score >= 3:
        rating = "MEDIUM"
    else:
        rating = "WEAK"

    return rating, feedback

def main():
    print("--- PASSWORD STRENGTH CHECKER ---")
    while True:
        password = input("\nEnter a password to check (or 'q' to quit): ")
        
        if password.lower() == 'q':
            print("Exiting...")
            break
            
        rating, feedback = check_password_strength(password)
        
        print(f"Strength: {rating}")
        
        if feedback:
            print("Suggestions to improve:")
            for tip in feedback:
                print(tip)
        else:
            print("Great job! This is a solid password.")

if __name__ == "__main__":
    main()