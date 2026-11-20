import sys
temp = int(input("Enter the Temperature: "))
def fah(temp):
    return (temp * 9 / 5) + 32
print("Temperature in Fahrenheit:", fah(temp))