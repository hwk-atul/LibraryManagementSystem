# Project Statement

## Problem statement

Small schools, clubs, and community centers often need a lightweight way to manage their book collections and track loans, but they lack access to a simple, offline tool that is easy to run and maintain. Existing solutions can be complex, require databases or internet access, or demand technical skills to install and operate.

## Scope of the project

This project provides a compact, file-based Library Management System implemented as a Python command-line program. It supports core operations needed for day-to-day library tasks: adding and managing book records, issuing and returning books, and tracking due/late loans. The scope intentionally excludes multi-user concurrency, secure authentication, and advanced reporting.

## Target users

- Small schools, student clubs, and community libraries with modest collections
- Teachers or volunteers with basic comfort running Python scripts or command-line programs
- Learners who want a simple example of file-based data management

## High-level features

- Add, update, delete, and list book records stored in a plain text file (`library.txt`).
- Search books by title (case-insensitive substring match).
- Issue books to students: record student name/id, issue date, and due date in `issued_books.txt`; decrement available quantity.
- Return books: increment quantity, remove the corresponding issued record, and compute fines for late returns.
- View issued books, due books, and late books from the issued records file.
- Minimal dependencies: runs with Python 3 and uses plain text files for persistence.

---

If you want the statement expanded into a short project proposal or converted into a presentation slide, I can generate that next.
