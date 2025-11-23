# Restaurant Database CLI — Quick Start Guide

This is a simple command-line tool for interacting with a restaurant SQLite database (`Restaurant-Database.db`).  
You can insert employees, insert menu items, update menu item prices, delete data, and print tables.

## 1. How to Run the CLI

From the terminal, run:

```
python cli.py <command> <arguments>
```

Example:

```
python cli.py insert_employee John Doe "225-555-5555" john@example.com 2025-01-01 "Active" 3
```

## 2. Commands Overview

Below is every command your CLI supports and how to use each one.

### insert_employee

Add a new employee to the `Employee` table.

**Usage:**
```
python cli.py insert_employee <first_name> <last_name> <phone> <email> <hire_date> <status> <position_id>
```

**Example:**
```
python cli.py insert_employee John Doe 2255551234 john@company.com 2025-01-12 Active 2
```

### insert_menu_item

Add a new menu item.

**Usage:**
```
python cli.py insert_menu_item <item_name> <price> <course_id> <section_id> <description> <isVegetarian> <isAvailable>
```

**Example:**
```
python cli.py insert_menu_item "Caesar Salad" 8.99 1 2 "Fresh romaine with dressing" 1 1
```

### update_item_price

Update the price of a menu item.

**Usage:**
```
python cli.py update_item_price <item_id> <new_price>
```

**Example:**
```
python cli.py update_item_price 5 12.50
```

### delete_menu_item

Delete a menu item by ID.

**Usage:**
```
python cli.py delete_menu_item <item_id>
```

**Example:**
```
python cli.py delete_menu_item 7
```

### delete_employee

Delete an employee by ID.

**Usage:**
```
python cli.py delete_employee <employee_id>
```

**Example:**
```
python cli.py delete_employee 3
```

### print_table

Print the entire contents of any table in the database.

**Usage:**
```
python cli.py print_table <table_name>
```

**Example:**
```
python cli.py print_table Employee
```

or:

```
python cli.py print_table MenuItem
```

This prints all rows in the selected table.

## 3. Database File

Place your database file in the same directory:

```
Restaurant-Database.db
```

If the file doesn’t exist, SQLite will create an empty one.

## 4. Notes

- Dates must use the format **YYYY-MM-DD**  
- `isVegetarian` and `isAvailable` must be **0 or 1**  
- All arguments are **positional**, so order matters
