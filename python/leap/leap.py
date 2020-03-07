def leap_year(year):
    a = not(year % 4 )
    b = not(year % 100) and not(year % 400) or bool(year % 100)
    return all([a,b])

# better solution
# return x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)