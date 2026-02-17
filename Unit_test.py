import math

# ========== CORE FUNCTIONS (used in unit tests) ==========

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32


def is_even(number: int) -> bool:
    return number % 2 == 0


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return math.factorial(n)


def reverse_string(text: str) -> str:
    return text[::-1]


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# ========== SAFE INPUT HELPERS ==========

def input_float(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("❌ Invalid input. Please enter a NUMBER (example: 36.6)")


def input_int(prompt, allow_negative=True):
    while True:
        value = input(prompt)
        try:
            num = int(value)
            if not allow_negative and num < 0:
                print("❌ Please enter a NON-NEGATIVE integer (0, 1, 2, ...)")
                continue
            return num
        except ValueError:
            print("❌ Invalid input. Please enter an INTEGER (example: 5)")


# ========== MENU PROGRAMS (user interaction) ==========

def run_celsius():
    c = input_float("Enter Celsius: ")
    print("Fahrenheit:", celsius_to_fahrenheit(c))


def run_even_odd():
    n = input_int("Enter integer number: ")
    print("Even" if is_even(n) else "Odd")


def run_factorial():
    n = input_int("Enter NON-NEGATIVE integer: ", allow_negative=False)
    try:
        print("Factorial:", factorial(n))
    except ValueError as e:
        print("Error:", e)


def run_reverse():
    text = input("Enter text: ")
    if not text:
        print("❌ Input cannot be empty")
        return
    print("Reversed:", reverse_string(text))


def run_prime():
    n = input_int("Enter integer number: ")
    print("Prime" if is_prime(n) else "Not prime")


# ========== MAIN MENU ==========

def main():
    while True:
        print("\nChoose program:")
        print("1. Celsius → Fahrenheit")
        print("2. Even or Odd")
        print("3. Factorial Calculator")
        print("4. Reverse String")
        print("5. Prime Number Checker")
        print("0. Exit")

        choice = input("Enter number: ").strip()

        if choice == "1":
            run_celsius()
        elif choice == "2":
            run_even_odd()
        elif choice == "3":
            run_factorial()
        elif choice == "4":
            run_reverse()
        elif choice == "5":
            run_prime()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("❌ Invalid choice. Please enter number 0–5")


if __name__ == "__main__":
    main()
