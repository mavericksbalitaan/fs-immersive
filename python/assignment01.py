# Create a string containing your first and last name. Use one of the built-in string functions explained in the "Strings" portion of the platform to check to see if that string contains your last name

my_name = "John Doe"
test1 = my_name.startswith("John")
test2 = my_name.endswith("Doe")
print(test1, test2)

# Create a user name. Your user name must contain letters and numbers ONLY. Use one of the built-in string functions explained in the previous slide to check to see if that string is valid.

user_name = "JohnDoe123"
test = user_name.isalnum()
print(test)
