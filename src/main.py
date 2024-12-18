employee = []

# Acyuta, 1324, CEO, $7,000,000, 20 years

print("Add employee - 1\nRemove employee - 2\nChange role - 3\nChange salary - 4\nExit - 5")
n = input('| ')

while n!='5':
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
      exp = input('Please enter the number of years of experience \n1| ')
      print('-------------------------------------------------------')
  
      e.extend([name, reg_num, role, sal, exp])
      employee.append(e)
    print(employee) 
  
  if n=='2':
    num = input('Enter the registration number | ')
    for i in employee:
      if employee[int(i)][2] == num:
        employee.pop(employee[i][2])
  
  if n=='3':
    num = input('Enter the registration number \n| ')
    nrole = input('Enter the new role | ')
    for i in employee:
      if employee[int(i)][2] == num:
        employee[int(i)][3] == nrole
    
