import random
import string
import sys # Needed for sys.exit() if using the advanced length check

def get_password_length():
    """Prompts the user for the desired password length and validates the input."""
    while True:
        try:
            length_str = input("Enter the desired password length (e.g., 12): ")
            length = int(length_str)
            if length > 0:
                return length
            else:
                print("Password length must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number for the length.")
        # Optional: Add a way to exit if the user keeps entering invalid input
        # except KeyboardInterrupt:
        #     print("\nOperation cancelled by user.")
        #     sys.exit() # Exit the script cleanly

def generate_password(length):
    """Generates a random password of the specified length."""
    # Define the character sets to use
    lowercase_letters = string.ascii_lowercase  # abcdef...
    uppercase_letters = string.ascii_uppercase  # ABCDEF...
    digits = string.digits                     # 012345...
    symbols = string.punctuation               # !@#$%^&*()...

    # Combine all character sets into one large pool
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # --- Password Generation ---
    # Method 1: Simple random choice for each character (allows repeats)
    # This is generally preferred for passwords as it increases randomness.
    password_list = [random.choice(all_characters) for _ in range(length)]
    password = "".join(password_list)

    # --- Alternative Method 2: Ensure at least one of each type ---
    # (More complex, sometimes requested, but slightly less random overall)
    # if length < 4: # Need at least 4 characters for this method
    #     print("Warning: Length too short to guarantee all character types. Using simple generation.")
    #     password_list = [random.choice(all_characters) for _ in range(length)]
    # else:
    #     password_list = [
    #         random.choice(lowercase_letters),
    #         random.choice(uppercase_letters),
    #         random.choice(digits),
    #         random.choice(symbols),
    #     ]
    #     # Fill the rest of the length with random choices from the full set
    #     remaining_length = length - 4
    #     password_list.extend([random.choice(all_characters) for _ in range(remaining_length)])
    #     # Shuffle the list to make the position of guaranteed characters random
    #     random.shuffle(password_list)
    # password = "".join(password_list)
    # --- End of Alternative Method ---

    return password

# --- Main Program ---
print("--- Password Generator ---")

# 1. Get User Input for Length
password_length = get_password_length()

# 2. Generate Password
if password_length: # Proceed only if a valid length was obtained
    generated_password = generate_password(password_length)

    # 3. Display the Password
    print("\nGenerating password...")
    print(f"Generated Password ({password_length} characters): {generated_password}")

print("\n--- Generation Complete ---")