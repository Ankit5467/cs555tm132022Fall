# Ankit Patel, Zane ThummBorst, ___, ____, ____
# CS 555 Agile | Group __
# Gedcom file parser
# I pledge my honor that I have abided by the Stevens Honor System.


# Pre-requisites: This program requires the gedcomParser library. Install it via:
# $pip install python-gedcom
# $pip install -U prettytable

# Usage: $Python3 gedcom_parser.py

# This script accepts a gedcom file as an input *while* it is executed.
# ie: Once the command above is entered, the program will prompt the user for a gedcom file name as an input.
# Output is written to output.txt.

# Make sure the gedcom file as the following line as its last line, otherwise this program will NOT work!
# '0 TRLR'

# from gedcom.element.individual import IndividualElement
# from gedcom.element.object import ObjectElement
# from gedcom.element.element import Element
from gedcom.parser import Parser

# Import pretttable
from prettytable import PrettyTable

# Import custom helper functions
from helpers import listOfDictsToNestedList

# Import custom operations
from operations import *

# Prompt the user for an input
input_file_name = input("Enter the gedcom file you would like to analyze: ")

# case 1: filename -> Append file '.ged' extension
# case 2: filename.ged -> No need to do anything extra
if ".ged" not in input_file_name:
    input_file_name += ".ged"

file_path = './' + input_file_name

# valid tags for the common case, along w/ their accepted level (ie: INDI & FAM not included)
valid_common_tags = [
    ['HEAD', 'TRLR', 'NOTE'],  # valid lvl 0 tags
    ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS',
     'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'],  # valid lvl 1 tags
    ['DATE']  # valid lvl 2 tags
]

mappings = {
    'BIRT': 'birthday',
    'DEAT': 'death',
    'MARR': 'married',
    'DIV': 'divorced',
    'NAME': 'name',
    'SEX': 'gender',
    'FAMS': 'spouse',
    'FAMC': 'child'
}

#  Initialize the parser
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path, False)  # disable strict parsing

child_elems = gedcom_parser.get_element_list()
print("Reading File: " + input_file_name)

# date string format: "[Day number] [Month abreviation] [birth year]"
# ComputeAge() pads day number w/ a 0 if day number > 9.

individuals = []  # list of dicts. Each elem represents info for an individual.
# {
#   ID: string
#   name: string
#   gender: string: 'M' or 'F'
#   birthday: string: date
#   age: int
#   alive: boolean: True or False
#   death: string: "NA" or date
#   child: List of strings ids. Each id represents a family that this individual is child of.
#   spouse: List of strings ids. Each id represents a family that is individual is a spouse of.
# }

families = []  # list of dicts.
# {
#   ID: string
#   married: string: date
#   divorced: string: 'NA' or date
#   husband_id: id
#   husband_name: string
#   wife_id: id
#   wife_name: string
#   children: list of string IDs
# }

# Tags for which there must be a date right afterwards
date_tags = ['BIRT', 'DEAT', 'MARR', 'DIV']

cur_obj = {}
cur_obj_type = ''  # Either 'INDI' or 'FAM'
# Tracks whether the next date string will be for a 'BIRT' or DEAT' or 'MARR' or 'DIV' tag
cur_obj_date_info = ''

# Create/open the output file:
f = open("output.txt", "w")

