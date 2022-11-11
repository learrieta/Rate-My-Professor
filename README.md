# Overview
The purpose of this program is for students to be able to look up the different professors at the university and gain more information about them based on other students' opinions. This program is linked to MYSQL database which contains different tables with different information that are linked to one another.

Starting college is hard, we need to worry about our books, materials, and classes. In an attempt to ease the transition to a new semester, the program Rate-My-Professor will let students be able to pick a teacher for a class that they feel better fits their learning style environment. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](https://youtu.be/UQ9qDRrgXr4)

# Relational Database

* I am using MYSQL database

The structure of the tables is very basic. There is a faculty table where I store the full names of the teachers. Then there is a course table that is linked to the faculty table as a one-to-many relationship. Lastly, there is a reviews table which is a link to the faculty table by a many-to-many relationship.

# Development Environment

* Python
* MySQL Workbench
* Tkinter

The programming language use is:
* Python

# Useful Websites

* [W3schools](https://www.w3schools.com/python/)
* [W3schools](https://www.w3schools.com/sql/default.asp)

# Future Work

* Better user interface
* A stronger relational database
* Make it online