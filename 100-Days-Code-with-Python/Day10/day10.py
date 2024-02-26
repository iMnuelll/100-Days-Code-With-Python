# Functions with outputs
def format_name(f_name, l_name) :
    # Multiple return values
    """Return a name into  title format"""
    if f_name == "" or l_name == "" :
        return("You did't provide valid inputs")
    return(f"{f_name.title()} {l_name.title()}")
print(format_name('ImNUEL', 'uNEPUTY'))

# Days In Month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
    
def days_in_month(year, month):
  month -= 1
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == True :
    month_days[1] = 29
    return (month_days[month])
  return (month_days[month])
  
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)