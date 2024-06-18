def show_menu():
    print("Unit Conversion Menu:")
    print("1. Millimeters to Centimeters (mm to cm)")
    print("2. Feet to Meters (ft to m)")
    print("3. Inches to Centimeters (in to cm)")
    print("4. Pounds to Kilograms (lbs to kg)")
    print("5. Gallons to Liters (gal to l)")
    print("6. Grams to Kilograms (g to kg)")
    print("7. Kilograms to Pounds (kg to lbs)")
    print("8. Celsius to Fahrenheit (°C to °F)")
    print("9. Fahrenheit to Celsius (°F to °C)")

def mm_to_cm(mm):
    return mm / 10

def ft_to_m(ft):
    return ft * 0.3048

def in_to_cm(inches):
    return inches * 2.54

def lbs_to_kg(lbs):
    return lbs * 0.453592

def gal_to_l(gal):
    return gal * 3.78541

def g_to_kg(g):
    return g / 1000

def kg_to_lbs(kg):
    return kg * 2.20462

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_units(choice, value):
    if choice == 1:
        return mm_to_cm(value)
    elif choice == 2:
        return ft_to_m(value)
    elif choice == 3:
        return in_to_cm(value)
    elif choice == 4:
        return lbs_to_kg(value)
    elif choice == 5:
        return gal_to_l(value)
    elif choice == 6:
        return g_to_kg(value)
    elif choice == 7:
        return kg_to_lbs(value)
    elif choice == 8:
        return c_to_f(value)
    elif choice == 9:
        return f_to_c(value)
    else:
        return None

def main():
    while True:
        show_menu()
        choice = int(input("Enter your choice (1-9) or 0 to exit: "))
        if choice == 0:
            print("Exiting the program.")
            break
        value = float(input("Enter the value to be converted: "))
        result = convert_units(choice, value)
        if result is not None:
            print(f"Converted value: {result}")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()