import math

# ========== CORE FUNCTIONS ==========

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32


def is_even(number: int) -> bool:
    """Return True if number is even, else False"""
    return number % 2 == 0


def factorial(n: int) -> int:
    """Return factorial of n (0! = 1). Raises ValueError for negative."""
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return math.factorial(n)


def reverse_string(text: str) -> str:
    """Return reversed string"""
    return text[::-1]


def is_prime(n: int) -> bool:
    """Return True if n is prime, else False"""
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


# ========== MENU PROGRAMS (user interaction) ==========

def run_celsius():
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(c))


def run_even_odd():
    n = int(input("Enter number: "))
    print("Even" if is_even(n) else "Odd")


def run_factorial():
    n = int(input("Enter non-negative integer: "))
    try:
        print("Factorial:", factorial(n))
    except ValueError as e:
        print("Error:", e)


def run_reverse():
    text = input("Enter text: ")
    print("Reversed:", reverse_string(text))


def run_prime():
    n = int(input("Enter number: "))
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
            print("Invalid choice")


if __name__ == "__main__":
    main()
