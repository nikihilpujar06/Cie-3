from vechile import vechile_details 
def vechile_details():
    expected_output = (
        "Vechile Number: 111\n"
        "Owner Name: John\n"
        "Vechile Type: Bike\n"
        "Year Of Manufacture: 2006"
    )
    assert employee_details("111","Jhon","Bike",2006) ==  expected_output
