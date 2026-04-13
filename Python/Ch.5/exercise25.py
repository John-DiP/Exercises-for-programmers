def main():
    password = input("Enter a password: ")
    strength = passwordValidator(password)
    print(f"The password '{password}' is a {strength} password. ")

def passwordValidator(password):
    
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    if len(password) < 8 and password.isdigit():
        return "very weak"
    if len(password) < 8 and password.isalpha():
        return "weak"
    elif len(password) >= 8 and has_letter and has_number and not has_special:
        return "strong"
    elif len(password) >= 8 and has_letter and has_number and has_special:
        return "very strong"

main()