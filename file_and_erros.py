# This file contains file and error handling related codes
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is an example file.\n")

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('example.txt', 'w') as file:
#     file.write("This will overwrite")

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

filename = 'example.txt'

try:
    # Attempts to read a file
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError as e:
    print(f"Error: {e}. The file '{filename}' does not exist.")

except IOError as e:
    print(f"Error: {e}. An I/O error occurred while handling the file '{filename}'.")

except PermissionError as e:
    print(f"Error: {e}. You do not have permission to access the file '{filename}'.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Program ended")