# this is to read the input from terminal
import sys

try:
    month = int(sys.argv[1])
    year = int(sys.argv[2])



    # This is to find the day on which the month starts
    from datetime import date
    d = date(year,month,1)
    day_of_week = (d.weekday()+1)%7


    month = month-1 # because indx in list starts from zero

    def days_in_february():
        if year % 100 ==0 and year % 400 == 0:
            return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28
   

    list_of_months = ["January",  "February", "March", "April", "May", "June",
                  "July", "August",  "September",  "October", "November",
                  "December"
    ]

    month_name = list_of_months[month]

    num_of_days = [ 31,  days_in_february() ,  31,  30,  31,  30, 31,  31,   30,   31, 30, 31]



    print(f"{month_name} {year}".center(20))

    print("Su Mo Tu We Th Fr Sa")
    print("   " * day_of_week, end="")


    for day in range(1, num_of_days[month]+1):
        print(f"{day:2}", end=" ")
        day_of_week += 1
        if day_of_week == 7: # wrap to next line after Saturday
            print()
            day_of_week = 0

    print("\n") # to get rid of the percent sign that is seen after the progam succesfully runs.

except Exception as e:
    print(str(e))
