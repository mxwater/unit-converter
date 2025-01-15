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
        print("\n1. Convert Temperature (F to C)")
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
            break
        else:
            print("Invalid choice. Try again.")
