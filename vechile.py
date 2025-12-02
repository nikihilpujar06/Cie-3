def vechile_details(v_num,o_name,v_type,year_of_mfg):
    return (
        f"Vechile Number : {v_num}\n"
        f"Owner Name: {o_name}\n"
        f"Vechile Type: {v_type}\n"
        f"Year Of Manufacture : {year_of_mfg}"
    )

if __name__ == "__main__":
    v_num = "111\n"
    o_name = "Jhon\n"
    v_type = "Bike\n"
    year_of_mfg = 2006

    result = vechile_details(v_num,o_name,v_type,year_of_mfg)
    print(result)
