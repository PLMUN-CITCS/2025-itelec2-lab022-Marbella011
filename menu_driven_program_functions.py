def display_menu():
    print("\nMenu:")
    print("1. Greet User")
    print("2. Even/Odd Checker")
    print("3. Exit")

def greet_user():
    print("\nHello! Welcome to the program.")

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def even_odd_checker_action():
    while True:
        try:
            num = int(input("Enter an integer: "))
            print(check_even_odd(num))
            break  # Exit the inner loop after successful check
        except ValueError:
            print("Invalid input. Please enter an integer.")


def handle_menu_choice(choice):
    if choice == 1:
        greet_user()
        return False  # Continue the main loop
    elif choice == 2:
        even_odd_checker_action()
        return False  # Continue the main loop
    elif choice == 3:
        print("Exiting program...")
        return True  # Terminate the main loop
    else:
        print("Invalid choice. Please try again.")
        return False  # Continue the main loop


def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
    
