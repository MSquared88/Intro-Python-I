"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# get the command line arguments minus the file path
cli_args = sys.argv[1:]

#get todays infor and set it to a  var
now = datetime.now()

# make a function that outputs the proper response 
# depending on how many args ar sent

def get_month(m = now.month, y = now.year, *args):

    # if more than 2 arguments ar given an error text will appear
    if  args:
        print("month and year are the only arguments needed")
    else:
        print(calendar.month(int(y), int(m)))

get_month(*cli_args)