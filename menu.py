from repositoryEmployee import employeeRepository
# repository = employeeRepository()
# getEmployees = repository['getEmployees']

def printMenu():
   print("Select an option: ")
   print("1 - Insert employee")
   print("2 - Delete employee")
   print("3 - Search a employee by id")
   print("4 - Show all employees")
   print("5 - Show employees for role")
   print("6 - Exit")

def runOption():
   repository = employeeRepository()
   getEmployees = repository['getEmployees']   
   insertEmployee = repository['insertEmployee']
   getEmployeeById = repository['getEmployeeById']   
   deleteEmployee = repository['deleteEmployee']    
   searchEmployeesByRole = repository['searchEmployeesByRole']
   option = int(input())
  
   options = {
      1: 'oi',
      2: lambda: inputDeleteEmployee(deleteEmployee),
      3: lambda: inputGetEmployeeById(getEmployeeById),
      4: getEmployees,
      5: lambda: inputGetEmployeeForRole(searchEmployeesByRole)
   }

   fn = options.get(option)
   if not fn:
      print('Invalid option')
   else:
      fn()

def inputGetEmployeeById(callback):
   id = input('Enter the employee ID: ')
   if not id:
      return runOption()
   printEmp = lambda emp: print(emp)
   callback(id,printEmp)

def inputGetEmployeeForRole(callback):
   role = input('Enter the employee role: ')
   if not role:
      return runOption()
   callback(role)

def inputDeleteEmployee(callback):
   id = input('Enter the ID of employee you want to delete')
   if not id:
      return runOption()
   callback(id)

printMenu()
runOption()
# repository = employeeRepository()
# print(repository['getEmployees'])