# Iterate through elems:
for elem in child_elems:
    try:

        orig_line = elem.to_gedcom_string().strip()
        f.write('--> ' + orig_line + '\n')
        parser_str = ""

        # Now, print: "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
        lvl = elem.get_level()  # int
        tag = elem.get_tag().strip()  # string
        # print(tag)

        uncommon_case = orig_line.endswith('INDI') or orig_line.endswith('FAM')

        if uncommon_case:
            # print("uncommon case ")
            # update tag
            tag = 'INDI' if orig_line.endswith('INDI') else 'FAM'
            valid = 'Y' if (lvl == 0) else 'N'

            # For the uncommon case, args is the id, ie: everything b/w the level and tag.
            args = orig_line.split(str(lvl), 1)[1].split(tag, 1)[0]
        else:
            valid = 'Y' if ((lvl >= 0 and lvl <= 2)
                            and tag in valid_common_tags[lvl]) else 'N'

            # args parameter is everything after the tag
            args = orig_line.split(tag, 1)
            if len(args) == 1:
                args = "NO ARGS"
            else:
                args = args[1]

        parser_str = "{l}|{t}|{v}|{a}".format(
            l=lvl, t=tag, v=valid, a=args.strip())

        # print('<-- ' + parser_str)
        f.write('<-- ' + parser_str + '\n')

        # Extract info into dict obj
        if valid:
            # parsed line represents start of new individual/family
            if (lvl == 0 and (tag == 'INDI' or tag == 'FAM')):

                # add obj to global dict
                if cur_obj_type == 'INDI':
                    individuals.append(cur_obj)
                elif cur_obj_type == 'FAM':
                    families.append(cur_obj)

                cur_obj = {}        # "reset" the current object
                cur_obj_type = tag  # update tag

                cur_obj['ID'] = args.strip()    # set item id

                # set default values
                if cur_obj_type == 'INDI':
                    cur_obj['name'] = 'name not parsed'
                    cur_obj['gender'] = 'gender not parsed'
                    cur_obj['birthday'] = 'Birthday not parsed'
                    cur_obj['age'] = -1
                    cur_obj['alive'] = True
                    cur_obj['death'] = 'NA'
                    cur_obj['child'] = []
                    cur_obj['spouse'] = []

                else:
                    cur_obj['married'] = 'marriage date not parsed'
                    cur_obj['divorced'] = 'NA'
                    cur_obj['husband_id'] = 'husband id not parsed'
                    cur_obj['husband_name'] = 'husband name not set'
                    cur_obj['wife_id'] = 'wife id not parsed'
                    cur_obj['wife_name'] = 'wife name not set'
                    cur_obj['children'] = []

            elif lvl == 1 or lvl == 2:  # parsed line represents part of an individual/family
                if lvl == 1:
                    if tag in date_tags:  # See if next attribute is a date. Takes care of the following tags: BIRT, DEAT, MARR, DIV
                        cur_obj_date_info = tag

                        # Update 'alive' attribute if neccessary
                        if tag == 'DEAT':
                            cur_obj['alive'] = False
                        continue

                    if cur_obj_type == 'INDI':
                        # Take care of the following tags: NAME, SEX, FAMS, FAMC
                        if tag == 'NAME':
                            cur_obj['name'] = args.strip()
                        elif tag == 'SEX':
                            cur_obj['gender'] = args.strip()
                        elif tag == 'FAMS':
                            cur_obj['spouse'].append(args.strip())
                        elif tag == 'FAMC':
                            cur_obj['child'].append(args.strip())
                        else:
                            print("Parsing Error: Unexpected tag: " + tag + ".")

                    elif cur_obj_type == 'FAM':
                        # Take care of the following tags: HUSB, WIFE, CHIL
                        if tag == 'HUSB':
                            cur_obj['husband_id'] = args.strip()
                        elif tag == 'WIFE':
                            cur_obj['wife_id'] = args.strip()
                        elif tag == 'CHIL':
                            cur_obj['children'].append(args.strip())
                        else:
                            print("Parsing Error: Unexpected tag: " + tag + ".")

                    else:
                        print("Parsing Error!!!")

                elif lvl == 2:  # Extract the date
                    cur_obj[mappings[cur_obj_date_info]] = args.strip()
                    cur_obj_date_info = ''

            elif lvl == 0 and tag == 'TRLR':  # end of gedcom file
                # add obj to global dict
                if cur_obj_type == 'INDI':
                    individuals.append(cur_obj)
                elif cur_obj_type == 'FAM':
                    families.append(cur_obj)

                cur_obj = {}        # "reset" the current object

        # reset variables and parse next line:
        valid = ''
        args = ''

    except:
        print("Unable to parse line")
        f.write("Unable to parse line\n")
f.close()

print("Finished analyzing file: " + input_file_name)
print("\n")

# Analyze Individuals & Families

# Compute ages
for indiv in individuals:
    indiv['age'] = computeAge(indiv)

# Update names in 'families' table
for family in families:
    family['husband_name'] = getNameFromId(family['husband_id'], individuals)
    family['wife_name'] = getNameFromId(family['wife_id'], individuals)

# Set up and display the individuals and familes tables
individualsTable = PrettyTable()
individualsTable.field_names = ['ID', 'name', 'gender', 'birthday',
                                'age', 'alive', 'death', 'child of families', 'spouse of families']
individualsTable.add_rows(listOfDictsToNestedList(individuals))
print("Individuals:")
print(individualsTable)
print("\n")

familiesTable = PrettyTable()
familiesTable.field_names = ['ID', 'married', 'divorced',
                             'husband_id', 'husband_name', 'wife_id', 'wife_name', 'children']
familiesTable.add_rows(listOfDictsToNestedList(families))
print("Families:")
print(familiesTable)
print("\n")

individualsTable = PrettyTable()
individualsTable.field_names = ['ID', 'name', 'gender', 'birthday',
                                'age', 'alive', 'death', 'child of families', 'spouse of families']
individualsTable.add_rows(listOfDictsToNestedList(deceased(individuals)))
print("Deceased:")
print(individualsTable)
print("\n")


# Print out the Errors and anomolies for each user story:

