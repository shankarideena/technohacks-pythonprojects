def get_temp_choice():
    temp_choice = input("Press 'f' to convert Fahrenheit to Celsius or 'c' to convert Celsius to Fahrenheit: ")
    return temp_choice.lower()

def convert_temp():
    temp_choice = get_temp_choice()

    while temp_choice not in ['f', 'c']:
        print("Invalid choice. Please try again.")
        temp_choice = get_temp_choice()

    if temp_choice == 'f':
        temp_in_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        temp_in_celsius = (temp_in_fahrenheit - 32) * 5 / 9
        print(f"{temp_in_fahrenheit} Fahrenheit is equal to {temp_in_celsius} Celsius")

    else:
        temp_in_celsius = float(input("Enter the temperature in Celsius: "))
        temp_in_fahrenheit = temp_in_celsius * 9 / 5 + 32
        print(f"{temp_in_celsius} Celsius is equal to {temp_in_fahrenheit} Fahrenheit")

def main():
    while True:
        convert_temp()

        cont = input("Press 'q' to quit or any other key to continue: ")
        if cont.lower() == 'q':
            break

if _name_ == "_main_":
    main()