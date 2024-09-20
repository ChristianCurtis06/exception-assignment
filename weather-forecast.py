# Task 1: Begin by asking the user to enter the temperature in Fahrenheit
def temp_conversion(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * 5/9
    return round(celsius_temp, 2)

while True:
    try:
        f_temp_input= float(input("Enter the temperature in Fahrenheit: "))
        
# Task 2: Temperature Conversion
        c_temp = temp_conversion(f_temp_input)
    except ValueError:
        print("ValueError: Invalid input. Please enter a number.")

# Task 3: User Experience
    else:
        print(f"{f_temp_input} degrees Fahrenheit is {c_temp} degrees Celsius.")

# Task 4: Add a 'finally' block that thanks the user for using the weather forecast application
    finally:
        print("Thank you for using the weather forecast application!")
        continue_input = input("Would you like to continue using the application? (yes/no) ").lower()
        if continue_input != "yes":
            break