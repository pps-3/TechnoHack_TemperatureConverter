# Display the menu
print("Temperature Converter")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
print("3. Exit")

while True:
    # Get user's choice
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        # Convert Celsius to Fahrenheit
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")

    elif choice == '2':
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius}°C")

    elif choice == '3':
        # Exit the program
        print("Exiting the converter. Goodbye!")
        break

    else:
        # Handle invalid input
        print("Invalid choice! Please enter 1, 2, or 3.")
