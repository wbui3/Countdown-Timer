from datetime import date

def countdown(yr,mo,dy):
    currDate = date.today()
    targetDate = date(yr,mo,dy) # 2022,7,30
    daysRemaining = targetDate - currDate
    print("The date today is ", currDate.month, currDate.day, currDate.year)
    print("The target date is ", targetDate.month, targetDate.day, targetDate.year)
    print("Days left:" + str(daysRemaining))

countdown(2022,7,30)