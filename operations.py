# Define feature functions (user story functions) and variables in this file:

from datetime import date, datetime

# Import helper functions
from helpers import convertDateStrToDateTuple

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


# User Story #2 -- Ankit
# Input: A person object/dictionary
# Output: Returns true if birth occurs before death on an individual. False otherwise.
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
    

# User Story #27 -- Ankit
# Input: a person object/dictionary
# Output: Computes the age of the person
# Note: DOES modify the input- slightly formats the person object to make date extraction easier for future uses.
# Question: SHould the program accept future dates?
def computeAge(personObj):       
    bdayLen = len(personObj['birthday'].split(' ')[0])
    if bdayLen == 1:
        personObj['birthday'] = '0' + personObj['birthday'] 

    birthday_datetime_obj = datetime.strptime(personObj['birthday'], '%d %b %Y')
    
    end = ''
    
    if personObj['death'] == 'NA':
        end = date.today()
    else:
        ddayLen = len(personObj['death'].split(' ')[0])
        if ddayLen == 1:
            personObj['death'] = '0' + personObj['death']
        end = datetime.strptime(personObj['death'], '%d %b %Y')
         
    age = end.year - birthday_datetime_obj.year - ((end.month, end.day) < (birthday_datetime_obj.month, birthday_datetime_obj.day))
    return age
        