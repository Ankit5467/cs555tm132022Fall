# Ankit Patel
# CS 555 Agile | Homework 2
# Gedcom file parser
# I pledge my honor that I have abided by the Stevens Honor System.


# Pre-requisites: This program requires the gedcomParser library. Install it via:
# $pip install python-gedcom

# Usage: $Python3 gedcom_parser.py

# This script accepts a gedcom file as an input *while* it is executed. 
# ie: Once the command above is entered, the program will prompt the user for a gedcom file name as an input.
# Output is written to output.txt.

# from gedcom.element.individual import IndividualElement
# from gedcom.element.object import ObjectElement
# from gedcom.element.element import Element
from gedcom.parser import Parser

# Prompt the user for an input
input_file_name = input("Enter the gedcom file you would like to analyze: ")

# case 1: filename -> Append file '.ged' extension
# case 2: filename.ged -> No need to do anything extra
if ".ged" not in input_file_name:   
    input_file_name += ".ged"

file_path = './' + input_file_name

# valid tags for the common case, along w/ their accepted level (ie: INDI & FAM not included)
valid_common_tags = [
    ['HEAD', 'TRLR', 'NOTE'], #valid lvl 0 tags
    ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 
     'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'], #valid lvl 1 tags
    ['DATE'] #valid lvl 2 tags
]

#  Initialize the parser
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path, False) #disable strict parsing

child_elems = gedcom_parser.get_element_list()
print("Reading File: " + input_file_name)

# Create/open the output file:
f= open("output.txt","w")

# Iterate through elems:
for elem in child_elems:
    try:
           
        orig_line = elem.to_gedcom_string().strip()
        # print('--> ' + orig_line)
        f.write('--> ' + orig_line + '\n')
        parser_str = ""
        
        # Now, print: "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
        
        lvl = elem.get_level() #int
        
        tag = elem.get_tag().strip() #string
        # print(tag)

        uncommon_case = orig_line.endswith('INDI') or orig_line.endswith('FAM')
        
        if uncommon_case:
            # print("uncommon case ")
            # update tag
            tag = 'INDI' if orig_line.endswith('INDI') else 'FAM'
            valid = 'Y' if (lvl==0) else 'N'
            
            # args is everything b/w the level and tag.
            args = orig_line.split(str(lvl),1)[1].split(tag,1)[0]
        else:
            valid = 'Y' if ((lvl >= 0 and lvl <= 2) and tag in valid_common_tags[lvl]) else 'N'
            
            args = orig_line.split(tag, 1) # args parameter is everything after the tag
            if len(args) == 1:
                args = "NO ARGS"
            else:
                args = args[1]
            
        parser_str = "{l}|{t}|{v}|{a}".format(l = lvl, t = tag, v = valid, a = args.strip())
        
        # print('<-- ' + parser_str)
        f.write('<-- ' + parser_str + '\n')
        
    except:
            print("Unable to parse line")
            f.write("Unable to parse line\n")

print("Finished analyzing file: " + input_file_name)
f.close()