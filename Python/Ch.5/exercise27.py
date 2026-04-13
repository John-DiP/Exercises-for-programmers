import re

def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    zip_code = input("Enter the ZIP code: ")
    employee_id = input("Enter an employee ID: ")
    
    errors = validateInput(first_name, last_name, zip_code, employee_id)

    if errors == "":
        print("There were no errors found.")
    else:
        print(errors)

def validateInput(first_name, last_name, zip_code, employee_id):
  
    errors = ""
    errors += firstName(first_name)
    errors += lastName(last_name)
    errors += zipCode(zip_code)
    errors += employeeID(employee_id)

    return errors
    
def firstName(first_name):
    if len(first_name) == 0:
        return "The first name must be filled in.\n"
    elif len(first_name) < 2:
        return f'"{first_name}" is not a valid first name. It is too short.\n'
    return ""

def lastName(last_name):
    if len(last_name) == 0:
        return "The last name must be filled in.\n"
    elif len(last_name) < 2:
        return f'"{last_name}" is not a valid last name. It is too short.\n'
    return ""

def zipCode(zip_code):
    if not zip_code.isdigit():
        return "The ZIP code must be numeric.\n"
    return ""

def employeeID(employee_id):
    if not re.match(r"^[A-Za-z]{2}-[0-9]{3,4}$", employee_id):
        return f'{employee_id} is not a valid ID.\n'
    
    return ""

main()