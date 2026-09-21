# Q1
def test_status():
    Expected_status = 200
    Actual_status = 200
    print("Status checking")
    assert Expected_status == Actual_status

#Q2
def test_details():
    Expected_username = "admin"
    Actual_username = "admin"
    print("admin checking")
    assert Expected_username == Actual_username

#Q3
def test_result():
    Expected_login_result = "Success"
    Actual_login_result = "Success"
    assert Expected_login_result == Actual_login_result
