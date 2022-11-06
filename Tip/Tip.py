def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #remove $
    no_dollar_sign = d.replace("$" , "")
    #return the value in float
    return float(no_dollar_sign)


def percent_to_float(p):
    #remove %
    no_percent_sign = p.replace("%" , "")
    #hwile converting it to float value divide it to 100
    p_converted = float(no_percent_sign) / 100
    return p_converted


main()