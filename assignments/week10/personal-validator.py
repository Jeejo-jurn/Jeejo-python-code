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

# === PERSONAL INFORMATION VALIDATOR ===

print("=== PERSONAL INFORMATION VALIDATOR ===")

name = input("Enter your name: ")
age = input("Enter your age: ")
phone = input("Enter your phone number: ")

print("\Validation Result:")

name_valid = all(part.isalpha() for part in name.split())
if name_valid:
    print("Name: Valid (constains only letters and space)")
else:
    print("Name: Invalid (should contain only letter and space)")

if age.isdigit():
    age_int = int(age)
    if 18 <= age_int <=65:
        print(f"Age: Valid ({age_int} year old)")
    else:
        print(f"Age: Invalid (must be between 18 and 65)")
        age_int = None
else:
    print("Age: Invalid (must be a number)")
    age_int = None

if phone.isdigit() and len(phone) == 10:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (must be exacly 10 digit)")

if name_valid and age_int is not None and phone.isdigit() and len(phone) == 10:
    print("\nFormatted Information:")

formatted_name = name.upper()

if 18 <= age_int <= 30:
    age_group = "Young Adult (18-30)"
elif 31 <= age_int <=50:
    age_group = "Adult (31-50)"
else:
    age_group = "Senior Adult (51-65)"

formatted_phone = "+91-{}".format(phone)

print("Name: {}".format(formatted_name))
print("Age Group: {}".format(age_group))
print("Phone: {}".format(formatted_phone))