# Define feature functions (user story functions) in this file:

from datetime import date, datetime
from functools import reduce
from tkinter.font import families

# Import helper functions
from helpers import *

# Input: an id string and a list of individuals (list of dictionaries w/ each dictionary representing a personObj)
# Output: The Date of Death of the person corresponding to the inputted id OR an error message.
# Note: Does NOT modify the input.


def GetDeathFromId(people, id):
    for indi in people:
        if indi['ID'] == id:
            return indi['death']
    return 'Error: Id does not exist!'

# Input: two dates in tuple format
# Output: returns true if a date occurs after death date, or false of otherwise


def compareDeath(date, death):
    if date[YEAR_IND] < death[YEAR_IND]:
        return False
    elif date[YEAR_IND] > death[YEAR_IND]:
        return True
    else:
        # Check month:
        if date[MONTH_IND] > death[MONTH_IND]:
            return True
        elif date[MONTH_IND] < death[MONTH_IND]:
            return False
        else:
            # Check day:
            return date[DAY_IND] >= death[DAY_IND]

# Input: A family ID as a string, a list of family objects/dictionaries, and a list of individual objects/dictionaries
# Output: returns the death dates of both parents in a given family


def getParentsDeathDates(familyID, families, people):
    for family in families:
        if family["ID"] == familyID:
            return [GetDeathFromId(people, family['husband_id']), GetDeathFromId(people, family['wife_id'])]


# Input: The death date of a husband of a family in tuple format, and the birthday of a child in tuple format
# Output: Returns True if the husband died at least nine months before the birth of a child or after, and false otherwise
def HusToChild(hus, child):
    if child[YEAR_IND] - hus[YEAR_IND] == 1:
        if (child[MONTH_IND] + 12) - hus[MONTH_IND] >= 9:
            return False

    if child[YEAR_IND] - hus[YEAR_IND] > 1:
        return False
    elif hus[YEAR_IND] > child[YEAR_IND]:
        return True
    else:
        # Check month:
        if hus[MONTH_IND] > child[MONTH_IND]:
            return True
        elif hus[MONTH_IND] < child[MONTH_IND] and (abs(hus[MONTH_IND] - child[MONTH_IND]) >= 9):
            return False
        else:
            return True


# User Story #1 -- Eric
# Input: A person object/dictionary
# Output: Returns true if every date [birth, death, marriage, divorce] occurs before death on an individual. False otherwise.
# Note: If alive, assume death is negligible. Death, marriage, divorce could be N/A. Will true in this case.
def datesBeforeToday(personObj, families):
    todayTuple = getTodayDateTuple()
    birthdayTuple = convertDateStrToDateTuple(personObj['birthday'])
    if personObj['alive'] == False:
        deathdayTuple = convertDateStrToDateTuple(personObj['death'])
    familyList = getFamilesFromPerson(personObj, families)
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

    if len(familyList) == 0:  # single, never married
        return True
    else:
        for fam_id in familyList:
            if fam_id["divorced"] == "NA":  # just check marriage date
                marriagedayTuple = convertDateStrToDateTuple(fam_id['married'])
                if marriagedayTuple[YEAR_IND] == todayTuple[YEAR_IND]:
                    # marriage month after current month
                    if marriagedayTuple[MONTH_IND] > todayTuple[MONTH_IND]:
                        return False
                    # marriage month after current month
                    elif marriagedayTuple[MONTH_IND] == todayTuple[MONTH_IND]:
                        # marriage day after current day
                        if marriagedayTuple[DAY_IND] > todayTuple[DAY_IND]:
                            return False
                return True
            else:
                marriagedayTuple = convertDateStrToDateTuple(fam_id['married'])
                if marriagedayTuple[YEAR_IND] > todayTuple[YEAR_IND]:
                    return False
                if marriagedayTuple[YEAR_IND] == todayTuple[YEAR_IND]:
                    # divorce month after current month
                    if marriagedayTuple[MONTH_IND] > todayTuple[MONTH_IND]:
                        return False
                    # divorce month after current month
                    elif marriagedayTuple[MONTH_IND] == todayTuple[MONTH_IND]:
                        # divorce day after current day
                        if marriagedayTuple[DAY_IND] > todayTuple[DAY_IND]:
                            return False
                divorcedayTuple = convertDateStrToDateTuple(fam_id['divorced'])
                if divorcedayTuple[YEAR_IND] > todayTuple[YEAR_IND]:
                    return False
                if divorcedayTuple[YEAR_IND] == todayTuple[YEAR_IND]:
                    # divorce month after current month
                    if divorcedayTuple[MONTH_IND] > todayTuple[MONTH_IND]:
                        return False
                    # divorce month after current month
                    elif divorcedayTuple[MONTH_IND] == todayTuple[MONTH_IND]:
                        # divorce day after current day
                        if divorcedayTuple[DAY_IND] > todayTuple[DAY_IND]:
                            return False
    return True

