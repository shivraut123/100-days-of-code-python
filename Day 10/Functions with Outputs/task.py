def format_name(f_name,l_name):
    print(f_name.title())
    print(l_name.title())

format_name("shiv","raut")

##############LEAP YEAR #################################
def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False

is_leap_year(2024)



