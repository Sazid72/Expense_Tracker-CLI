# Expense Tracker

#### Video Demo: https://youtu.be/cjkqb9Ts-qk
#### Description:
This is a command-line Expense Tracker application written in Python. The program allows users to record, store, and view their daily expenses in a simple and organized way. It also calculates the total amount spent, helping users better understand their spending habits.

Expense Tracker is a command-line application written in Python that helps users record and monitor their daily expenses. The program allows users to add expenses by providing a description, category, and amount. Each expense is automatically saved to a CSV file along with the current date using the datetime module, creating a record that can be accessed later.

The application provides a simple menu-driven interface. Users can choose to add a new expense or view all previously recorded expenses. When viewing expenses, the program reads data from the CSV file and displays each entry in a formatted layout. It also calculates the total amount spent by adding all recorded expenses, giving users a quick overview of their spending.

One of the main design goals of this project was simplicity. I chose to use Python's built-in csv module instead of a database because CSV files are lightweight, easy to understand, and sufficient for a small personal finance application. This approach also keeps the project accessible to beginners while demonstrating file handling and data persistence.

Another important design decision was separating validation logic from user interaction. Functions such as validate_choice and validate_amount are responsible for validating user input, while other functions handle input and output. This separation improves code organization and makes the program easier to test with pytest. Unit tests were written to verify that valid inputs are accepted and invalid inputs correctly raise exceptions.

During development, I learned how to work with CSV files, create reusable functions, validate user input, and write automated tests. These concepts are important foundations for larger Python applications. The project demonstrates several topics covered in CS50P, including file I/O, exception handling, functions, modules, and testing.

In the future, the application could be expanded with additional features such as category-based spending summaries, monthly reports, expense editing and deletion, and graphical visualizations of spending patterns. These improvements would make the tracker more useful while building on the existing structure of the program.

---

## Features

- Add new expenses with description, category, and amount
- Automatically stores expenses in a CSV file
- View all saved expenses in a formatted output
- Displays total amount spent
- Input validation for menu choices and amounts

---

## Files

- `project.py` — Main program file containing all logic
- `test_project.py` — Unit tests using pytest
- `expenses.csv` — Stores all recorded expenses (created automatically)
- `requirements.txt` — Contains required dependencies (pytest)

---

## How to Run

1. Run the program:
- `python project.py`

2. Follow the on-screen menu:
- Press `1` to add an expense
- Press `2` to view expenses

---

## Testing

To run tests:
- `pytest test_project.py`

The tests check:
- Valid and invalid menu choices
- Valid and invalid expense amounts

---

## Author
Md. Sazid Al Mafi<br>
<b>Created as a final project for CS50P (Introduction to Programming with Python).