# User Story #2 -- Jan, Ankit, Eric (PAIR PROGRAMMING)
# Input: a person object/dictionary and a list of family objects
# Output: true if they were born before marriage, false otherwise
# Error
# Refactoredj by Ankit for Sprint 2


def birthBeforeMarriage(personObj, families):
    spouseList = personObj['spouse']

    if len(spouseList) == 0:
        return True

    birthdayTuple = convertDateStrToDateTuple(personObj['birthday'])

    return reduce(lambda x, y: x and y, map(lambda spouse: timeBetweenDatesSigned(birthdayTuple, convertDateStrToDateTuple(getFamilyFromId(spouse, families)['married'])) > 0, spouseList))

# User Story #3 -- Ankit
# Input: A person object/dictionary
# Output: Returns true if birth occurs before death on an individual. False otherwise. False should be logged as an error.
# Note: Returns true if person is not dead.
# Question: Can someone die on the same day they were born? This function assumes thats allowed
# Refactored by Ankit for Sprint 2


def birthBeforeDeath(personObj):
    if personObj['alive']:
        return True
    else:

        birthdayTuple = convertDateStrToDateTuple(personObj['birthday'])
        deathdayTuple = convertDateStrToDateTuple(personObj['death'])

        num_days_alive = timeBetweenDatesSigned(birthdayTuple, deathdayTuple)

        if num_days_alive >= 0:
            return True
        return False


# User Story #5 -- Zane
# Input: A Family object/dictionary, a list of individual objects/dictionaries
# Output: Return true if marriage occurs before death, and false if otherwise
def MarriageBeforeDeath(familyObj, people):
    marriedTuple = convertDateStrToDateTuple(familyObj['married'])
    hus_death = GetDeathFromId(people, familyObj['husband_id'])
    wife_death = GetDeathFromId(people, familyObj['wife_id'])
    ans, ans2 = True, True

    if not hus_death == 'NA':
        husbandTuple = convertDateStrToDateTuple(hus_death)
        ans = compareDeath(husbandTuple, marriedTuple)

    if not wife_death == 'NA':
        wifeTuple = convertDateStrToDateTuple(wife_death)
        ans2 = compareDeath(wifeTuple, marriedTuple)
    return ans and ans2


# User Story #4 -- Jan
# Input: a family object
# Output: boolean
# True if marriage occurs before divorce, False if not
# ERROR
def marrBefDiv(familyObj):
    marriageDate = convertDateStrToDateTuple(familyObj['married'])
    if (familyObj['divorced'] == 'NA'):
        return True
    else:
        divorceDate = convertDateStrToDateTuple(familyObj['divorced'])
        if (divorceDate[YEAR_IND] < marriageDate[YEAR_IND]):
            return False
        elif (divorceDate[YEAR_IND] > marriageDate[YEAR_IND]):
            return True
        else:
            # Check month:
            if (divorceDate[MONTH_IND] < marriageDate[MONTH_IND]):
                return False
            elif (divorceDate[MONTH_IND] > marriageDate[MONTH_IND]):
                return True
            else:
                # Check day
                return divorceDate[DAY_IND] >= marriageDate[DAY_IND]


