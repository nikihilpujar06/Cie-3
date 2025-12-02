def vechile_details(v_num,o_name,v_type,year_of_mfg):
    return (
        f"Vechile Number : {v_num}"
        f"Owner Name: {o_name}"
        f"Vechile Type: {v_type}"
        f"Year Of Manufacture : {year_of_mfg}"
    )

if __name__ == "__main__":
    v_num = "111"
    o_name = "Jhon"
    v_type = "Bike"
    year_of_mfg = 2006

    result = vechile_details(v_num,o_name,v_type,year_of_mfg)
    print(result)