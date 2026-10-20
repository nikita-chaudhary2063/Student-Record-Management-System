# Student Record Management System

A menu-driven Python application for managing student records. Users can add, view, search, update, and delete student information, calculate class statistics, and display students who have passed.

This project was built to practise core Python programming concepts before moving on to Object-Oriented Programming (OOP).

## Features

- **Add Students:** Store student names and marks.
- **View Students:** Display all saved student records.
- **Search Students:** Find students by name.
- **Update Marks:** Modify an existing student's marks.
- **Delete Students:** Remove a student record.
- **Class Statistics:** Calculate average, highest, and lowest marks, and count passed and failed students.
- **Passed Students:** Display students who scored 40 or above.
- **JSON Storage:** Save and load student records between program runs.
- **Error Handling:** Handle invalid inputs and file errors.

## Technologies Used

- Python
- JSON
- Built-in `os` module

## Requirements

- Python 3.8 or later
- No external libraries required

## How to Run

1. Clone this repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Open the project directory:

   ```bash
   cd <your-project-folder>
   ```

3. Run the program:

   ```bash
   python student_manager.py
   ```

4. Choose an option from the menu and follow the instructions.

## Data Storage

Student records are stored in `students.json`. The program loads existing records when it starts and saves changes when student records are added, updated, or deleted.

## Passing Criteria

A student passes with marks greater than or equal to 40. Marks must be between 0 and 100.

## Python Concepts Practised

- Variables and data types
- Functions
- Lists and dictionaries
- Loops and conditional statements
- List comprehensions
- Exception handling
- File handling
- JSON data storage
- Modules and imports

## Future Improvements

- Add unique student IDs.
- Support multiple students with the same name.
- Sort student records by marks.
- Add unit tests.
- Build a graphical user interface.

## Learning Purpose

This project is part of my journey to strengthen my Python fundamentals and prepare for more advanced software development projects.

## Author

Nikita
