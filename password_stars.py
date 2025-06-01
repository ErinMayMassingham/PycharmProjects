import os

min_length = 8
password = input("Enter a password: ")
while len(password) < min_length:
    print(f"Error: Password must be at least {min_length} characters.")
    password = input("Enter a password: ")
print("*" * len(password))
