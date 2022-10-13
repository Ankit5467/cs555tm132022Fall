# Define helper functions/variables here (Eg: Data transformation, formulas, etc.)
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

# Helper Function
# Input: 2 date tuples of the form: (day, month, year)
# Output: returns the number of [whole] days [rounded up] between the 2 dates
# Note: 
# return value is positive if to_date is after from_date,
# negative if to_date is before from_date,
# and zero if to_date == from_date.
def timeBetweenDatesSigned(from_date, to_date):
    fromDate = date(from_date[2], from_date[1], from_date[0])
    toDate = date(to_date[2], to_date[1], to_date[0])
    difference = toDate-fromDate
    return int(difference.days)

# Flattens a nested list
# Taken from: https://stackoverflow.com/questions/12472338/flattening-a-list-recursively
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

#------FAMILY FUNCTION HELPERS----------------

# Input: an id string and a list of individuals
# Output: The person object corresponding to id
# Note: Does NOT modify the input.
def getPersonFromId(id, people):
   personObj =  list(filter(lambda person: person['ID'] == id, people)) # Need to return a default value of []
   if personObj==[]:
       return []
   return personObj[0]

# Input: an id string and a list of individuals (list of dictionaries w/ each dictionary representing a personObj)
# Output: The name of the person corresponding to the inputted id OR an error message.
# Note: Does NOT modify the input.
def getNameFromId(id, people):
    for indi in people:
        if indi['ID'] == id:
            return indi['name']
    return 'Error: Id does not exist!'

# Input: an id string and a list of families
# Output: The family object corresponding to id
# Note: Does NOT modify the input.
def getFamilyFromId(id, families):
    for fam in families:
        if fam['ID'] == id:
            return fam
    return {} #Id does not exist!

# Input: list of family objects and a id in string format
# Output: the family object the corresponds to the string id             
def FamilybyID(families, id):
    for fam in families:
        if fam['ID'] == id:
            return fam


# Input: person object
# Output: returns a list of families objects
def getFamilesFromPerson(personObj, families):
    listOfFam = []
    for fam_id in personObj["spouse"]:
        famObj = getFamilyFromId(fam_id, families)
        if famObj != {}:
            listOfFam.append(famObj)
    return listOfFam

# Purpose: Helper function that returns a list of the given person's childrens' IDs
# Input: A person object and the families list
# Output: Returns a list of string IDs.
def getChildren(personObj, families):
    theFamilies = getFamilesFromPerson(personObj, families) # list of fam objs
    children = list(map(lambda fam: fam['children'], theFamilies))
    return flatten(children)

# Purpose: Helper Getter Function that returns a list of descendants of a person (children, grandchildren, etc. Also returns step children)
# Input: A person object, the families list, and people list.
# Output: List of People IDs
def getDescendants(personObj, families, people):
    childrenIds = getChildren(personObj, families) # list of string IDs
    if len(childrenIds) == 0:
        return []
    return flatten(childrenIds + list(map(lambda childID: getDescendants(getPersonFromId(childID, people), families, people), childrenIds)))

# Purpose: Helper Getter Function that returns a list of ppl the given person is/was married to
# Input: A person object, the families list, and people list.
# Output: List of People IDs
def getSpouses(personObj, families):
    personFamsIDs = personObj['spouse']
    spouses = []
    
    for id in personFamsIDs:
        famObj = getFamilyFromId(id, families)
        if famObj != {}:
            spouse = [famObj['husband_id']] + [famObj['wife_id']]
            spouses = spouses + spouse
    
    return list(set(spouses)) # remove duplicates