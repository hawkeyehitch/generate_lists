import itertools

def get_input(prompt):
    return input(prompt)

def generate_usernames(first_names, last_names, years):
    usernames = []
    for first, last, year in itertools.product(first_names, last_names, years):
        usernames.append(f"{first}{last}{year}")
    return usernames

def generate_passwords(words, numbers, special_chars):
    passwords = []
    for word, num, char in itertools.product(words, numbers, special_chars):
        passwords.append(f"{word}{num}{char}")
    return passwords

def save_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item}\n")

def main():
    print("Custom Username and Password List Generator")

    # Get user input for username components
    first_names = get_input("Enter first names (comma separated): ").split(',')
    last_names = get_input("Enter last names (comma separated): ").split(',')
    years = get_input("Enter years (comma separated): ").split(',')

    # Generate usernames
    usernames = generate_usernames(first_names, last_names, years)
    print(f"Generated {len(usernames)} usernames.")

    # Get user input for password components
    words = get_input("Enter words (comma separated): ").split(',')
    numbers = get_input("Enter numbers (comma separated): ").split(',')
    special_chars = get_input("Enter special characters (comma separated): ").split(',')

    # Generate passwords
    passwords = generate_passwords(words, numbers, special_chars)
    print(f"Generated {len(passwords)} passwords.")

    # Save to files
    username_file = get_input("Enter the filename to save usernames: ")
    password_file = get_input("Enter the filename to save passwords: ")

    save_to_file(username_file, usernames)
    save_to_file(password_file, passwords)

    print("Usernames and passwords have been saved.")

if __name__ == "__main__":
    main()
