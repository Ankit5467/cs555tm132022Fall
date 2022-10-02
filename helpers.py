# Define helper functions here (Eg: Data transformation, formulas, etc.)
from datetime import date

DAY_IND = 0
MONTH_IND = 1
YEAR_IND = 2

month_mappings = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5,
                  "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}

# Input: list of dictionary object
# Output: list of lists, where each inner list corresponds to the values of a dictionary object.
# Note: Doesnt modify the input
def listOfDictsToNestedList(listOfDicts):
    return list(map(lambda x: list(x.values()), listOfDicts))


# Input: Date String in format: 'DAY MONTH YEAR', where DAY 1-31, MONTH = month abreviation, YEAR = a year.
# Output: A tuple of format: (DAY, MONTH, YEAR) that corresponds to a date, where 1 <= DAY <= 31, 1 <= MONTH <= 12, 1 <= YEAR <= 2022
def convertDateStrToDateTuple(dateStr):
    day = int(dateStr.split(" ")[0])
    month = month_mappings[dateStr.split(" ")[1]]
    year = int(dateStr.split(" ")[2])
    # print((day,month,year))
    return (day, month, year)

# Note: date.today() comes in the form yyyy-mm-dd
# Returns a Date Tuple for today's specific date
def getTodayDateTuple():
    today = date.today()
    day = int(today.strftime("%d"))
    month = int(today.strftime("%m"))
    year = int(today.strftime("%Y"))
    return (day, month, year)

# Takes in two dateTuples and outputs a number, in days, the two days are apart
def timeBetweenDays(day1, day2):
    date1 = date(day1[2], day1[1], day1[0])
    date2 = date(day2[2], day2[1], day2[0])
    difference = date1-date2
    return abs(int(difference.days))
