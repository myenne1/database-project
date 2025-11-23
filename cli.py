import argparse
from datetime import datetime
import re
import sqlite3

def parse
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be YYYY-MM-DD")

def establish_cli():
    parser = argparse.ArgumentParser(description="CLI for sql database instructions")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Insert Employee
    insert_employee = subparsers.add_parser("insert_employee", help="Insert an employee")

    insert_employee.add_argument("first_name", type=str)
    insert_employee.add_argument("last_name", type=str)
    insert_employee.add_argument("phone", type=str)
    insert_employee.add_argument("email", type=str)
    insert_employee.add_argument("hire_date", type=parse_date)
    insert_employee.add_argument("status", type=str)
    insert_employee.add_argument("position_id", type=int)

    # Insert Menu Item
    insert_menu_item = subparsers.add_parser("insert_menu_item", help="Insert a menu item")

    insert_menu_item.add_argument("item_name")
    insert_menu_item.add_argument("price", type=float)
    insert_menu_item.add_argument("course_id", type=int)
    insert_menu_item.add_argument("section_id", type=int)
    insert_menu_item.add_argument("description", type=str)
    insert_menu_item.add_argument("isVegetarian", type=int, choices=[0, 1])
    insert_menu_item.add_argument("isAvailable", type=int, choices=[0, 1])

    # Update Menu Item Price
    update = subparsers.add_parser("update_item_price", help="Update menu item price")

    update.add_argument("item_id", type=int)
    update.add_argument("price", type=float)

    # Delete Menu Item
    delete_menu_item = subparsers.add_parser("delete_menu_item", help="Delete a menu item")

    delete_menu_item.add_argument("item_id", type=int)

    # Delete Employee
    delete_employee = subparsers.add_parser("delete_employee", help="Delete an employee")

    delete_employee.add_argument("employee_id", type=int)
    
    # Print Database Contents
    print_table = subparsers.add_parser("print_table", help="Prints all rows in a specific table")
    
    print_table.add_argument("table_name", type=str)
    
    return parser

def connect_to_database():
    db = sqlite3.connect('Restaurant-Database.db')
    return db

def insert_employee(db, args):
    cursor = db.cursor()
    try:
        sql_command = "INSERT INTO Employee (FirstName, LastName, Phone, Email, HireDate, Status, PositionID) VALUES (?,?,?,?,?,?,?)"
        cursor.execute(sql_command, (args.first_name, args.last_name, args.phone, args.email, args.hire_date.strftime("%Y-%m-%d"), args.status, args.position_id))
        db.commit()
        print("Insert Successful!")
    except sqlite3.Error as e:
        print(f"Error inserting employee: {e}")
    

def insert_menu_item(db, args):
    cursor = db.cursor()
    try:
        sql_command = "INSERT INTO MenuItem (ItemName, CourseID, SectionID, Price) VALUES (?,?,?,?)"
        cursor.execute(sql_command, (args.item_name, args.course_id, args.section_id, args.price))
        db.commit()
        print("Insert Successful!")
    except sqlite3.Error as e:
        print(f"Error inserting menu item: {e}")
    
    
def update_menu_price(db, args):
    cursor = db.cursor()
    try:
        sql_command = "UPDATE MenuItem SET Price = ? WHERE MenuItemID = ?"
        cursor.execute(sql_command, (args.price, args.item_id))
        db.commit()
        print("Update Successful!")
    except sqlite3.Error as e:
        print(f"Error updating menu price: {e}")
    
    
def delete_menu_item(db, args):
    cursor = db.cursor()
    try:
        sql_command = "DELETE FROM MenuItem WHERE MenuItemID = ?"
        cursor.execute(sql_command, (args.item_id,))
        db.commit()
        print("Deletion Successful!")
    except sqlite3.Error as e:
        print(f"Error deleting menu item: {e}")
    
    
def delete_employee(db, args):
    cursor = db.cursor()
    try:
        sql_command = "DELETE FROM Employee WHERE EmployeeID = ?"
        cursor.execute(sql_command, (args.employee_id,))
        db.commit()
        print("Deletion Successful!")
    except sqlite3.Error as e:
        print(f"Error deleting employee: {e}")
    
def print_table(db, args):
    cursor = db.cursor()
    try:
        sql_command = f"Select * from {args.table_name}"
        cursor.execute(sql_command)
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row}\n")
    except sqlite3.Error as e:
        print(f"Error printing database: {e}")
        
if __name__ == "__main__":
    parser = establish_cli()
    
    args = parser.parse_args()
    
    db = connect_to_database()
    
    if args.command == "insert_employee":
        insert_employee(db, args)

    elif args.command == "insert_menu_item":
        insert_menu_item(db, args)

    elif args.command == "update_item_price":
        update_menu_price(db, args)

    elif args.command == "delete_menu_item":
        delete_menu_item(db, args)

    elif args.command == "delete_employee":
        delete_employee(db, args)
    elif args.command == "print_table":
        print_table(db, args)
    