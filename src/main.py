employee = []

# Acyuta, 1324, CEO, $7,000,000, 20 years - This is how one entry of the list is supposed to work

#Query 1
print("Add employee - 1\nRemove employee - 2\nChange role - 3\nChange salary - 4\nPrint list - 5\nExit - 6")
n = input('| ')

while n!='6': #Main Loop for the program to run until the client chooses 6
  if n=='1': #Adding Employees
    n = int(input("How many employees do you want to add? \n| "))
  
    if type(n) != int: #Error Handling
      print("Please enter a numerical value")
  
    for i in range(n):
      e = []
      reg_num = input('Please enter the employee\'s registration number \n| ')
      name = input('Please enter the name of the employee \n| ')
      dob = input('Please enter the date of birth \n| ')
      doj = input('Please enter the date of joining \n| ')
      exp = input('Please enter the number of years of experience \n| ')
      role = input('Please enter the employee\'s role \n| ')
      sal = input('Please enter the employee\'s salary \n| ')
      print('-------------------------------------------------------')
  
      e.extend([name, reg_num, role, sal, exp])
      employee.append(e)
    print(employee) 
  
  elif n=='2': #Removing Employees
    num = input('Enter the registration number \n| ')
    for i in range(0,len(employee)):
      if employee[i][1] == num:
        employee.pop(i)
      print(employee)
  
  elif n=='3': #Changing Roles
    num = input('Enter the registration number \n| ')
    nrole = input('Enter the new role \n| ')
    for i in (0,len(employee)):
      if employee[i][1] == num:
        employee[i][2] == nrole
      print(employee)
  
  elif n=='4': #Changing Salaries
    num = input("Enter the registration number \n| ")
    nsal = input("Enter the new salary \n| ")
    for i in (0,len(employee)):
      if employee[i][1] == num:
        employee[i][3] == nsal
      print(employee)

  elif n=='5': #Printing List
    print(employee)

  elif n=='6': #Exiting
    break
    
  n=input('| ') #Repeating the loop
 
#End of Program 