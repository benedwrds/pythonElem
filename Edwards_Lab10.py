#Ben Edwards
#This lab collects and displays information for 3 employees
import employee

def main():
    employeeList = []
    EMP = 3 
    i = 0

    while i < EMP:
      name = input("Enter employee name: ")
      idNum = input("Enter employee id: ")
      department = input("Enter employee department: ")
      position = input("Enter position: ")
      print()
      employeeList.append(employee.Employee(name, idNum, department, position))
      i += 1

    for i in employeeList:
        print("Employee " + str(employeeList.index(i) + 1) + " :")
        print(i)
        print()


main()
