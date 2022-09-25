# Define feature functions (user story functions) and variables in this file:

from datetime import date, datetime
 
# familes = []
# individuals = []

# Input: an id string and a list of individuals (list of dictionaries w/ each dictionary representing a person)
# Output: The name of the person corresponding to the inputted id OR an error message.
# Note: Does NOT modify the input.
def getNameFromId(id, people):    
    for indi in people:
        if indi['ID'] == id:
            return indi['name']
    return 'Error: Id does not exist!'


# User Story #27 -- Ankit
# Input: a person object/dictionary
# Output: Computes the age of the person
# Note: DOES modify the input- slightly formats the person object to make date extraction easier for future uses.
def computeAge(person):       
    bdayLen = len(person['birthday'].split(' ')[0])
    if bdayLen == 1:
        person['birthday'] = '0' + person['birthday'] 

    birthday_datetime_obj = datetime.strptime(person['birthday'], '%d %b %Y')
    
    end = ''
    
    if person['death'] == 'NA':
        end = date.today()
    else:
        ddayLen = len(person['death'].split(' ')[0])
        if ddayLen == 1:
            person['death'] = '0' + person['death']
        
        end = datetime.strptime(person['death'], '%d %b %Y')
         
    age = end.year - birthday_datetime_obj.year - ((end.month, end.day) < (birthday_datetime_obj.month, birthday_datetime_obj.day))
    return age
        