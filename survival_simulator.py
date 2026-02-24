import random

# ---------------------------
# GLOBAL GAME STATE
# ---------------------------

tasks_completed = {
    "file_extension": False,
    "math_vault": False,
    "nutrition": False,
    "coke_machine": False,
    "camelcase": False,
    "outdated": False,
    "guessing_game": False,
    "bitcoin": False,
    "emojize": False,
    "taqueria": False,
    "letters": False
}


# ---------------------------
# HELPER FUNCTIONS
# ---------------------------

def safe_int_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ Please enter a valid NUMBER.")


def press_enter():
    input("\nPress Enter to return to menu...")


# ---------------------------
# 1. FILE EXTENSION
# ---------------------------

def file_extension_task():
    print("\nYou found a mysterious file: list.recipe")
    answer = input("What type of file is this? ").lower()

    if "recipe" in answer:
        print("✅ Correct! It contains recipes.")
        tasks_completed["file_extension"] = True
    else:
        print("❌ Incorrect. Think about the extension.")

    press_enter()


# ---------------------------
# 2. MATH VAULT
# ---------------------------

def math_vault_task():
    print("\nA vault asks: 2 + 3 * 4 = ?")
    answer = safe_int_input("Enter answer: ")

    if answer == 14:
        print("✅ Correct! Order of operations matters.")
        tasks_completed["math_vault"] = True
    else:
        print("❌ Wrong! Remember multiplication comes first.")

    press_enter()


# ---------------------------
# 3. NUTRITION
# ---------------------------

def nutrition_task():
    print("\nYou need exactly 500 calories to gain strength.")

    foods = {
        "apple": 95,
        "sandwich": 250,
        "chocolate": 200,
        "chips": 150
    }

    total = 0

    while total < 500:
        print("\nAvailable foods:")
        for food in foods:
            print(f"- {food} ({foods[food]} cal)")

        choice = input("Choose food: ").lower()

        if choice in foods:
            total += foods[choice]
            print(f"Total calories: {total}")
        else:
            print("❌ Invalid food.")

        if total > 500:
            print("❌ Too many calories! Try again.")
            press_enter()
            return

    if total == 500:
        print("✅ Perfect energy level!")
        tasks_completed["nutrition"] = True

    press_enter()


# ---------------------------
# 4. COKE MACHINE
# ---------------------------

def coke_machine_task():
    print("\nThe coke machine requires the code: 1 0 2")

    code = input("Enter button sequence separated by spaces: ")

    if code.strip() == "1 0 2":
        print("✅ The machine works! You get a drink.")
        tasks_completed["coke_machine"] = True
    else:
        print("❌ Wrong sequence.")

    press_enter()


# ---------------------------
# 5. CAMELCASE
# ---------------------------

def camelcase_task():
    print("\nEncrypted message: YouMustEscapeNow")

    answer = input("Decrypt it (add spaces): ").lower().strip()

    if answer == "you must escape now":
        print("✅ Message decrypted!")
        tasks_completed["camelcase"] = True
    else:
        print("❌ Incorrect format.")

    press_enter()


# ---------------------------
# 6. OUTDATED (FIXED)
# ---------------------------

def outdated_task():
    print("\nYou must remove expired products from the shelves.")

    groceries = [
        ("Milk", 2024),
        ("Beans", 2027),
        ("Yogurt", 2023),
        ("Rice", 2028)
    ]

    current_year = 2026

    print("\nProducts:")
    for item in groceries:
        print(f"- {item[0]} (expires {item[1]})")

    expired_products = [item[0].lower() for item in groceries if item[1] < current_year]
    removed = []

    while True:
        choice = input("\nEnter expired product to remove (or type done): ").lower()

        if choice == "done":
            break

        if choice in expired_products and choice not in removed:
            print("✅ Correct! Product removed.")
            removed.append(choice)
        elif choice in removed:
            print("⚠ Already removed.")
        else:
            print("❌ That product is not expired.")

    if set(removed) == set(expired_products):
        print("\n🎉 All expired products removed!")
        tasks_completed["outdated"] = True
    else:
        print("\n❌ You did not remove all expired products.")

    press_enter()


# ---------------------------
# 7. GUESSING GAME
# ---------------------------

