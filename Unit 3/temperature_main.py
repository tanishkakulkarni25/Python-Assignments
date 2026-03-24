from temperature.celsius_to_fahrenheit import celsius_to_fahrenheit
from temperature.fahrenheit_to_celsius import fahrenheit_to_celsius
from temperature.celsius_to_kelvin import celsius_to_kelvin

def main():
    print("Choose a conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    try:
        num = float(input("Enter temperature: "))
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            print(f"{num}°C = {celsius_to_fahrenheit(num)}°F")

        elif choice == 2:
            print(f"{num}°F = {fahrenheit_to_celsius(num)}°C")

        elif choice == 3:
            print(f"{num}°C = {celsius_to_kelvin(num)}K")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()