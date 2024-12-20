import csv

class Employee : # class representing an employee

    def __init__(self, ID, name, position, salary, email):
        self.ID = ID
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def display(self):
        return f"{self.ID}, {self.name}, {self.position}, {self.salary}, {self.email}"

# class to manage the employee information
class EmployeeManager:
        def __init__(self, filename="employees.csv"):
            self.filename = filename
            self.employees = []
            self.initialize_file()
            self.load_data()



        def initialize_file(self):
            try:
                with open(self.filename, mode="x", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["ID", "Name", "Position", "Salary", "Email"])  # set up the column names or headers
            except FileExistsError:
                pass 

        def load_data(self):  # function to read employee data from the file and adds it

            with open(self.filename, mode="r") as file:
                reader = csv.reader(file)
                next(reader) 
                for row in reader:
                    if row:
                        self.employees.append(Employee(*row))
                    

        def save_data(self):   # writes all employee data back to the file 
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Position", "Salary", "Email"]) 
                for emp in self.employees:
                    writer.writerow([emp.ID, emp.name, emp.position, emp.salary, emp.email])


        def add_employee(self, ID, name, position, salary, email):  # adds a new employee to the system
            if any(emp.ID == ID for emp in self.employees):   # make sure the ID is unique
                print("Error: Employee ID already exists.")
                return
                
            if not salary.isdigit():  # Check if salary is numeric (bonus)
                print("Error: Salary must be a numeric value.")
                return
            self.employees.append(Employee(ID, name, position, salary, email))
            self.save_data()   # save the updated list to the file
            print("Employee added successfully.")



        def update_employee(self, ID):  # updates the details of an existing employee
            for emp in self.employees:
                if emp.ID == ID:
                    print(f"Updating details for {emp.name}...")
                    emp.name = self.get_user_input("Enter new name (or press Enter to keep current): ", emp.name)
                    emp.position = self.get_user_input("Enter new position (or press Enter to keep current): ", emp.position)
                    emp.salary = self.get_user_input("Enter new salary (or press Enter to keep current): ", emp.salary)
                    emp.email = self.get_user_input("Enter new email (or press Enter to keep current): ", emp.email)
                    self.save_data()
                    print("Employee details updated successfully.")
                    return
            print("Error: Employee ID not found.")

        def delete_employee(self, ID):  # deletes an employee by their ID
            for emp in self.employees:
                if emp.ID == ID:  # find the employee by their ID.
                    self.employees.remove(emp)
                    self.save_data()
                    print("Employee deleted successfully.")
                    return
            print("Error: Employee ID not found.")   # if no employee with the given ID is found
        
        def search_employee(self, ID):    # searches for an employee by their ID
            for emp in self.employees:
                if emp.ID == ID:
                    print("Employee found:")
                    print(emp.display())  # show their details
                    return
            print("Error: Employee ID not found.")


        def list_employees(self):  # lists all employees in the system
            if not self.employees:
                print("No employees found.")
            else:
                print("Employee List:")
                for emp in self.employees:
                    print(emp.display())



def main():
    manager = EmployeeManager()
    options = [
        "1. Add Employee",
        "2. Update Employee",
        "3. Delete Employee",
        "4. Search Employee",
        "5. List All Employees",
        "6. Exit"
    ]

    while True:
        print("\n ( Employee Management System )")
        for opt in options:
            print(opt)
        choice = input("Enter your choice: ")
        
        # perform an action based on the user's choice
        if choice == "1":
            ID = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            email = input("Enter Email: ")
            manager.add_employee(ID, name, position, salary, email)
        elif choice == "2":
            ID = input("Enter Employee ID to update: ")
            manager.update_employee(ID)
        elif choice == "3":
            ID = input("Enter Employee ID to delete: ")
            manager.delete_employee(ID)
        elif choice == "4":
            ID = input("Enter Employee ID to search: ")
            manager.search_employee(ID)
        elif choice == "5":
            manager.list_employees()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")    # handles any invalid input

if __name__ == "__main__":
    main()
