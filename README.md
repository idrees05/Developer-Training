# Developer Training

I have dedicated 4 hours a day every weekday for 3 months to studying

- HTML
- CSS
- JavaScript
- SQL
- Python


# Table of Contents for SQL Notes

## 1. Introduction to SQL and Relational Databases
   - 1.1. What is SQL?
   - 1.2. Purpose and Importance of SQL
   - 1.3. What is a Relational Database?
   - 1.4. Basics of Relational Database Design

## 2. Setting Up Your SQL Environment
   - 2.1. Installing MySQL
   - 2.2. Overview of MySQL Workbench
   - 2.3. Connecting to the MySQL Server
   - 2.4. Creating Your First Database

## 3. SQL Syntax and Basic Queries
   - 3.1. Structure of SQL Statements
   - 3.2. Understanding Data Types
   - 3.3. Basic SELECT Queries
   - 3.4. Filtering Data with WHERE
   - 3.5. Sorting Data with ORDER BY

## 4. Modifying Data and Table Structure
   - 4.1. INSERT INTO Statement
   - 4.2. UPDATE Statement
   - 4.3. DELETE Statement
   - 4.4. ALTER TABLE Basics

## 5. Advanced Data Retrieval
   - 5.1. Aggregating Data with Functions
   - 5.2. Grouping Data with GROUP BY
   - 5.3. Filtering Groups with HAVING
   - 5.4. Combining Queries with UNION

## 6. Understanding Joins and Table Relationships
   - 6.1. INNER JOIN Explained
   - 6.2. OUTER JOINS: LEFT and RIGHT
   - 6.3. CROSS JOIN and Its Uses
   - 6.4. SELF JOIN for Advanced Data Comparison

## 7. Complex SQL Queries
   - 7.1. Subqueries in SQL
   - 7.2. Using JOINs in Complex Queries
   - 7.3. Advanced WHERE Clauses
   - 7.4. The CASE Statement

## 8. Working with Indexes and Performance Tuning
   - 8.1. Introduction to Indexing
   - 8.2. Creating and Using Indexes
   - 8.3. Understanding Query Performance
   - 8.4. Basic Performance Tuning Techniques

## 9. Database Normalization and Schema Design
   - 9.1. Database Normalization Concepts
   - 9.2. First, Second, and Third Normal Forms
   - 9.3. Denormalization Considerations
   - 9.4. Implementing Relationships: Keys and Constraints

## 10. SQL in the Real World
    - 10.1. Integrating SQL with Applications
    - 10.2. Security Best Practices in SQL
    - 10.3. Transaction Management
    - 10.4. Common SQL Patterns in Industry

## 11. Backup, Restore, and Migration
    - 11.1. Strategies for Backing Up Data
    - 11.2. Restoring Data from Backups
    - 11.3. Migrating Data Between Databases
    - 11.4. Automating Backup and Restore Processes

## 12. Practice with Real-world SQL Scenarios
    - 12.1. Designing a Database for E-commerce
    - 12.2. Building a Blogging Platform Database
    - 12.3. Analyzing Data with SQL for Business Intelligence
    - 12.4. SQL for Data Science: Basics of Data Analysis

## 13. Review and Practice Exercises
    - 13.1. Practice Exercise Set 1: Basic Queries
    - 13.2. Practice Exercise Set 2: Joins and Subqueries
    - 13.3. Practice Exercise Set 3: Aggregation and Reporting
    - 13.4. Practice Exercise Set 4: Performance and Indexing

## 14. Conclusion and Next Steps
    - 14.1. Reviewing Key SQL Concepts
    - 14.2. Continuing Education in SQL and Databases
    - 14.3. Exploring Advanced SQL Topics
    - 14.4. Resources for Further Learning




# Introduction to SQL and Relational Databases

## 1.1 What is SQL?
SQL stands for Structured Query Language, which is a standardized programming language specifically designed for storing, manipulating, and retrieving data in databases. It is the foundation for all relational database operations.

### Key Points:
- SQL is used to communicate with a database.
- It is the standard language for relational database management systems.
- SQL statements are used to perform tasks such as updating data on a database or retrieving data from a database.

## 1.2 Purpose and Importance of SQL
SQL is essential for interacting with relational databases. It allows users to create, read, update, and delete records in a database (often referred to as CRUD operations). It's widely used because it can work with database systems like MySQL, SQL Server, PostgresSQL, and Oracle.

### Key Points:
- CRUD operations: Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE).
- SQL can set permissions on tables, procedures, and views.
- A strong understanding of SQL provides the ability to maintain data integrity and security.

## 1.3 What is a Relational Database?
A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables.

