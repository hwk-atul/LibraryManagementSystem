# Project Statement

## Problem statement

Many small schools, clubs, and community groups need an easy way to keep record of their books and track which books are taken. But they do not have a simple offline tool that is easy to use. Most available systems are difficult, need databases or internet, and require technical knowledge. That is why a simple and easy-to-run Library Management System is needed.

## Scope of the project

This project is a small and simple Library Management System made in Python. It works using text files and runs in the command line. It helps in basic library work like adding books, keeping records, giving books to students, taking returns, and checking late books. This project does not include things like multi-user login, security, or advanced reports because it is made only for simple and basic use.

## Target users

-Small schools, student clubs, and community libraries that have only a few books.
-Teachers or helpers who know a little bit of Python or can run simple command-line programs.
-Students who want an easy example of how to store and manage data using text files.

## High-level features

-We can add, update, delete, and show book records that are saved in a simple text file called library.txt.
-We can search for books by their title, even if we type only part of the name.
-We can issue books to students by saving their name/ID, the issue date, and due date in issued_books.txt. The number of available copies is also reduced.
-When a book is returned, the quantity increases again, the issue record is removed, and the fine is calculated if the book is late.
-We can see all issued books, books that are due soon, and books that are already late by checking the issued records file.
-This system needs almost no special setup. It only uses Python 3 and simple text files to store the data.