# User Story #6 -- Faraz
# Input: a person object/dictionary and a family object/dictionary
# Output: True or False if death before divorce.
def deathBeforeDivorce(personObj, family):
    if (family['divorced'] == 'NA'):
        return True
    divorceTuple = convertDateStrToDateTuple(family['divorced'])

    if (personObj['alive'] == True):
        return True
    deathDate = convertDateStrToDateTuple(personObj['death'])
    if ((deathDate[YEAR_IND] < divorceTuple[YEAR_IND]) or ((deathDate[YEAR_IND] == divorceTuple[YEAR_IND]) and (deathDate[MONTH_IND] < divorceTuple[MONTH_IND])) or ((deathDate[YEAR_IND] == divorceTuple[YEAR_IND]) and (deathDate[MONTH_IND] == divorceTuple[MONTH_IND]) and (deathDate[DAY_IND] < divorceTuple[DAY_IND]))):
        return False
    return True

# User Story #7 -- Eric
# Input: a person object
# Output: boolean
# True [if death is less than 150 years after birth] and current date is less than 150 years after birth for living peopel, False otherwise
# This assumes a standard 4-year leap year schedule. 150 years includes 37 leap years and 113 regular years. 54787 days = 150 years.
# Also assumes that AD year started at 1. Year 0 will error.


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


# User Story #8 -- Jan
# Input: a person object
# Output: True if person is born after marriage OR at most 9 months after divorce, False if not
# 9 months = 273.75 days, rounded up to 274
# ANOMALY
def bornBefMarr(personObj, families):
    birthDate = convertDateStrToDateTuple(personObj['birthday'])
    familyList = personObj['child']
    for fam in familyList:
        famObj = getFamilyFromId(fam, families)
        marriageDate = convertDateStrToDateTuple(famObj['married'])
        if (famObj['divorced'] != 'NA'):
            divorceDate = convertDateStrToDateTuple(famObj['divorced'])
            if (birthDate[YEAR_IND] >= divorceDate[YEAR_IND]):
                daysBetweenBirthDiv = timeBetweenDays(birthDate, divorceDate)
                if (daysBetweenBirthDiv > 274):
                    return False
        else:
            if (birthDate[YEAR_IND] < marriageDate[YEAR_IND]):
                return False
            if (birthDate[YEAR_IND] == marriageDate[YEAR_IND]):
                if (birthDate[MONTH_IND] < marriageDate[MONTH_IND]):
                    return False
                if (birthDate[MONTH_IND] == marriageDate[MONTH_IND]):
                    if (birthDate[DAY_IND] < marriageDate[DAY_IND]):
                        return False
    return True


# User Story #9 -- Zane
# Input: A person object, a list of family objects, and a list of people objects
# Output: Return false if mother dies before personObj's birthday or the father dies more than nine months before birthday
# Returns true otherwise
def BirthBeforeParentsDeath(personObj, families, people):
    for famID in personObj['child']:
        arr = getParentsDeathDates(famID, families, people)
        hus_death = arr[0]
        wife_death = arr[1]
        birthdayTuple = convertDateStrToDateTuple(personObj['birthday'])
        ans, ans2 = True, True

        if not hus_death == 'NA':
            husbandTuple = convertDateStrToDateTuple(hus_death)
            ans = HusToChild(husbandTuple, birthdayTuple)

        if not wife_death == 'NA':
            wifeTuple = convertDateStrToDateTuple(wife_death)
            ans2 = compareDeath(wifeTuple, birthdayTuple)
        if not (ans and ans2):
            return False
    return True

# User Story #10 -- Faraz
# Input: a person object/dictionary and a family object/dictionary
# Output: True or False if the person got married before 14.
# Note: DOES modify the input- slightly formats the person object to make date extraction easier for future uses.
# Question: SHould the program accept future dates?


