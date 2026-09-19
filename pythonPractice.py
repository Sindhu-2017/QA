# Q1
name="Sindhuja"
age=23
role="QA Tester"
print("Name :",name)
print("Age :",age)
print("Role :",role)

# Q2
number=int(input("Enter the number :"))
if number >0:
    print("Positive")
elif number <0:
    print("negative")
else:
    print("Zero")


# Q3
browsers=["chrome","microsoft edge","safari","firefox","browser5"]
for browser in browsers:
    print(browser)

# Q4
dict1={"name":"Sindhu","email":"sindhu@gmail.com","role":"QA Tester","experience":1}
for key,value in dict1.items():
    print(key,"=",value)

# Q5
def check_login(username,password):
    if username=="Admin" and password=="12345":
        print("Login successful")
    else:
        print("Invalid credentials")

check_login("Admin","12345")

# Q6
actual_status = 200
expected_status = 200
assert actual_status == expected_status


# Q7
def API_status(api_code):
    if api_code == 200:
        print("API test passed")
    elif api_code == 400:
        print("Bad request")
    elif api_code == 401:
        print("Unauthorized")
    elif api_code == 500:
        print("Server error")

API_status(200)
API_status(400)
API_status(401)
API_status(500)

