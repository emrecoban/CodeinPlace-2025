"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    weight = float(input("Enter a weight on Earth: "))
    result = round(weight * 37.8 / 100, 2)
    print(f"The equivalent weight on Mars: {result}")

if __name__ == "__main__":
    main()
