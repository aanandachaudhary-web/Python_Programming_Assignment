students = [
    {"name": "Aanand", "marks": [85, 90, 80]},
    {"name": "Ram", "marks": [75, 80, 70]},
    {"name": "Sita", "marks": [90, 85, 95]},
    {"name": "Hari", "marks": [65, 70, 75]},
    {"name": "Gita", "marks": [88, 92, 84]}
]


def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    return calculate_total(marks) / 300 * 100


def display_result(student):
    marks = student.get("marks", [])

    if len(marks) < 3 or any(mark is None for mark in marks):
        print("Error: Subject marks are missing.")
        return

    total = calculate_total(marks)
    percentage = calculate_percentage(marks)

    print("Student Name:", student["name"])
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")


try:
    student_name = input("Enter student name: ").strip()

    student = next(
        s for s in students
        if s["name"].lower() == student_name.lower()
    )

    display_result(student)

except StopIteration:
    print("Error: Student does not exist.")

except (TypeError, ValueError):
    print("Error: Invalid or missing subject marks.")