# Define feature functions (user story functions) in this file:

from datetime import date, datetime
from functools import reduce
from operator import truediv
from tkinter.font import families
import itertools
from webbrowser import get

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

# Input: list of family objects and a id in string format
# Output: the family object the corresponds to the string id


def FamilybyID(families, id):
    for fam in families:
        if fam['ID'] == id:
            return fam

# Input: list of family objects and a id in string format
# Output: the family object the corresponds to the string id


def PersonbyID(people, id):
    for person in people:
        if person['ID'] == id:
            return person

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
# refactor: use personbyID instead and simplified return conditions
def MarriageBeforeDeath(familyObj, people):
    marriedTuple = convertDateStrToDateTuple(familyObj['married'])
    hus_death, wife_death = (PersonbyID(people, familyObj['husband_id']))[
        'death'],  (PersonbyID(people, familyObj['wife_id']))['death']

    if not hus_death == 'NA':
        husbandTuple = convertDateStrToDateTuple(hus_death)
        if not compareDeath(husbandTuple, marriedTuple):
            return False

    if not wife_death == 'NA':
        wifeTuple = convertDateStrToDateTuple(wife_death)
        if not compareDeath(wifeTuple, marriedTuple):
            return False
    return True


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

# User Story #13 -- Eric
# Input: a family object
# Output: True if Birth dates of siblings should be more than 8 months apart or less than 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
# ANOMALY
# NOTE: assumes 8 months = 243 days


def siblingsSpacing(familyObj, individuals):
    numSiblings = len(familyObj['children'])
    if (numSiblings <= 1):  # no children or 1 child
        return True
    else:
        children = familyObj['children']
        childrenAgeNumber = []
        for x in children:
            child = getPersonFromId(x, individuals)
            childrenAgeNumber.append(timeBetweenDays(
                convertDateStrToDateTuple(child['birthday']), getTodayDateTuple()))
        for x, y in itertools.combinations(childrenAgeNumber, 2):
            if (2 < abs(x-y) < 243):
                return False
    return True


# User Story #15 -- Jan
# Input: a family object
# Output: True if family has less than 15 siblings, False otherwise
# ANOMALY


def lessThan15Siblings(familyObj):
    numSiblings = len(familyObj['children'])
    if (numSiblings < 15):
        return True
    return False

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

# User Story #18 -- Zane
# input: family object/ dictionary and list of individual objects/dictionaries
# output: True if sibilings are not married to one another, false if otherwise


def siblingsMarriage(family, individuals):
    h = PersonbyID(individuals, family["husband_id"])
    w = PersonbyID(individuals, family['wife_id'])

    for fam1 in h['child']:
        for fam2 in w['child']:
            if fam1 == fam2:
                return False
    return True
# User Story #19 -- Faraz
# input: family object/ dictionary and list of individual objects/dictionaries
# output: True if sibilings are not married to one another, false if otherwise
# possible bug is if they cannot find the parent 
def firstCousinsShouldNotMarry(family, familyList):
    husbendId = family['husband_id']
    wifeId = family['wife_id']
    relative = 0
    husbandParentsFamily={}
    wifeParentsFamily= {}
    husbandGrandParents2 = {}
    husbandGrandparents1 = {}
    for familyMembers  in familyList:
        
        if husbendId in familyMembers['children']:
            husbandParentsFamily = familyMembers
            
        elif wifeId in familyMembers['children']:
            wifeParentsFamily = familyMembers
    if husbandParentsFamily=={} or wifeId=={}:
        return True
    for familyMembers in familyList:
        if husbandParentsFamily['husband_id'] in familyMembers['children']:
            husbandGrandparents1 = familyMembers
        elif husbandParentsFamily['wife_id'] in familyMembers['children']:
            husbandGrandParents2 = familyMembers
    if husbandGrandparents1 == {}:
        return True
    if (wifeParentsFamily['husband_id'] in husbandGrandparents1['children']) or (wifeParentsFamily['wife_id'] in husbandGrandparents1['children']):
        return False
    if husbandGrandparents2 == {}:
        return True
    if (wifeParentsFamily['husband_id'] in husbandGrandparents2['children']) or (wifeParentsFamily['wife_id'] in husbandGrandparents2['children']):
        return False
    else:
        return True
    
