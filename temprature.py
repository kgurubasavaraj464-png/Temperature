
import sys

def fah(temp):
    return (temp * 9 / 5) + 32


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python temperature.py <temperature>")
        sys.exit(1)

    try:
        temp = int(sys.argv[1])
        result = fah(temp)
        print("Temperature in Fahrenheit:", result)

    except ValueError:
        print("Error: Please enter a valid temperature.")
        sys.exit(1)
