# Q1
class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role

emp=Employee("Sindhuja","QA Tester")
print(emp.name)
print(emp.role)

# Q2
class Calculator:
    def add(self,n1,n2):
        return n1+n2

    def subtract(self,n1,n2):
            return n1-n2

    def multiply(self,n1,n2):
            return n1*n2

calc=Calculator()
print(calc.add(2,3))
print(calc.subtract(2,3))
print(calc.multiply(2,3))

# Q3
class APITest:
    def __init__(self,api_name,status_code):
        self.api_name=api_name
        self.status_code=status_code

    def validate_status(self):
        if self.status_code ==200:
            print("API Test Passed")
        else:
             print("API Test Failed")

api=APITest("Login",200)
api.validate_status()

# Q4
# 1.class is a blueprint /template for creating structure or layout for object
# 2.object is an instance of class.its a real world entity contain attributes and behaviors
# 3.Method is reusable block of code and function inside the class.
# 4.self refers to the current object
# 5.__init__() used to initialize the data 


          

        