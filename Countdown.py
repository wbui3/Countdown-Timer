from datetime import date

def countdown(yr,mo,dy):
    currDate = date.today()
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
