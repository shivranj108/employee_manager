employee = []

# Acyuta, 1324, CEO, $7,000,000, 20 years

print("Add employee - 1\nRemove employee - 2\nChange role - 3\nChange salary - 4\nPrint list - 5\nExit - 6")
n = input('| ')

while n!='6':
  if n=='1':
    n = int(input("How many employees do you want to add? \n| "))
  
    if type(n) != int:
      print("Please enter a numerical value")
  
    for i in range(n):
      e = []
      name = input('Please enter the name of the employee \n| ')
      reg_num = input('Please enter the employee\'s registration number \n| ')
      role = input('Please enter the employee\'s role \n| ')
      sal = input('Please enter the employee\'s salary \n| ')
      exp = input('Please enter the number of years of experience \n| ')
      print('-------------------------------------------------------')
  
      e.extend([name, reg_num, role, sal, exp])
      employee.append(e)
    print(employee) 
  
  elif n=='2':
    num = input('Enter the registration number \n| ')
    for i in range(0,len(employee)):
      if employee[i][1] == num:
        employee.pop(i)
      print(employee)
  
  elif n=='3':
    num = input('Enter the registration number \n| ')
    nrole = input('Enter the new role \n| ')
    for i in (0,len(employee)):
      if employee[i][1] == num:
        employee[i][2] == nrole
      print(employee)
  
  elif n=='4':
    num = input("Enter the registration number \n| ")
    nsal = input("Enter the new salary \n| ")
    for i in (0,len(employee)):
      if employee[i][1] == num:
        employee[i][3] == nsal
      print(employee)

  elif n=='5':
    print(employee)

  elif n=='6':
    break
    
  n=input('| ')
 
