
username = input("Enter username: ")
password = input("Enter password: ")

admin_password = "admin123"

if password == admin_password:
    print("Login successful!")
else:
    print("Invalid password")

print("Username:", username)
print("Password:", password)