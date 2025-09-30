"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

name = " John Doe"
age = "25"
phone_number = "0928398659"

nameFlag = True
for char in name:
    if not (char.isalpha() or char == " "):
        nameFlag = False
        break

ageFlag = True
if not age.isdigit():
    ageFlag = False
else:
    age_int = int(age)
    if age_int < 18 or age_int > 65:
        ageFlag = False

phoneFlag = True
if len(phone_number) != 10 or not phone_number.isdigit():
    phoneFlag = False

print("Validation Result:")

if nameFlag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (should contain only letters and spaces)")

if ageFlag:
    print(f"Age: Valid ({age} years old)")
else:
    print("Age: Invalid (must be between 18 and 65)")

if phoneFlag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (must be a 10-digit number)")

if nameFlag and ageFlag and phoneFlag:
    print("\nFormatted Information:")

    print("Name:", name.upper().strip())

    age_int = int(age)
    if 18 <= age_int <= 30:
        print("Age Group: Young Adult (18-30)")
    elif 31 <= age_int <= 50:
        print("Age Group: Adult (31-50)")
    else:
        print("Age Group: Senior Adult (51-65)")

    print("Phone: +66-%s" % phone_number)