def marriageAfter14(personObj, family):
    marriedTuple = convertDateStrToDateTuple(family['married'])
    birthTuple = convertDateStrToDateTuple(personObj['birthday'])
    days = timeBetweenDays(marriedTuple, birthTuple)
    if (days >= 5113):
        return True
    return False

# User Story #12 -- Eric
# Input: a person object/dictionary and a family object/dictionary
# Output: True if mother < 60yrs old of child ^ father < 80yrs old of child


def parentsNotTooOld(familyObj, individuals):
    children = familyObj['children']
    childrenAge = []
    for x in children:
        childrenAge.append(computeAgeHelper(getPersonFromId(x, individuals)))
    dadAge = computeAgeHelper(getPersonFromId(
        familyObj['husband_id'], individuals))
    momAge = computeAgeHelper(getPersonFromId(
        familyObj['wife_id'], individuals))
    for x in childrenAge:
        if (dadAge-x > 80 or momAge-x > 60):
            return False
    return True

# User Story #16 -- Ankit
# Purpose: Checks if all male members of a family have the same last name.
# Input: a family object/dictionary, and the list of people
# Output: returns a SET of unique last names possessed by the male members of a family.
#           If every male familymember has the same surname, then the size of the set is 1.
# ANOMOLY


def maleLastNames(family, people):
    lastNameToMatch = family['husband_name'].split()[1]  # get family name
    lastNamesSet = {lastNameToMatch}

    # Filter for male family members
    maleMembers = list(
        filter(lambda p: p['ID'] in family['children'] and p['gender'] == 'M', people))

    # Cast to set to remove duplicates
    retval = set(map(lambda p: lastNamesSet.add(
        p['name'].split()[1]), maleMembers))

    return lastNamesSet

# User Story #17 -- Ankit
# Purpose: Checks if a person married any of their descendants.
# Input: a person object, a list of families, and a list of people
# Output: returns empty set if parent married any of their descendants, otherwise returns a set of descendants they are married to.
# Note: A descendant is defined as anyone born in a direct biological OR adoptive line. Eg: A daughter is a descendant, but daughter in law isn't. Step-children are considered descendants as well.
# ANOMOLY


def marriedToDescendants(personObj, families, people):
    # Get all descendants of the person - set of string IDs
    descendants = set(getDescendants(personObj, families, people))

    # Get everyone the person is/was married to - set of Family IDs
    marriedTo = set(getSpouses(personObj, families))

    both = marriedTo.intersection(descendants)
    return both

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


# user story 29 -- Zane
# Input: A list odf all individuals from a gedcom file
# Output: All individuals who are labeled as deceased
def deceased(individuals):
    arr = []
    for indi in individuals:
        if not indi['alive']:
            arr.append(indi)
    return arr


# user story 30 -- Zane and Faraz (PAIR PROGRAMMING)
# Input: A list of all individuals from a gedcom file
# Output: a list of individuals who are living and married
def livingMarried(individuals, families):
    arr = []
    for indi in individuals:
        if len(indi['spouse']) > 0:
            fam = FamilybyID(families, id)
            for id in indi['spouse']:
                if indi['alive'] == True and fam['divorced'] == 'NA':
                    arr.append(indi)
                    break
    return arr
# user story 31 -- Faraz (PAIR PROGRAMMING)
# Input: A list of all individuals from a gedcom file
# Output: a list of individuals who are living single over 30


def livingSingle(individuals):
    arr = []
    for indi in individuals:
        if len(indi['spouse']) == 0:
            birthday = convertDateStrToDateTuple(indi['birthday'])
            today = getTodayDateTuple()
            ageInDays = timeBetweenDays(birthday, today)
            if indi['alive'] == True and ageInDays > 10958:
                arr.append(indi)
    return arr

# User Story #15 -- Jan
# Input: a family object
# Output: True if family has less than 15 siblings, False otherwise
# ANOMALY


def lessThan15Siblings(familyObj):
    numSiblings = len(familyObj['children'])
    if (numSiblings < 15):
        return True
    return False