# User Story #20 -- Faraz
# input: family object/ dictionary and list of individual objects/dictionaries
# output: True if sibilings are not married to one another, false if otherwise
def auntieHelper(Uncle,Niece,familyList):
    nieceParentsFamily ={}
    uncleParentsFamily = {}
    for familyMembers  in familyList:
        if Niece in familyMembers['children']:
            nieceParentsFamily = familyMembers
        elif Uncle in familyMembers['children']:
            uncleParentsFamily = familyMembers
    if(nieceParentsFamily=={}) or(uncleParentsFamily=={}):
        return True
    if (nieceParentsFamily["husband_id"] in uncleParentsFamily['children']) or (nieceParentsFamily["wife_id"] in uncleParentsFamily['children']):
        return False
    else:
        return True
def auntandUncleNoNephew(family, familyList):
    result1 = auntieHelper(family['husband_id'],family['wife_id'], familyList)
    result2 = auntieHelper(family['wife_id'],family['husband_id'],familyList)
    if(result1==False) or (result2==False):
        return False
    else: 
        return True





# User Story # 24 -- Zane
# Input: a family objecy/dictionary
# Description: a Family husband name, wife name, and marriage date should be unique to each family object
# if there are multiple entries with the same name and date combos, return false. Otherwise, return true


def uniqueFamBySpouse(families):
    n = {}
    for family in families:
        entry = str([family['husband_name'],
                    family['wife_name'], family['married']])
        if entry in n:
            return False
        else:
            n[entry] = True
    return True


# User Story #25 -- Ankit
# Input: a family object/dictionary and the people list
# Description: No more than one child with the same name and birth date should appear in a family.
# Output: returns True if every pair of twins in a family has a unique name or if there are no twins in a family. Returns False otherwise (ie twins have same names).
# Anomaly
def checkUniqueFirstNames(family, people):

    # get children objs of given family
    children = list(map(lambda child: getPersonFromId(
        child, people), family['children']))

    if len(children) == 1:
        return True

    # Test every child pair
    for i in range(len(children)-1):
        for j in range(i+1, len(children)):
            i_child_bday_tup = convertDateStrToDateTuple(
                children[i]['birthday'])
            j_child_bday_tup = convertDateStrToDateTuple(
                children[j]['birthday'])

            # If birthdays are the same, make sure their names are different
            if timeBetweenDays(i_child_bday_tup, j_child_bday_tup) <= 1 and children[i]['name'] == children[j]['name']:
                return False

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

# User story 28 -- Zane
# Input: list of person objects/dictionaries and list of family objects/dictionaries
# Output: Checks if spouse and child attributes are consistent between individual and family objects


def CorrespondingEntries(families, individuals):
    try:
        for indi in individuals:
            for child_id in indi['child']:
                fam = getFamilyFromId(child_id, families)
                if not (indi['ID'] in fam['children']):
                    return False
            for spouse_id in indi['spouse']:
                fam = getFamilyFromId(spouse_id, families)
                if not (indi['ID'] == fam['wife_id'] or indi['ID'] == fam['husband_id']):
                    return False
        for family in families:
            for child_id in family['children']:
                ind = getPersonFromId(child_id, individuals)
                if not (family['ID'] in ind['child']):
                    return False
            w = getPersonFromId(family['wife_id'], individuals)
            hus = getPersonFromId(family['husband_id'], individuals)
            if not (family['ID'] in w['spouse']):
                return False
            if not (family['ID'] in hus['spouse']):
                return False
        return True
    except:
        return False

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
# ask ankit about married and divorse
def livingMarried(individuals):
    # arr = []
    # for indi in individuals:
    #     if len(indi['spouse']) > 0:
    #         fam = FamilybyID(families, id)
    #         for id in indi['spouse']:
    #             if indi['alive'] == True and fam['divorced'] == 'NA':
    #                 arr.append(indi)
    #                 break
    # return arr
    arr = []
    for indi in individuals:
        if len(indi['spouse']) > 0:
            if indi['alive'] == True:
                arr.append(indi)
    return arr
# user story 31 -- Faraz (PAIR PROGRAMMING)
# Input: A list of all individuals from a gedcom file
# Output: a list of individuals who are living single over 30


def livingSingle(individuals):
    arr = []
    for indi in individuals:
        if len(indi['spouse']) == 0:
            if indi['alive'] == True and indi['age'] >= 30:
                arr.append(indi)
    return arr


def multipleBirths(family, individuals):
    n = {}
    if len(family['children']) <= 5:
        return True
    for id in family['children']:
        pers = PersonbyID(individuals, id)
        date = pers['birthday']
        if date in n:
            n[date] += 1
        else:
            n[date] = 1

    for key in n.keys():
        if n[key] > 5:
            return False
    return True


