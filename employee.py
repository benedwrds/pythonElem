#Ben Edwards in conjunction with Lab 10

class Employee():
  def __init__(self, name, idNum, department, job):
    self.__name = name
    self.__idNum = idNum
    self.__department = department
    self.__job = job
  def set_name(self, name):
    self.__name = name
  def get_name(self):
    return self.__name
  def set_id(self, idNum):
    self.__idNum = idNum
  def get_id(self):
    return self.__idNum
  def set_department(self, department):
    self.__department = department
  def get_department(self):
    return self.department
  def set_job(self, job):
    self.__job = job
  def get_job(self):
    return self.__job
  def __str__(self):
    #return self.name + "\t" + self.id + "\t" + self.department + "\t" + self.job
    return "Name: " + self.__name + "\nID Number: " + self.__idNum + \
    "\nDepartment: " + self.__department + "\n" + "Title: " + self.__job
