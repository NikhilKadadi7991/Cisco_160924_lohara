class Employee:
    def __init__(self,name,address,code,salary):
        self.name=name
        self.address=address
        self.code=code
        self.salary=salary
    def __str__(self):
        return f'{self.name}, {self.address}, {self.code}, {self.salary} '
    
mahesh = Employee('Maheswaran','2/21, alagu nagar','PYAB10021', 2000000)
print(mahesh)