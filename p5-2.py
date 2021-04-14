def isLeapYear(year):
       if year%4==0:
          return True
       if year%100==0:
          return False
       if year%400==0:
          return True
       else:
           return False
def daysInMonth(year,month):
    if month in (1,3,5,7,8,10,12):
       return 31
    else:
        if month==2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30
def dateIsbefore(year1, month1, day1, year2, month2, day2):  
    if year1 < year2:
        return True
    if year1 == year2:
        if month1< month2:
            return True
        if month1==month2:
            return day1<day2
def next(year,month,day):
    if day<daysInMonth(year,month):
       return year,month,day + 1
    else:
        if month < 12:
           return year, month +1,1
        else:
            return year +1 ,1,1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  
   d=0
   while dateIsbefore(year1, month1, day1, year2, month2, day2):
         year1,month1,day1=next(year1,month1,day1)
         d+=1
   return d
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
