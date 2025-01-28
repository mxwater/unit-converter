from flask import Flask, request, render_template

app = Flask(__name__)

def convert_temperature():
    print("\nConvert Temperature: Fahrenheit to Celsius")
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    temp_c = (temp_f - 32) * 5 / 9
    print(f"{temp_f}°F is {temp_c:.2f}°C")

def convert_weight():
    print("\nConvert Weight: Pounds to Kilograms")
    weight_lbs = float(input("Enter weight in pounds: "))
    weight_kg = weight_lbs * 0.453592
    print(f"{weight_lbs} lbs is {weight_kg:.2f} kg")

def convert_volume():
    print("\nConvert Volume: Ounces to Milliliters")
    volume_oz = float(input("Enter volume in ounces: "))
    volume_ml = volume_oz * 29.5735
    print(f"{volume_oz} oz is {volume_ml:.2f} ml")

def convert_distance():
    print("\nConvert Distance: Miles to Kilometers")
    distance_miles = float(input("Enter distance in miles: "))
    distance_km = distance_miles * 1.60934
    print(f"{distance_miles} miles is {distance_km:.2f} km")

def main():
    while True:
        print("\nWelcome to the Unit Converter App!")
        print("1. Convert Temperature (F to C)")
        print("2. Convert Weight (lbs to kg)")
        print("3. Convert Volume (oz to ml)")
        print("4. Convert Distance (miles to km)")
        print("5. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            convert_temperature()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_volume()
        elif choice == "4":
            convert_distance()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
