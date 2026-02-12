# ---------------- SMART CAFE HELPER ----------------

# 1. Welcome Message
def welcome():
    print("Welcome to Smart Café!")
    choice = input("Would you like to customize the welcome message? (yes/no): ").lower()

    if choice == "yes":
        msg = input("Enter your custom message: ")
        transformed = "...".join(msg)
        print("Transformed welcome message:")
        print(transformed)
    print()


# 2. Order Handling + Emoji
def handle_order(order):
    o = order.lower()

    if "cake" in o:
        print("Okay, I will prepare cake 🍰")
    elif "coffee" in o:
        print("Okay, I will prepare coffee ☕")
    elif "tea" in o:
        print("Okay, I will prepare tea 🍵")
    elif "patat" in o:
        print("Okay, I will prepare patat 🍟")
    elif "cookie" in o:
        print("Okay, I will prepare cookie 🍪")
    elif "sandwich" in o:
        print("Okay, I will prepare sandwich 🥪")
    else:
        print("Okay, I will prepare", order.lower())


# 3. Energy Calculation
def energy_calc():
    choice = input("Would you like to calculate energy? (yes/no): ").lower()

    if choice == "yes":
        m = float(input("Enter the weight in grams: "))
        c = 300000000
        E = m * (c ** 2)
        print(f"Energy: {E:.2e} Joules.")
    return


# 4. Main Program
def main():
    welcome()

    total = 0

    while True:
        order = input("Please enter your order or type 'done' to finish: ")

        if order.lower() == "done":
            break

        handle_order(order)
        energy_calc()

        price = float(input("Enter the price of this item: $"))
        total += price
        print()

    print(f"Your total is ${total:.2f}.")
    tip_percent = int(input("How much tip would you like to add? (10, 15, 20): "))

    tip = total * tip_percent / 100
    final_total = total + tip

    print(f"With tip, your total is: ${final_total:.2f}")
    print("Thank you for visiting Smart Café!")


# Run
main()
