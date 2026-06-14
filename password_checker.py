
import re
import math
import getpass


# Common weak passwords list

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "password1", "111111", "letmein", "iloveyou", "admin",
    "welcome", "monkey", "dragon", "master", "sunshine",
    "princess", "shadow", "superman", "michael", "football"
]



# Calculate entropy of the password

def calculate_entropy(password):
    """
    Entropy = length * log2(character_pool_size)
    Higher entropy = harder to brute-force.
    """
    pool = 0
    if re.search(r'[a-z]', password):
        pool += 26   # lowercase letters
    if re.search(r'[A-Z]', password):
        pool += 26   # uppercase letters
    if re.search(r'\d', password):
        pool += 10   # digits
    if re.search(r'[!@#$%^&*(),.?":{}|<>_\-\[\]\\\/\']', password):
        pool += 32   # special characters

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)



# Check individual criteria

def check_criteria(password):
    """
    Returns a dictionary of criterion -> (passed: bool, message: str)
    """
    criteria = {}

    # 1. Minimum length
    criteria['length'] = (
        len(password) >= 8,
        f"Length: {len(password)} characters (minimum 8)"
    )

    # 2. Uppercase letter
    criteria['uppercase'] = (
        bool(re.search(r'[A-Z]', password)),
        "Contains uppercase letter (A-Z)"
    )

    # 3. Lowercase letter
    criteria['lowercase'] = (
        bool(re.search(r'[a-z]', password)),
        "Contains lowercase letter (a-z)"
    )

    # 4. Digit
    criteria['digit'] = (
        bool(re.search(r'\d', password)),
        "Contains digit (0-9)"
    )

    # 5. Special character
    criteria['special'] = (
        bool(re.search(r'[!@#$%^&*(),.?":{}|<>_\-\[\]\\\/\']', password)),
        "Contains special character (!@#$...)"
    )

    # 6. Not a common password
    criteria['not_common'] = (
        password.lower() not in COMMON_PASSWORDS,
        "Not a commonly used password"
    )

    # 7. No repeated characters (e.g., "aaa", "111")
    criteria['no_repeat'] = (
        not bool(re.search(r'(.)\1{2,}', password)),
        "No repeated characters (e.g., aaa, 111)"
    )

    # 8. No sequential characters (e.g., "abc", "123")
    has_seq = False
    for i in range(len(password) - 2):
        if (ord(password[i+1]) == ord(password[i]) + 1 and
                ord(password[i+2]) == ord(password[i]) + 2):
            has_seq = True
            break
    criteria['no_sequence'] = (
        not has_seq,
        "No sequential characters (e.g., abc, 123)"
    )

    return criteria



# Calculate strength score and label

def calculate_strength(criteria, entropy):
    """
    Score is based on criteria passed + entropy bonus.
    Returns: score (0-100), label, color hint
    """
    passed = sum(1 for v in criteria.values() if v[0])
    total = len(criteria)

    # Base score from criteria (max 80)
    base_score = (passed / total) * 80

    # Entropy bonus (max 20)
    entropy_bonus = min(entropy / 6, 20)

    score = round(base_score + entropy_bonus)
    score = min(score, 100)

    # Strength label
    if score < 20:
        label = "Very Weak"
        symbol = "🔴"
    elif score < 40:
        label = "Weak"
        symbol = "🟠"
    elif score < 60:
        label = "Moderate"
        symbol = "🟡"
    elif score < 80:
        label = "Strong"
        symbol = "🟢"
    else:
        label = "Very Strong"
        symbol = "✅"

    return score, label, symbol



# Display results

def display_results(password, criteria, score, label, symbol, entropy):
    """Prints a formatted analysis report."""
    print("\n" + "=" * 50)
    print("       PASSWORD STRENGTH ANALYSIS REPORT")
    print("=" * 50)

    # Masked password display
    masked = password[0] + "*" * (len(password) - 2) + password[-1] if len(password) > 2 else "***"
    print(f"\n  Password : {masked}")
    print(f"  Length   : {len(password)} characters")
    print(f"  Entropy  : {entropy} bits")

    print("\n  ── Criteria Check ──")
    for key, (passed, message) in criteria.items():
        status = "✔" if passed else "✘"
        print(f"  [{status}] {message}")

    print(f"\n  ── Strength Score ──")
    # Visual progress bar
    filled = int(score / 5)
    bar = "█" * filled + "░" * (20 - filled)
    print(f"  [{bar}] {score}/100")
    print(f"\n  Result : {symbol}  {label}")

    # Suggestions
    print("\n  ── Suggestions ──")
    suggestions = []
    if not criteria['length'][0]:
        suggestions.append("  → Use at least 8 characters (12+ recommended)")
    if not criteria['uppercase'][0]:
        suggestions.append("  → Add uppercase letters (A-Z)")
    if not criteria['lowercase'][0]:
        suggestions.append("  → Add lowercase letters (a-z)")
    if not criteria['digit'][0]:
        suggestions.append("  → Include numbers (0-9)")
    if not criteria['special'][0]:
        suggestions.append("  → Add special characters (!@#$%...)")
    if not criteria['not_common'][0]:
        suggestions.append("  → Avoid commonly used passwords")
    if not criteria['no_repeat'][0]:
        suggestions.append("  → Avoid repeating the same character 3+ times")
    if not criteria['no_sequence'][0]:
        suggestions.append("  → Avoid sequential characters (abc, 123)")

    if suggestions:
        for s in suggestions:
            print(s)
    else:
        print("  → Your password meets all criteria. Great job!")

    print("=" * 50)



# Main function

def main():
    print("=" * 50)
    print("       PASSWORD STRENGTH CHECKER")
    print("       CodTech Internship Project")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Check a password")
        print("  2. Exit")
        choice = input("\nEnter choice (1/2): ").strip()

        if choice == "2":
            print("\nGoodbye! Stay secure. 🔐\n")
            break

        elif choice == "1":
            # Use getpass to hide input (won't echo in terminal)
            try:
                password = getpass.getpass("\nEnter password (input hidden): ")
            except Exception:
                password = input("\nEnter password: ")

            if not password:
                print("  ⚠ Password cannot be empty.")
                continue

            # Run analysis
            criteria = check_criteria(password)
            entropy = calculate_entropy(password)
            score, label, symbol = calculate_strength(criteria, entropy)

            # Display report
            display_results(password, criteria, score, label, symbol, entropy)

            again = input("\n  Check another password? (y/n): ").strip().lower()
            if again != 'y':
                print("\nGoodbye! Stay secure. 🔐\n")
                break
        else:
            print("  Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
