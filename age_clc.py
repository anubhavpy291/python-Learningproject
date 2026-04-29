import datetime 
class age:
    month = 0
    year = 0
    date = 0
now = datetime.date.today()
date = int(input("the date in between 1 to 30: "))
while  not date >= 1 or not date <= 30:
    print("not valid input")
    date = int(input("the date in between 1 to 30: "))
month = int(input("the month in between 1 to 12: "))
while  not month >= 1 or not month <= 12:
    print("not valid input")
    month = int(input("the month in between 1 to 12: "))
year = int(input(f"the year in less than {now.year}: "))
while not year < now.year:
    print("not valid input")
    year = int(input(f"the year in less than {now.year}: "))

age.year = abs(now.year - year)
age.date = abs(now.day - date)
age.month = abs(now.month - month)

print(f"you are \nyear:{age.year}..month:{age.month}..day:{age.date}\nold")