### Key Points:
- In a relational database, each row in the table is a record with a unique ID called the key.
- The columns of the table hold attributes of the data.
- The relational model means that the logical data structures—the data tables, views, and indexes—are separate from the physical storage.

## 1.4 Basics of Relational Database Design
Effective relational database design involves organizing data into a set of tables with unique keys and understanding the relationships between those tables.

### Key Points:
- Tables, sometimes referred to as relations, are a matrix of data arranged in rows and columns.
- A table has a unique key, known as the primary key, which uniquely identifies each record.
- Relationships between tables are established via foreign keys, columns that reference the primary key in another table.

The design of a relational database adheres to a series of principles known as normalization rules to reduce data redundancy and improve data integrity. Normalization typically involves dividing a database into two or more tables and defining relationships between the tables.

In the next section, we'll dive deeper into setting up your SQL environment and taking the first steps in using MySQL. Stay tuned!



# Setting Up Your SQL Environment

## 2.1 Installing MySQL

Before diving into the world of SQL, you need a relational database management system (RDBMS). MySQL is a popular choice due to its robust features and open-source nature.

### Steps to Install MySQL:
1. **Download MySQL Installer**: Visit the official MySQL website and download the installer appropriate for your operating system.
2. **Run the Installer**: Execute the downloaded file and follow the installation prompts.
3. **Configure MySQL Server**: Set up a root password and, optionally, create additional user accounts.
4. **Complete the Installation**: Finish the setup and launch MySQL Workbench to interact with your MySQL server.

## 2.2 Overview of MySQL Workbench

MySQL Workbench is a unified visual tool for database architects, developers, and DBAs. It provides data modeling, SQL development, and comprehensive administration tools.

### Key Features:
- **SQL Development**: Write and execute SQL statements.
- **Data Modeling**: Design and manage database schema.
- **Server Administration**: Configure, manage, and monitor server settings and log files.

## 2.3 Connecting to the MySQL Server

To start working with MySQL, you need to establish a connection between MySQL Workbench and your MySQL server instance.

### Steps to Connect:
1. Open MySQL Workbench.
2. Click on the **+** symbol beside **MySQL Connections**.
3. Enter the connection details like hostname, port, username, and password.
4. Test the connection and if successful, click **OK** to save it.

## 2.4 Creating Your First Database

With a connection established, you can now create your first database using MySQL Workbench.

### SQL Command:
```sql
CREATE DATABASE IF NOT EXISTS first_database;
```

### Steps in MySQL Workbench:
1. Connect to your MySQL server instance.
2. Open a new SQL tab for executing queries.
3. Type the `CREATE DATABASE` command into the query window.
4. Execute the command by clicking the lightning bolt icon.

With your environment set up and your first database created, you're now ready to start exploring SQL queries and database operations.


# SQL Syntax and Basic Queries

## 3.1 Structure of SQL Statements

SQL is a domain-specific language used in programming and designed for managing data held in a relational database management system. It is particularly useful in handling structured data where there are relations between different entities/variables of the data.

### Basic SQL Query Structure:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
ORDER BY column1, column2, ... ASC|DESC;
```

- `SELECT`: Specifies the columns to be retrieved.
- `FROM`: Specifies the tables from which to retrieve the data.
- `WHERE`: Filters records based on specified conditions.
- `ORDER BY`: Specifies the sort order for the result set.

## 3.2 Understanding Data Types

Data types define the type of data that can be stored in a particular column of a database table. SQL supports a variety of data types.

### Common Data Types:
- `INT`: A whole number (integer).
- `VARCHAR`: A variable-length string.
- `DATE`: A date.
- `FLOAT` or `DOUBLE`: Floating-point numbers.

## 3.3 Basic SELECT Queries

The `SELECT` statement is used to select data from a database. The data returned is stored in a result table, sometimes called the result set.

### SELECT Examples:
```sql
-- Select all columns from a table
SELECT * FROM table_name;

-- Select specific columns from a table
SELECT column1, column2 FROM table_name;

-- Select distinct entries
SELECT DISTINCT column1 FROM table_name;
```

## 3.4 Filtering Data with WHERE

The `WHERE` clause is used to filter records. It is used to extract only those records that fulfill a specified condition.

### WHERE Clause Examples:
```sql
-- Select entries with specific conditions
SELECT * FROM table_name WHERE condition;

-- Using comparison operators in conditions
SELECT * FROM table_name WHERE column1 > value1;
```

## 3.5 Sorting Data with ORDER BY

The `ORDER BY` clause is used to sort the result set in ascending or descending order.

### ORDER BY Examples:
```sql
-- Sort the result set by a single column
SELECT * FROM table_name ORDER BY column1;

