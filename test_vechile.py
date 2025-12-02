def vehicle_details(v_num, o_name, v_type, year_of_mfg):
    return (
        f"Vehicle Number: {v_num}\n"
        f"Owner Name: {o_name}\n"
        f"Vehicle Type: {v_type}\n"
        f"Year of Manufacture: {year_of_mfg}"
    )

expected = (
    "Vehicle Number: 111\n"
    "Owner Name: Jhon\n"
    "Vehicle Type: Bike\n"
    "Year of Manufacture: 2006"
)

assert vehicle_details("111", "Jhon", "Bike", 2006) == expected
