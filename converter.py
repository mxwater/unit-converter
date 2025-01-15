

def convert_weight():
    print("\nConvert Weight: Pounds to Kilograms")
    weight_lbs = float(input("Enter weight in pounds: "))
    weight_kg = weight_lbs * 0.453592
    print(f"{weight_lbs} lbs is {weight_kg:.2f} kg")

def convert_temperature():
    print("\nConvert Temperature: Fahrenheit to Celsius")
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    temp_c = (temp_f - 32) * 5 / 9
    print(f"{temp_f}°F is {temp_c:.2f}°C")

def main():
    while True:
        print("\n1. Convert Temperature (F to C)")
        print("2. Convert Weight (lbs to kg)")
        print("3. Convert Volume (oz to ml)")
        print("4. Convert Distance (miles to km)")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            convert_temperature()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