-- Sort the result set by multiple columns
SELECT * FROM table_name ORDER BY column1 ASC, column2 DESC;
```

These foundational concepts are key to understanding how to interact with and manipulate data in SQL. As you become more comfortable with these basics, you'll be able to perform more complex operations and query data more effectively.

Next, we'll look at how to modify data and table structures using SQL commands.



# Modifying Data and Table Structure

## 4.1 INSERT INTO Statement

The `INSERT INTO` statement is used to add new rows to a table. 

### Syntax:
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

### Example:
```sql
INSERT INTO Employees (FirstName, LastName, Age)
VALUES ('John', 'Doe', 30);
```

This command inserts a new row into the Employees table where the FirstName is 'John', the LastName is 'Doe', and the Age is 30.

## 4.2 UPDATE Statement

The `UPDATE` statement is used to modify existing records in a table.

### Syntax:
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### Example:
```sql
UPDATE Employees
SET Age = 31
WHERE FirstName = 'John' AND LastName = 'Doe';
```

This command updates the age of 'John Doe' in the Employees table to 31.

## 4.3 DELETE Statement

The `DELETE` statement is used to delete existing records from a table.

### Syntax:
```sql
DELETE FROM table_name WHERE condition;
```

### Example:
```sql
DELETE FROM Employees
WHERE FirstName = 'John' AND LastName = 'Doe';
```

This command deletes the record for 'John Doe' from the Employees table.

## 4.4 ALTER TABLE Basics

The `ALTER TABLE` statement is used to add, delete, or modify columns in an existing table.

### Add a Column:
```sql
ALTER TABLE table_name
ADD column_name datatype;
```

### Delete a Column:
```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

### Modify a Column:
```sql
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```

### Example - Add a Column:
```sql
ALTER TABLE Employees
ADD Email VARCHAR(255);
```

This command adds a new column named 'Email' to the Employees table.

Through these commands, you can manipulate both the data within your tables and the structure of the tables themselves. Understanding how to use these statements effectively is crucial for managing and maintaining the integrity of your database.

In the upcoming sections, we will delve into more advanced data retrieval techniques and explore the power of SQL for complex queries and data analysis.


# Advanced Data Retrieval

## 5.1 Aggregating Data with Functions

SQL provides several built-in functions to perform calculations on a set of values, giving you a single value in return. These functions are known as aggregate functions.

### Common Aggregate Functions:
- `COUNT()`: Returns the number of rows that matches a specified criterion.
- `SUM()`: Returns the total sum of a numeric column.
- `AVG()`: Returns the average value of a numeric column.
- `MAX()`: Returns the largest value of the selected column.
- `MIN()`: Returns the smallest value of the selected column.

### Examples:
```sql
-- Count the total number of employees
SELECT COUNT(*) FROM Employees;

-- Calculate the total salary expenditure
SELECT SUM(Salary) FROM Employees;

-- Find the average salary
SELECT AVG(Salary) FROM Employees;

-- Get the highest and lowest salary
SELECT MAX(Salary), MIN(Salary) FROM Employees;
```

## 5.2 Grouping Data with GROUP BY

The `GROUP BY` statement groups rows that have the same values into summary rows, like "find the number of employees in each department".

### Syntax:
```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name;
```

### Example:
```sql
-- Count the number of employees in each department
SELECT DepartmentID, COUNT(*) AS 'Number of Employees'
FROM Employees
GROUP BY DepartmentID;
```

## 5.3 Filtering Groups with HAVING

The `HAVING` clause was added to SQL because the `WHERE` keyword cannot be used with aggregate functions. `HAVING` allows you to specify conditions to filter groups or aggregates.

### Syntax:
```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
GROUP BY column_name
HAVING condition;
```

### Example:
```sql
-- Find departments with more than 10 employees
SELECT DepartmentID, COUNT(*) AS 'Number of Employees'
FROM Employees
GROUP BY DepartmentID
HAVING COUNT(*) > 10;
```

## 5.4 Combining Queries with UNION

The `UNION` operator is used to combine the result sets of two or more `SELECT` statements. It removes duplicate rows between the various `SELECT` statements.

### Syntax:
```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

### Example:
```sql
-- Combine unique employee names from two different tables
SELECT FirstName FROM CurrentEmployees
UNION
SELECT FirstName FROM FormerEmployees;
```

Advanced data retrieval in SQL is pivotal for deeper data analysis and generating reports. Using aggregate functions, grouping, filtering, and combining queries can provide powerful insights into your data.

In the following sections, we'll dive into the more complex aspects of SQL queries, including joins and subqueries, which are instrumental in performing sophisticated database operations.


