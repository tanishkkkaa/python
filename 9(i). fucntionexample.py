month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year):
 """return true for leap year and false for non leap year """
 return year % 4 == 0 and (year%100!=0 or year%400==0)
def number_of_days(year,month):
    """return number of days in that year and month"""
    if not 1<=month<=12:
      return 'invalid input'
    
    if month ==2 and leap_year(year):
      return 29

    return month_days[month]
print(leap_year(2020))
print(number_of_days(2024,2))