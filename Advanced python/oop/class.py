class Employee:
    def __init__(self,id,name):
        # self.new_id=id
        # self.new_name=name
        self.id=id
        self.name=name

emp=Employee(1,'kdsr')
# print(emp.id)
# print(emp.name)

del emp.id
# Deleting the object itself
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")
