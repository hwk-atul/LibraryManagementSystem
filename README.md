(# Library Management (Simple CLI)

Small, file-based Library Management System written in Python. It provides a simple command-line interface to add, search, update, delete, issue, and return books using two plain-text files as storage:

- `library.txt` — stores book records (BookID, Title, Author, Quantity)
- `issued_books.txt` — stores issued book records (BookID, Title, StudentName, StudentID, IssueDate, DueDate)

This project is intended for learning and small demos. It has no external dependencies and runs with Python 3.

## Files in this repository

- `library new and final.py` — main CLI program. Run this to start the menu-driven interface.
- `library.txt` — data file for available books. Each line is a CSV record: `BookID,Title,Author,Quantity`.
- `issued_books.txt` — data file for issued books. Each line is a CSV record: `BookID,Title,StudentName,StudentID,IssueDate,DueDate`.
- `issued_books.txt` — may be empty initially.

## Usage

1. Make sure you have Python 3 installed. To check your Python version in PowerShell:

```powershell
python --version
```

2. From the project folder, run the script:

```powershell
python "library new and final.py"
```

3. Follow the on-screen menu. Options include adding books, displaying all books, searching by title, deleting/updating books, issuing and returning books, and viewing due/late issued books.

Example: Issue a book

- Choose option 7 (Issue Book).
- Enter the Book ID that exists in `library.txt`.
- Enter student name and ID. The program records the issue date (today) and a due date 7 days later in `issued_books.txt`, and decrements the book quantity in `library.txt`.

Example: Return a book

- Choose option 8 (Return Book).
- Enter Book ID, Student Name, and Student ID exactly as used when issuing. The program will increment the quantity and remove the corresponding entry from `issued_books.txt`. If returned after the due date, it prints a fine (Rs. 5 per late day).

## Data formats

- `library.txt` sample line:

```
1,Cant Hurt Me,david goggin,100
```

- `issued_books.txt` sample line:

```
1,Cant Hurt Me,John Doe,STU001,2025-11-24,2025-12-01
```

Notes:

- The program uses simple CSV-like lines split by commas. Titles and names should avoid commas or the parsing will break.
- Dates are stored in `YYYY-MM-DD` format.
- No concurrency control: avoid editing the files while the program runs.

## Assumptions and Limitations

- This is a single-user, file-based demo. It is not intended for production use.
- No input validation beyond basic conversions. Numeric fields and dates may fail silently in some edge cases.
- The program expects UTF-8 plain text files in the same directory as the script.

## Suggested Improvements (next steps)

- Add input validation and clearer error messages.
- Use the `csv` module to handle commas inside fields safely.
- Add persistent unique ID generation for books.
- Add unit tests and separate the CLI from the library logic for easier maintenance.

## License

Use and modify freely for learning purposes.

---

If you want, I can also:

- Clean up and refactor `library new and final.py` (PEP8, functions split into a module),
- Replace the plain-text files with a small SQLite database and migration script, or
- Add a small test suite and basic input validation.

Tell me which of these you'd like next.)
