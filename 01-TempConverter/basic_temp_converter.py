def convert_temperature(temp, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (temp * 9/5) + 32
        elif to_unit == 'Kelvin':
            return temp + 273.15
        else:
            return temp
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (temp - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (temp - 32) * 5/9 + 273.15
        else:
            return temp
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return temp - 273.15
        elif to_unit == 'Fahrenheit':
            return (temp - 273.15) * 9/5 + 32
        else:
            return temp

def main():
    print("Temperature Converter")
    while True:
        temp = float(input("Enter the temperature (we will ask Celsius, Fahrenheit, Kelvin up next): "))
        from_unit = input("Enter the unit to convert from (Celsius, Fahrenheit, Kelvin): ")
        to_unit = input("Enter the unit to convert to (Celsius, Fahrenheit, Kelvin): ")

        if from_unit not in ['Celsius', 'Fahrenheit', 'Kelvin'] or to_unit not in ['Celsius', 'Fahrenheit', 'Kelvin']:
            print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")
            continue

        converted_temp = convert_temperature(temp, from_unit, to_unit)
        print(f"Converted Temperature: {converted_temp:.2f} {to_unit}")

        continue_choice = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using the Temperature Converter!")
            break

if __name__ == "__main__":
    main()
