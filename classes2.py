# Q1
class Login:
    def __init__(self,password):
        self.__password=password

    def check_password(self):
        if self.__password == "12345":
            return True

login=Login("12345")
print(login.check_password())

# Q2
class BaseTest:
    def setup(self):
        print("Browser Opened")

class LoginTest(BaseTest):
    def test_login(self):
        print("Login test executed")

l=LoginTest()
l.setup()
l.test_login()

# Q3
class Chrome:
    def start(self):
        print("Chrome started")

class Firefox:
    def start(self):
        print("Firefox started")

c=Chrome()
f=Firefox()
c.start()
f.start()

# Q4
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPIPayment(Payment):
    def pay(self):
        print("Pay")
class CreditCardPayment(Payment):
    def pay(self):
        print("Pay")   

u=UPIPayment()
u.pay()
c=CreditCardPayment()
c.pay()

# Q5
# Inheritance-One class reuse the properties of another class
# Polymorphism-Different object respond to same method /operation in different way
# Abstraction-Showing only neccessary details while hiding unneccessary implementation details
# Encapsulation-Keeping data and methods together and controls how internal data are accessed