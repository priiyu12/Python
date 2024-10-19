def celFah(celsius):
    if celsius < -273.15:
        raise ValueError(f"Invalid temperature! Temperature cannot be below absolute zero (-273.15°C).")
    return (celsius * 9/5) + 32

try:
    cel = float(input("Enter temperature in Celsius: "))
    fah = celFah(cel)
    print(f"Temperature in Fahrenheit: {fah:.2f}°F")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
