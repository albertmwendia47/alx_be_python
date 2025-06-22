FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# Function to convert F to C
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert C to F
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Ask user for input
temperature = input("Enter the temperature: ")
unit = input("Is it in Celsius or Fahrenheit? (C/F): ").upper()

# Check if input is a number
if not temperature.replace('.', '', 1).isdigit():
    raise ValueError("Invalid temperature. Please enter a numeric value.")

# Convert to float
temperature = float(temperature)

# Convert based on unit
if unit == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result:.2f}°F")
elif unit == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
