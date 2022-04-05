from datetime import date

def countdown(yr,mo,dy):
    currDate = date.today()
    ############ Error checking ############
    months31=[1, 3, 5, 7, 8, 10, 12]
    months30 = [4, 6, 9, 11]
    if (mo == 2 and dy > 28 and yr%4 > 0):
        print("Invalid february dates. Exiting")
        return
    elif (mo in months31 and dy > 31):
        print("Invalid dates for months with 31. Exiting")
        return
    elif (mo in months30 and dy > 30):
        print("Invalid dates for months with 30. Exiting")
        return
    ############ Error checking ############
    targetDate = date(yr,mo,dy) # 2022,7,30
    daysRemaining = targetDate - currDate
   if int(daysRemaining.days) < 0:
        print("The date has already passed")
    elif int(daysRemaining.days) == 0:
        print("The deadline is today!")
    else:
        print("The date today is ", currDate.month, currDate.day, currDate.year)
        print("The target date is ", targetDate.month, targetDate.day, targetDate.year)
        print("Days left: " + str(daysRemaining.days))

countdown(2022,7,30)
