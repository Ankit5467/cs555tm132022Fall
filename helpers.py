# Define helper functions here (Eg: Data transformation, formulas, etc.)


DAY_IND = 0
MONTH_IND = 1
YEAR_IND = 2

month_mappings = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}

# Input: list of dictionary object
# Output: list of lists, where each inner list corresponds to the values of a dictionary object.
# Note: Doesnt modify the input
def listOfDictsToNestedList(listOfDicts):
    return list(map(lambda x: list(x.values()), listOfDicts))


# Input: Date String in format: 'DAY MONTH YEAR', where DAY 1-31, MONTH = month abreviation, YEAR = a year.
# Output: A tuple of format: (DAY, MONTH, YEAR) that corresponds to a date, where 1 <= DAY <= 31, 1 <= MONTH <= 12, 1 <= YEAR <= 2022
def convertDateStrToDateTuple(dateStr):
    day = int(dateStr.split(" ")[0])
    month= month_mappings[dateStr.split(" ")[1]]
    year= int(dateStr.split(" ")[2])
    # print((day,month,year))
    return (day,month,year)