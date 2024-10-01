# Fractional-Julian-Date.py
#
# Usage: python3 Fractional-Julian-Date.py Year Month Day Hour Minute Second
#  Converts from Gregorian Calendar to Julian calendar
# Parameters:
# Year: What year (gregorian/standard)
# Month: What month (1-12)
# Day: What day (1-31)
# Hour: What hour (0-23)
# Minute: What minute ()
# Second: What second
#
# Output:
#  Gives the julian date
#
# Written by Lee Wallenfang
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv
# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
Year = float('nan')
Month = float('nan')
Day = float('nan')
Hour = float('nan')
Minute = float('nan')
Second = float('nan')

# parse script arguments
if len(sys.argv)==7:
   Year = float(sys.argv[1])
   Month = float(sys.argv[2])
   Day = float(sys.argv[3])
   Hour = float(sys.argv[4])
   Minute = float(sys.argv[5])
   Second = float(sys.argv[6])
else:
   print(\
    'Usage: '\
    'python3 arg1 arg2 ...'\
   )
   exit()

# write script below this line
Y = Year
M = Month
D = Day
H = Hour
Min = Minute
S = Second

JD = D - 32075 + 1461*(Y+4800+(M-14)//12)//4 + 367*(M-2-(M-14)//12*12)//12 - 3*((Y+4900+(M-14)//12)//100)//4
JDmid = JD-0.5
DFrac = (S+60*(Min+60*H))/86400
JD_Frac = JDmid+DFrac

print(JD_Frac)