# User Story #34 -- Ankit
# Input: the families list and peoples list objects
# Description: Lists all couples who were married when the older spouse was more than twice as old as the younger spouse
# Output: returns a list of Family IDs where the marriage occured when there was a large age gap b/w the couple.
# Anomaly
def listLargeAgeDifferences(families, people):

    problematic_age_gaps = []

    for family in families:
        marriageDateTup = convertDateStrToDateTuple(family['married'])
        husbandDOB = convertDateStrToDateTuple(
            getPersonFromId(family['husband_id'], people)['birthday'])
        wifeDOB = convertDateStrToDateTuple(
            getPersonFromId(family['wife_id'], people)['birthday'])
        # time unit is in days, but it doesnt matter
        ageHusbandMarried = timeBetweenDatesSigned(husbandDOB, marriageDateTup)
        ageWifeMarried = timeBetweenDatesSigned(wifeDOB, marriageDateTup)
        if (ageHusbandMarried > 2 * ageWifeMarried) or (ageWifeMarried > 2 * ageHusbandMarried):
            problematic_age_gaps.append(family['ID'])

    return problematic_age_gaps

# User Story #21 -- Jan
# Input: a family object and a list of individuals
# Description: Checks if the husband is male and wife is female
# Output: true if husband = M and wife = F; false otherwise
# Anomaly


def checkFamGender(family, people):
    husband_info = PersonbyID(people, family['husband_id'])
    wife_info = PersonbyID(people, family['wife_id'])
    if (husband_info['gender'] != 'M' or wife_info['gender'] != 'F'):
        return False
    return True


# User Story #22 -- Jan
# Input: a list of objects (could be an individual or family)
# Description: Will check to see if every 'ID' field is unique amongst individuals or families
# Output: true if every ID is unique, false othrwise
# Error
def checkIds(arr):
    idList = []
    for x in arr:
        if len(idList):
            if x['ID'] in idList:
                return False
            else:
                idList.append(x['ID'])
        else:
            idList.append(x['ID'])
    return True

# User Story #32 -- Faraz
# Input: List of all family
# Description: Post list of family who have more than 1 children
# Output: returns a list of families with more than 1 children.


def multipleBirthList(familyList):
    result = []
    for family in familyList:
        if len(family['children']) > 1:
            result.append(family)
    return result
# User Story #28 -- Faraz
# Input: the family obj and all peoples list
# Description: orders the sibling by their age
# Output: returns a sort array of siblings by age


def orderSibling(family, personList):
    result = []
    if len(personList) == 0 or len(family['children']) == 0:
        return result
    for sibling in family['children']:
        person = PersonbyID(personList, sibling)
        result.append(person)
    result.sort(key=lambda x: x['age'], reverse=True)
    return result

# User Story #23 -- Eric
# Input: list of individuals
# Description: Unique name and birth date
# Output: true/false


def uniquePeople(individualsList):
    individualsTuple = []
    for personDuo in individualsList:
        personName = personDuo["name"]
        personBirthday = personDuo["birthday"]
        personTuple = (personName, personBirthday)
        individualsTuple.append(personTuple)
    setTuple = [*set(individualsTuple)]
    if len(individualsTuple) != len(setTuple):
        return False
    return True

# User Story #33 -- Eric
# Input: list of individuals and list of families
# Description: List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
# Output: array of orphans


def listOfOrphans(individualsList, familiesList):
    orphans = []
    for person in individualsList:
        if computeAgeHelper(person) >= 18:
            continue
        else:
            if len(person["child"]) == 0:
                continue
            else:
                for fam in person["child"]:
                    familyObj = getFamilyFromId(fam, familiesList)
                    dadObj = getPersonFromId(
                        familyObj['husband_id'], individualsList)
                    momObj = getPersonFromId(
                        familyObj['wife_id'], individualsList)
                    if (momObj["alive"] or dadObj["alive"]):
                        continue
                    else:
                        orphans.append(person)
    return orphans

# User Story #35 -- Ankit
# Input: the peoples list
# Output: a list of person objects
# Description: Lists all people who were born within the last 30 days.
# Note: Output does not include people born in the future.
# Neither an Anomaly nor error.


def listRecentBirths(people):
    newborns = []

    for person in people:
        bday = convertDateStrToDateTuple(person['birthday'])
        age = timeBetweenDatesSigned(bday, getTodayDateTuple())
        if 0 <= age <= 30:
            newborns.append(person)

    return newborns

# User Story #36 -- Ankit
# Input: the peoples list
# Output: a list of person objects
# Description: Lists all people who died within the last 30 days.
# Note: Output does not include people who die in the future (ie: currently alive people).
# Neither an Anomaly nor error


