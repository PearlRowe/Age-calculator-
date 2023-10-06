# ROWE PEARL ROWENA INDANA
#SCT211-0678/2021
name = input("enter your name here")
print("hello" + name)
Num1 =int(input("enter first number"))
Num2 = int(input("enter second number"))
Sum = Num1 + Num2
print (name,"the sum of",Num1,"and", Num2,"is", Num1+ Num2)
#age
import datetime
currentDate = datetime.datetime.now()

deadline= input (" enter your date of birth (mm/dd/yyyy) ")
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
print (deadlineDate)
daysLeft = deadlineDate - currentDate
print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)

months=(years-yearsInt)*12
monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)
daysInt=int(days)

print("You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, old.".format(yearsInt,monthsInt,daysInt))
