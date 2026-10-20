
import json
import os

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read student file. Starting with an empty list.")
        return []


def save_students():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error: Could not save student records.")


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter student marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    student = {"name": name, "marks": marks}
    students.append(student)
    save_students()
    print(f"{name} added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student Records ---")

    for number, student in enumerate(students, start=1):
        print(
            f"{number}. Name: {student['name']} | "
            f"Marks: {student['marks']:g}"
        )


def search_student():
    name = input("Enter student name to search: ").strip().lower()

    matches = [
        student for student in students
        if name in student["name"].lower()
    ]

    if matches:
        print("\n--- Search Results ---")
        for student in matches:
            print(f"Name: {student['name']}, Marks: {student['marks']:g}")
    else:
        print("Student not found.")


def update_student():
    name = input("Enter the student's name to update: ").strip().lower()

    matches = [
        student for student in students
        if student["name"].lower() == name
    ]

    if not matches:
        print("Student not found.")
        return

    if len(matches) > 1:
        print("Multiple students have this name. Please use unique names.")
        return

    student = matches[0]

    try:
        new_marks = float(input("Enter new marks (0-100): "))

        if not 0 <= new_marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    student["marks"] = new_marks
    save_students()
    print("Student marks updated successfully!")


def delete_student():
    name = input("Enter the student's name to delete: ").strip().lower()

    matches = [
        student for student in students
        if student["name"].lower() == name
    ]

    if not matches:
        print("Student not found.")
        return

    if len(matches) > 1:
        print("Multiple students have this name. Please use unique names.")
        return

    students.remove(matches[0])
    save_students()
    print("Student deleted successfully!")


def show_statistics():
    if not students:
        print("No student records available.")
        return

    marks_list = [student["marks"] for student in students]

    average = sum(marks_list) / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)
    passed = sum(1 for mark in marks_list if mark >= 40)
    failed = len(students) - passed

    print("\n--- Class Statistics ---")
    print(f"Total students: {len(students)}")
    print(f"Average marks: {average:.2f}")
    print(f"Highest marks: {highest:g}")
    print(f"Lowest marks: {lowest:g}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")


def show_passed_students():
    passed_students = [
        student for student in students
        if student["marks"] >= 40
    ]

    if not passed_students:
        print("No passed students found.")
        return

    print("\n--- Passed Students ---")

    for student in passed_students:
        print(f"{student['name']} - {student['marks']:g} marks")


def main():
    while True:
        print("\n==== STUDENT RECORD MANAGER ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Show Class Statistics")
        print("7. Show Passed Students")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 8.")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            show_statistics()
        elif choice == 7:
            show_passed_students()
        elif choice == 8:
            print("Goodbye, bro!")
            break
        else:
            print("Invalid choice. Please select 1-8.")


students = load_students()
main()
