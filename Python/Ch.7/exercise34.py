def main():
    employees = ["John Smith", "Jackie Jackson", "Chris Jones", "Amanda Cullen", "Jeremy Goodwin"]

    print("There are " + str(len(employees)) + " Employees:")

    for employee in employees:
        print(employee)

    remove_name = input("Enter an employee name to remove: ")

    employees.remove(remove_name)

    print("There are " + str(len(employees)) + " Employees:")

    for employee in employees:
        print(employee)

main()