from temperature import celsius_to_fahrenheit
from temperature import fahrenheit_to_celsius
from temperature import celsius_to_kelvin

def temperature_main():
    print("Choose a conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")

    try:
        num = float(input("Enter temperature: "))
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            print("Celsius to Fahrenheit:", num, "=", celsius_to_fahrenheit.convert_to_fahrenheit(num))

        elif choice == 2:
            print("Fahrenheit to Celsius:", num, "=", fahrenheit_to_celsius.convert_to_celsius(num))

        elif choice == 3:
            print("Celsius to Kelvin:", num, "=", celsius_to_kelvin.convert_to_kelvin(num))

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    temperature_main()
