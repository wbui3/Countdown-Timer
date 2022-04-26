from datetime import date

def countdown(yr,mo,dy):
    currDate = date.today()
    months30 = [4, 6, 9, 11]
    if (mo == 2 and dy > 28 and yr%4 > 0):
        print("Invalid February dates. Exiting")
        return
    elif (mo in months30 and dy > 30):
        print("Invalid dates for months with 30 days. Exiting")
        return
    targetDate = date(yr,mo,dy) # 2022,7,30
    daysRemaining = targetDate - currDate
    if int(daysRemaining.days) < 0:
        print("The date has already passed")
    elif int(daysRemaining.days) == 0:
        print("The deadline is today!")
    elif int(daysRemaining.days) < 32:
        print("The date today is ", currDate.month, currDate.day, currDate.year)
        print("The target date is ", targetDate.month, targetDate.day, targetDate.year)
        print("Days left: " + str(daysRemaining.days))
    else:
        shortDate(daysRemaining.days)

        
def shortDate(inputDays):
    if (inputDays > 30):
        remainingDays = inputDays%30
        remainingMonths = inputDays//30 
        print("Time left: " + str(remainingMonths) + " months, " + str(remainingDays) + " days left")

        
# example date
countdown(2022,5,26)
