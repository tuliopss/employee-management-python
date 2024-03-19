from repositoryEmployee import employeeRepository
from employeeHelpers import checkIfEmployeeExist, queryGetEmployeeById


def printMenu():
    print("Select an option: ")
    print("1 - Insert employee")
    print("2 - Delete employee")
    print("3 - Search a employee by id")
    print("4 - Show all employees")
    print("5 - Show employees for role")
    print("6 - Edit employee")
    print("7 - Exit")

def runOption():
    repository = employeeRepository()
    getEmployees = repository['getEmployees']   
    insertEmployee = repository['insertEmployee']
    editEmployee = repository['editEmployee']
    getEmployeeById = repository['getEmployeeById']   
    deleteEmployee = repository['deleteEmployee']    
    searchEmployeesByRole = repository['searchEmployeesByRole']
    option = int(input("Enter your choice: "))
  
    options = {
        1: lambda: inputInsertEmployee(insertEmployee),
        2: lambda: inputDeleteEmployee(deleteEmployee),
        3: lambda: inputGetEmployeeById(getEmployeeById),
        4: getEmployees,
        5: lambda: inputGetEmployeeForRole(searchEmployeesByRole),
        6: lambda: inputEditEmployee(editEmployee),    
        7: exitProgram,
            
    }

    fn = options.get(option)
    if not fn:
        print('Invalid option')
    else:
        fn()
        executeMenu()

def inputInsertEmployee(callback):
    name = input("Enter employee name: ")
    email = input("Enter employee email: ")
    role = input("Enter employee role: ")
    salary = float(input("Enter employee salary: "))
    callback(name, email, role, salary)

def inputGetEmployeeById(callback):
    id = input('Enter the employee ID: ')
    if not id:
        return runOption()
    
    callback(id, printEmp)  # A função de callback deve ser passada aqui

def inputEditEmployee(callback):
     id = input('Enter the employee ID: ')
     if not id:
        return runOption()
     employee = queryGetEmployeeById(id)
     checkIfEmployeeExist(employee)
     if employee: #Tive que fazer a verificacao pra acso o id nao seja encontrado, ja encerre aqui e nao depois dos inputs
        updatedName = input("Enter the new name: ")
        updatedRole = input("Enter the new role: ")
        updatedSalary = input("Enter the new salary: ")
        callback(id, updatedName, updatedRole, updatedSalary)


def printEmp(emp):
    print(emp)


def inputGetEmployeeForRole(callback):
    role = input('Enter the employee role: ')
    if not role:
        return runOption()
    callback(role)

def inputDeleteEmployee(callback):
    id = input('Enter the ID of employee you want to delete: ')
    if not id:
        return runOption()
    callback(id)

def exitProgram():
    print("Program closed.")
    exit()

def executeMenu():
    printMenu()
    runOption()
