employees = {
    "E101": {
        "name": "Aanand",
        "department": "IT",
        "salary": 30000
    },
    "E102": {
        "name": "Ram",
        "department": "HR",
        "salary": 35000
    },
    "E103": {
        "name": "Sita",
        "department": "Finance",
        "salary": 40000
    },
    "E104": {
        "name": "Hari",
        "department": "Marketing",
        "salary": 32000
    },
    "E105": {
        "name": "Gita",
        "department": "IT",
        "salary": 45000
    }
}


def find_employee(employee_id):
    return employees[employee_id]


def calculate_yearly_salary(salary):
    return salary * 12


def increase_salary(employee, percentage):
    if percentage < 0:
        raise ValueError("Percentage cannot be negative.")

    old_salary = employee["salary"]
    increase = old_salary * percentage / 100
    employee["salary"] = old_salary + increase

    return old_salary, employee["salary"]


try:
    employee_id = input("Enter employee ID: ").strip().upper()
    employee = find_employee(employee_id)

    print("Employee Name:", employee["name"])
    print("Department:", employee["department"])

    percentage = float(
        input("Enter salary increase percentage: ")
    )

    old_salary, new_salary = increase_salary(
        employee, percentage
    )

    print("\n--- Salary Details ---")
    print("Old Monthly Salary: Rs.", old_salary)
    print("New Monthly Salary: Rs.", round(new_salary, 2))
    print("Yearly Salary: Rs.",
          round(calculate_yearly_salary(new_salary), 2))

except KeyError:
    print("Error: Employee ID does not exist.")

except ValueError as error:
    print("Invalid input:", error)