def listRecentDeaths(people):
    recentlyDead = []

    for person in people:

        if not person['alive']:
            deathdate = convertDateStrToDateTuple(person['death'])
            age = timeBetweenDatesSigned(deathdate, getTodayDateTuple())
            if 0 <= age <= 30:
                recentlyDead.append(person)

    return recentlyDead

# User Story #37 -- Zane
# Input: list of individuals and families
# Output: if an individual has died recently, list any and all spouses and children that are still alive


def recentSurvivor(individuals, families):
    date = dateNDaysAgo(30)
    id_list = []
    for p in individuals:
        if p['alive'] or not p['spouse']:
            continue
        else:
            days = timeBetweenDatesSigned(
                date, convertDateStrToDateTuple(p['death']))
            if days < 30 and days > 0:
                for fam_id in p['spouse']:
                    fam = getFamilyFromId(fam_id, families)
                    id_list.append(fam['husband_id'])
                    id_list.append(fam['wife_id'])
                    for child_id in fam['children']:
                        id_list.append(child_id)
    ppl_list = []
    for id in id_list:
        person = getPersonFromId(id, individuals)
        if person['alive'] == True:
            ppl_list.append(person)

    return ppl_list


# User Story #11 -- Jan
# Input: a person object
# Output: True if person did NOT engage in bigamy, False if they DID
# ANOMALY
def noBigamy(personObj, families):
    familyList = personObj['spouse']
    if (len(familyList) == 1):
        return True
    else:
        for i in range(0, len(familyList) - 1):
            famObj = getFamilyFromId(familyList[i], families)
            if (famObj['divorced'] == 'NA'):
                return False
            else:
                famObj2 = getFamilyFromId(familyList[i+1], families)
                famDiv1 = convertDateStrToDateTuple(famObj['divorced'])
                famMarr2 = convertDateStrToDateTuple(famObj2['married'])
                checkBigamy = timeBetweenDatesSigned(famDiv1, famMarr2)
                if (checkBigamy < 0):
                    return False
    return True


# User Story #39 -- Jan
# Input: a list of family objects and a list of people objects
# Output: List of upcoming anniversaries of LIVING couples (within the next 30 days)
def upcomingAnniversaries(families, people):
    upcomingAnni = []
    for fam in families:
        currFam = fam
        if (currFam['divorced'] == 'NA'):
            husbandInfo = getPersonFromId(currFam['husband_id'], people)
            wifeInfo = getPersonFromId(currFam['wife_id'], people)
            if (husbandInfo['alive'] == True and wifeInfo['alive'] == True):
                marrDate = convertDateStrToDateTuple(currFam['married'])
                currDate = getTodayDateTuple()
                checkGap = timeBetweenDaysNoYear(marrDate, currDate)
                if (checkGap >= 0 and checkGap <= 30):
                    upcomingAnni.append(currFam['ID'])
    return upcomingAnni

# User Story #38 -- Eric
# Input: list of people objects
# Output: List of alive, upcoming birthdays (within the next 30 days)


def upcomingBirthdays(people):
    upcoming = []
    for personObj in people:
        birthday = convertDateStrToDateTuple(personObj['birthday'])
        currDate = getTodayDateTuple()
        checkGap = timeBetweenDaysNoYear(birthday, currDate)
        if (0 <= checkGap <= 30 and personObj['alive']):
            upcoming.append(personObj['ID'])
    return upcoming

# User Story #42 -- Eric
# Input: list f people objects
# Output: returns a list of a pair of person ID and their illegitimate dates


def rejectIllegitimateDates(people, family):
    listOfIllegitimateDates = []
    for personObj in people:
        birthday = convertDateStrToDateTuple(personObj['birthday'])
        if (not isLegitDate(birthday)):
            listOfIllegitimateDates.append((personObj['ID'], "birthday"))
        if (not personObj['alive']):
            deathDate = convertDateStrToDateTuple(personObj['death'])
            if (not isLegitDate(deathDate)):
                listOfIllegitimateDates.append((personObj['ID'], "death day"))
    for famObj in family:
        married = convertDateStrToDateTuple(famObj['married'])
        if (not isLegitDate(married)):
            listOfIllegitimateDates.append((famObj['ID'], "marriage day"))
        if (famObj['divorced'] != 'NA'):
            divorced = convertDateStrToDateTuple(famObj['divorced'])
            if (not isLegitDate(divorced)):
                listOfIllegitimateDates.append((famObj['ID'], "divorce day"))
    return listOfIllegitimateDates
