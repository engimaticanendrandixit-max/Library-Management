Library Management System (Python + MySQL)
Project Overview

This is a Library Management System developed using Python and MySQL database integration.
The project demonstrates how Python can interact with a SQL database to manage books, members, and administrative operations in a library.

This project was created as part of my Class 12 Data Integration Project.

Features
Add, modify, delete and display books
Member registration and management
Issue books to members
Return books with automatic fine calculation
Admin login system
User login system
Database integration using MySQL
Automatic database and table creation
Technologies Used
Python
MySQL
mysql-connector
SQL Queries
CLI (Command Line Interface)
Database Structure

The system automatically creates these tables:

Book Table
Member Table
Admin Table

These tables store:

Book details
Member records
Login credentials
Issued book information
How to Run the Project
Install Python
Install MySQL
Install MySQL connector library
pip install mysql-connector-python
Update database credentials in the code:
con = sqltor.connect(
host='localhost',
user='your_mysql_username',
password='your_mysql_password',
charset='utf8'
)
Run the program
python library_management.py
System Modules

This project includes the following modules:

Admin Panel
Book management
Member management
Database control
User Panel
Login system
Issue book
Return book
Database Integration
Automatic database creation
Table management
Data storage and retrieval
Learning Outcomes

From this project I learned:

Python and SQL integration
Database management
CRUD operations
User authentication system
CLI based software development
Future Improvements
GUI interface using Tkinter or PyQt
Online database support
Book search system
Dashboard analytics
Web-based version
Author

Anendra Narayan Dixit
