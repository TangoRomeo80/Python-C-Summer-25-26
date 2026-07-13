# This file will contain error handling related codes
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
# print(10/0)

request = input("Do you want to continue? (yes/no): ")

try:
    if request.lower() == "yes":
        print("Continuing...")
    elif request.lower() == "no":
        print("Exiting...")
    else:
        raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
except ValueError as e:
    print(f"Error: {e}")
    