username = input("Enter username: ")
password = input("Enter password: ")
stored_password = "SecurePassword123"
if password == stored_password:
    print("Login successful!")
else:
    print("Invalid credentials")
print("Username:", username)