firstname, middlename, lastname = input("Enter your full name(First name, Middle Name, Last name):").split()

firstname = firstname.strip().capitalize()
middlename = middlename.strip().capitalize()
lastname = lastname.strip().capitalize()

middleinitial = middlename[0] + "."

print("Formatted Name:", f"{lastname}, {firstname} {middleinitial}")