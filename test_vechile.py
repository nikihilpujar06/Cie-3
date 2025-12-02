def vehicle_details(v_num, o_name, v_type, year_of_mfg):
    return (
        f"Vehicle Number : {v_num}\n"
        f"Owner Name: {o_name}\n"
        f"Vehicle Type: {v_type}\n"
        f"Year Of Manufacture : {year_of_mfg}"
    )

if __name__ == "__main__":
    v_num = "111"
    o_name = "Jhon"
    v_type = "Bike"
    year_of_mfg = 2006

    result = vehicle_details(v_num, o_name, v_type, year_of_mfg)
    print(result)
