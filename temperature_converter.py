# Temperature Conversion Program

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(c):
    return c + 273.15

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(k):
    return k - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Main program
def main():
    print("Welcome to the Temperature Conversion Program!")
    
    # User input
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    
    # Conversion logic
    if unit == "C":
        print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F and {celsius_to_kelvin(temp):.2f}K")
    elif unit == "F":
        print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C and {fahrenheit_to_kelvin(temp):.2f}K")
    elif unit == "K":
        print(f"{temp}K is {kelvin_to_celsius(temp):.2f}°C and {kelvin_to_fahrenheit(temp):.2f}°F")
    else:
        print("Invalid unit! Please enter C, F, or K.")

# Run the program
if __name__ == "__main__":
    main()