def guessing_game_task():
    secret = random.randint(1, 10)
    print("\nGuess the secret number (1-10)")

    while True:
        guess = safe_int_input("Your guess: ")

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("✅ Correct!")
            tasks_completed["guessing_game"] = True
            break

    press_enter()


# ---------------------------
# 8. BITCOIN
# ---------------------------

def bitcoin_task():
    estimated_price = random.randint(20000, 70000)
    print(f"\nBitcoin estimated price: ${estimated_price}")

    choice = input("Buy? (yes/no): ").lower()

    if choice == "yes":
        print("You invested! Hope it goes up.")
    else:
        print("You stayed safe.")

    tasks_completed["bitcoin"] = True
    press_enter()


# ---------------------------
# 9. EMOJIZE
# ---------------------------

def emojize_task():
    print("\nClue: 🍎🍪")

    answer = input("What does this mean? ").lower()

    if "fruit" in answer and "cookie" in answer:
        print("✅ Correct!")
        tasks_completed["emojize"] = True
    else:
        print("❌ Not quite.")

    press_enter()


# ---------------------------
# 10. TAQUERIA
# ---------------------------

def taqueria_task():
    print("\nCreate taco ingredients list.")

    needed = {"tortilla", "meat", "cheese"}
    user_list = set()

    while True:
        item = input("Add ingredient (type done to finish): ").lower()

        if item == "done":
            break

        user_list.add(item)

    if needed.issubset(user_list):
        print("✅ Taco complete!")
        tasks_completed["taqueria"] = True
    else:
        print("❌ Missing ingredients.")

    press_enter()


# ---------------------------
# 11. LETTER PUZZLE
# ---------------------------

def letters_task():
    print("\nFind a 5-letter word containing 'a'")

    word = input("Enter word: ").lower()

    if len(word) == 5 and "a" in word:
        print("✅ Valid word!")
        tasks_completed["letters"] = True
    else:
        print("❌ Invalid.")

    press_enter()


# ---------------------------
# 12. VIEW PROGRESS
# ---------------------------

def view_progress():
    print("\n====== YOUR PROGRESS ======\n")

    total = len(tasks_completed)
    completed = 0

    for task, status in tasks_completed.items():
        name = task.replace("_", " ").title()

        if status:
            print(f"✅ {name}")
            completed += 1
        else:
            print(f"❌ {name}")

    percent = (completed / total) * 100
    print(f"\nProgress: {completed}/{total} tasks completed")
    print(f"Completion: {percent:.1f}%")

    press_enter()


# ---------------------------
# FAREWELL
# ---------------------------

def farewell():
    print("\n🎉 YOU ESCAPED THE SUPERMARKET!")
    print("Goodbye abandoned shelves...")
    print("Goodbye expired milk...")
    print("Goodbye broken coke machine...")
    print("I will never forget this strange place!")


# ---------------------------
# MENU SYSTEM
# ---------------------------

def menu():
    while True:
        print("\n====== SURVIVAL SIMULATOR ======")
        print("1. File Extension")
        print("2. Math Vault")
        print("3. Nutrition")
        print("4. Coke Machine")
        print("5. CamelCase")
        print("6. Outdated")
        print("7. Guessing Game")
        print("8. Bitcoin")
        print("9. Emojize")
        print("10. Taqueria")
        print("11. Letter Puzzle")
        print("12. View Progress")
        print("0. Exit")

        choice = safe_int_input("Choose option: ")

        if choice == 1:
            file_extension_task()
        elif choice == 2:
            math_vault_task()
        elif choice == 3:
            nutrition_task()
        elif choice == 4:
            coke_machine_task()
        elif choice == 5:
            camelcase_task()
        elif choice == 6:
            outdated_task()
        elif choice == 7:
            guessing_game_task()
        elif choice == 8:
            bitcoin_task()
        elif choice == 9:
            emojize_task()
        elif choice == 10:
            taqueria_task()
        elif choice == 11:
            letters_task()
        elif choice == 12:
            view_progress()
        elif choice == 0:
            break
        else:
            print("❌ Invalid option.")

        if all(tasks_completed.values()):
            farewell()
            break


# ---------------------------
# START GAME
# ---------------------------

menu()