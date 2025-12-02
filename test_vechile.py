def vechile_details(v_num, o_name, v_type, year_of_mfg):
    return (
        f"Vechile Number: {v_num}\n"
        f"Owner Name: {o_name}\n"
        f"Vechile Type: {v_type}\n"
        f"Year of Manufacture: {year_of_mfg}"
    )

expected = (
    "Vechile Number: 111\n"
    "Owner Name: Jhon\n"
    "Vechile Type: Bike\n"
    "Year of Manufacture: 2006"
)
assert vechile_details("111", "Jhon", "Bike", 2006) == expected