for person in individuals:

    # User Story 1 -- ERROR HERE
    if not datesBeforeToday(person, families):
        print("Error: INDIVIDUAL: US01: " +
              person['ID'] + ": A date occurs after today")

    # User Story 2
    if not birthBeforeMarriage(person, families):
        print("Error: INDIVIDUAL: US02: " +
              person['ID'] + ": was married before they were born.")

    # User Story 3
    if not birthBeforeDeath(person):
        print("Error: INDIVIDUAL: US03: " +
              person['ID'] + ": Death date occurs before birth!")

    # User Story 7
    if not lessThan150(person):
        print("Error: INDIVIDUAL: US07: " +
              person['ID'] + ": More than 150 years old at death!. Birth: " + person['birthday'] + ". Death: " + person['death'])

    # User Story 8
    if not bornBefMarr(person, families):
        print("Anomaly: INDIVIDUAL: US08: " + person['ID'] + ": Child " + person['ID'] +
              " was born before marriage of parents or more than 9 months after divorce.")

    # User Story 9
    if not BirthBeforeParentsDeath(person, families, individuals):
        print("Error: INDIVIDUAL: US09: " +
              person['ID'] + ": Birth occurs after death of parents.")

    # User Story 17
    marriedDescendants = marriedToDescendants(person, families, individuals)
    if len(marriedDescendants) > 0:
        print("Anomaly: INDIVIDUAL: US17: " +
              person['ID'] + ": is married to their descendant(s): " + str(marriedDescendants))

for family in families:

    person1 = getPersonFromId(family["husband_id"], individuals)
    person2 = getPersonFromId(family["wife_id"], individuals)

    # User Story 4
    if not marrBefDiv(family):
        # User Story 4
        print("Error: FAMILY: US04: " + family['ID'] + " Marriage on " +
              family['married'] + " occurs after divorce on " + family['divorced'] + ".")

    # User Story 5
    if not MarriageBeforeDeath(family, individuals):
        # Enter dates here
        print("Error: FAMILY: US05: " +
              family['ID'] + " Marriage occurs after after death.")

    # User Story 6
    if not deathBeforeDivorce(person1, family):
        print("Error: INDIVIDUAL: US06: " +
              person1['ID'] + " Divorce occurs after after death.")  # Enter dates here
    if not deathBeforeDivorce(person2, family):
        print("Error: INDIVIDUAL: US06: " +
              person2['ID'] + " Divorce occurs after after death.")  # Enter dates here

    # User Story 10
    if not marriageAfter14(person1, family):
        print("Anomaly: INDIVIDUAL: US10: " +
              person1['ID'] + " Marriage occurs before 14.")  # Enter more info here
    if not marriageAfter14(person2, family):
        print("Anomaly: INDIVIDUAL: US10: " +
              person2['ID'] + " Marriage occurs before 14.")  # Enter more info here

    # User Story 12
    if not parentsNotTooOld(family, individuals):
        print("Anomaly: FAMILY: US10: " +
              family['ID'] + " Parents too old.")

    # User Story 13
    if not siblingsSpacing(family, individuals):
        print("Anomaly: FAMILY: US10: " +
              family['ID'] + " Siblings spacing is abnormal")

    #User Story 14
    if not multipleBirths(family, individuals):
        print("Anomaly: FAMILY: US14: " +
              family['ID'] + " Multiple Births.")

    #User Story 15
    if not lessThan15Siblings(family):
        print("Anomaly: FAMILY: US:15 " + 
                family['ID'] + " has 15 or more siblings.")

    # User Story 16
    family_names = maleLastNames(family, individuals)
    if len(family_names) > 1:
        print("Anomaly: FAMILY: US16: Male members of family " +
              family['ID'] + " have multiple surnames: " + str(family_names))
        
    # User Story 25
    if not checkUniqueFirstNames(family, individuals):
        print("Anomaly: FAMILY: US25: A pair of twins in Family " + family['ID'] + " has identical names!")
        
    # WHAT USER STORY IS THIS?
    if not multipleBirths(family, individuals):
         print("Anomoly: FAMILY: US14: " +
              family['ID'] + " Multiple Births.")



# User Story 24
if not uniqueFamBySpouse(families):
    print("Error: US24: All families must be unique by spouses and marriage dates!")
if not CorrespondingEntries(families, individuals):
    print("Error: US28: All entries between individuals and families (spouses, husband, wife, children, etc) must be consistent!")
#User Story 28
print("\n")
print("Order siblings by each family")
for family in families:
    print(orderSibling(family,individuals))
# User Story 30
print("\n")
print("Living Single List (US 30): ")    
print(livingSingle(individuals))

# User Story 31
print("\n")
print("Living Married List (US 31): ")
print(livingMarried(individuals))
# User Story 32
print("\n")
print("Multiple Birth")
print(multipleBirthList(families))

# User Story 34
print("\n")
print("List of couples with large age gaps at time of marriage (Anomaly): ")
list_large_age_gaps = listLargeAgeDifferences(families, individuals)
print("No large age gaps!" if list_large_age_gaps == [] else list_large_age_gaps )


print("")
