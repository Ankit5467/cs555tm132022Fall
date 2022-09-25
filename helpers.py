# Define helper functions here (Eg: Data transformation, formulas, etc.)

# Input: list of dictionary object
# Output: list of lists, where each inner list corresponds to the values of a dictionary object.
# Note: Doesnt modify the input
def listOfDicts_to_nestedList(listOfDicts):
    return list(map(lambda x: list(x.values()), listOfDicts))