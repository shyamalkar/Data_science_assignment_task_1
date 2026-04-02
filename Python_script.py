def main_menu():
    """Displays the main menu and handles user navigation."""
    # Step 1: Initialize the dictionary with sample data
    employees = {
        101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
    }

    while True:
        print("\n--- Employee Management System (EMS) ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee(employees)
        elif choice == '2':
            view_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            print("Thank you for using the EMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def add_employee(employees):
    """Adds a new employee to the dictionary."""
    try:
        while True:
            emp_id = int(input("Enter Employee ID: "))
            # Validate unique ID
            if emp_id in employees:
                print(f"Error: ID {emp_id} already exists. Please enter a unique ID.")
            else:
                break
        
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        dept = input("Enter Department: ")
        salary = float(input("Enter Monthly Salary: "))

        # Store in dictionary
        employees[emp_id] = {
            'name': name, 
            'age': age,
            'department': dept,
            'salary': salary
        }
        print(f"Employee '{name}' added successfully!")
    
    except ValueError:
        print("Invalid input. Please ensure ID, Age, and Salary are numbers.")

def view_employees(employees):
    """Displays all employee details in a table-like structure."""
    if not employees:
        print("No employees available.")
        return

    print(f"\n{'ID':<10} {'Name':<15} {'Age':<10} {'Department':<15} {'Salary':<10}")
    print("-" * 60)
    for emp_id, info in employees.items():
        print(f"{emp_id:<10} {info['name']:<15} {info['age']:<10} {info['department']:<15} {info['salary']:<10}")

def search_employee(employees):
    """Searches for an employee by their unique ID."""
    try:
        search_id = int(input("Enter the Employee ID to search: "))
        if search_id in employees:
            emp = employees[search_id]
            print(f"\nEmployee Found:")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")

if __name__ == "__main__":
    main_menu()
