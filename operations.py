# Define feature functions (user story functions) and variables in this file:

from datetime import date, datetime

# Import helper functions
from helpers import *

# Import constants
from helpers import DAY_IND, MONTH_IND, YEAR_IND

# familes = []
# individuals = []

# Input: an id string and a list of individuals (list of dictionaries w/ each dictionary representing a personObj)
# Output: The name of the person corresponding to the inputted id OR an error message.
# Note: Does NOT modify the input.


def getNameFromId(id, people):
    for indi in people:
        if indi['ID'] == id:
            return indi['name']
    return 'Error: Id does not exist!'

# User Story #1 -- Eric
# Input: A person object/dictionary
# Output: Returns true if every date [birth, death, marriage, divorce] occurs before death on an individual. False otherwise.
# Note: If alive, assume death is negligible. Death, marriage, divorce could be N/A. Will true in this case.


def datesBeforeToday(personObj):
    todayTuple = getTodayDateTuple()
    birthdayTuple = convertDateStrToDateTuple(personObj['birthday'])
    deathdayTuple = convertDateStrToDateTuple(personObj['death'])
    # marriagedayTuple = convertDateStrToDateTuple(personObj['married'])
    # divorcedayTuple = convertDateStrToDateTuple(personObj['divorced'])

    if birthdayTuple[YEAR_IND] > todayTuple[YEAR_IND]:  # birth year after current year
        return False
    # birth year before or is current year
    if birthdayTuple[YEAR_IND] == todayTuple[YEAR_IND]:
        # birth month after current month
        if birthdayTuple[MONTH_IND] > todayTuple[MONTH_IND]:
            return False
        # birth month after current month
        elif birthdayTuple[MONTH_IND] == todayTuple[MONTH_IND]:
            if birthdayTuple[DAY_IND] > todayTuple[DAY_IND]:  # birth day after current day
                return False
    if not personObj['alive']:  # testing death dates now
        if deathdayTuple[YEAR_IND] > todayTuple[YEAR_IND]:  # death year after current year
            return False
        # death year before or is current year
        elif deathdayTuple[YEAR_IND] == todayTuple[YEAR_IND]:
            # death month after current month
            if deathdayTuple[MONTH_IND] > todayTuple[MONTH_IND]:
                return False
            # death month before or is current month
            elif deathdayTuple[MONTH_IND] == todayTuple[MONTH_IND]:
                # death day after current day
                if deathdayTuple[DAY_IND] > todayTuple[DAY_IND]:
                    return False
    return True


# User Story #3 -- Ankit
# Input: A person object/dictionary
# Output: Returns true if birth occurs before death on an individual. False otherwise. False should be logged as an error.
# Note: Returns true if person is not dead.
# Question: Can someone die on the same day they were born? This function assumes thats allowed


def birthBeforeDeath(personObj):
    if personObj['alive']:
        return True
    else:

        birthdayTuple = convertDateStrToDateTuple(personObj['birthday'])
        deathdayTuple = convertDateStrToDateTuple(personObj['death'])

        if birthdayTuple[YEAR_IND] > deathdayTuple[YEAR_IND]:
            return False
        elif birthdayTuple[YEAR_IND] < deathdayTuple[YEAR_IND]:
            return True
        else:
            # Check month:
            if birthdayTuple[MONTH_IND] < deathdayTuple[MONTH_IND]:
                return True
            elif birthdayTuple[MONTH_IND] > deathdayTuple[MONTH_IND]:
                return False
            else:
                # Check day:
                return birthdayTuple[DAY_IND] <= deathdayTuple[DAY_IND]

# User Story #7 -- Eric
# Input: a person object
# Output: boolean
# True [if death is less than 150 years after birth] and current date is less than 150 years after birth for living peopel, False otherwise
# This assumes a standard 4-year leap year schedule. 150 years includes 37 leap years and 113 regular years. 54787 days = 150 years.


def lessThan150(personObj):
    todayTuple = getTodayDateTuple()
    birthdayTuple = convertDateStrToDateTuple(personObj['birthday'])
    if personObj['alive'] == True:
        days = timeBetweenDays(birthdayTuple, todayTuple)
        if (days > 54787):
            return False
        else:
            return True
    else:  # Dead, so compare the days between birth and death.
        deathdayTuple = convertDateStrToDateTuple(personObj['death'])
        days = timeBetweenDays(deathdayTuple, birthdayTuple)
        if (days > 54787):
            return False
        else:
            return True


# User Story #27 -- Ankit
# Input: a person object/dictionary
# Output: Computes the age of the person
# Note: DOES modify the input- slightly formats the person object to make date extraction easier for future uses.
# Question: SHould the program accept future dates?


def computeAge(personObj):
    bdayLen = len(personObj['birthday'].split(' ')[0])
    if bdayLen == 1:
        personObj['birthday'] = '0' + personObj['birthday']

    birthday_datetime_obj = datetime.strptime(
        personObj['birthday'], '%d %b %Y')

    end = ''

    if personObj['death'] == 'NA':
        end = date.today()
    else:
        ddayLen = len(personObj['death'].split(' ')[0])
        if ddayLen == 1:
            personObj['death'] = '0' + personObj['death']
        end = datetime.strptime(personObj['death'], '%d %b %Y')

    age = end.year - birthday_datetime_obj.year - \
        ((end.month, end.day) < (birthday_datetime_obj.month, birthday_datetime_obj.day))
    return age
