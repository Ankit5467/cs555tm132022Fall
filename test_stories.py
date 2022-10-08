import unittest
from operations import *

# Command to run script:
# $Python3 test_stories.py

# TESTS GO HERE


class testStories(unittest.TestCase):
    def test_user_story_1(self):

        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        person2 = {'ID': 'I1', 'name': 'Jill /Smith/', 'gender': 'F', 'birthday': '01 JAN 1961', 'age': 61, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        person3 = {'ID': 'I1', 'name': 'Jared /Smith/', 'gender': 'M', 'birthday': '26 JUN 2002', 'age': 20, 'alive': True, 'death': 'NA', 'child': [], 'spouse': []}
        person4 = {'ID': 'I1', 'name': 'Wonder /Wall/', 'gender': 'M', 'birthday': '01 JAN 3413', 'age': 953, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        person5 = {'ID': 'I1', 'name': 'Wonder /Wall/', 'gender': 'M', 'birthday': '01 JAN 1935', 'age': 88, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F3']}

        family = [{'ID': 'F1', 'married': '16 MAY 1969', 'divorced': 'NA', 'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'Jill /Smith/', 'children': ['I3']}, 
        {'ID': 'F2', 'married': '16 NOV 1993', 'divorced': 'NA', 'husband_id': 'I3', 'husband_name': 'Tim /Smith/', 'wife_id': 'I5', 'wife_name': 'Jane /Cooper/', 'children': ['I7', 'I9']}, 
        {'ID': 'F3', 'married': '7 AUG 1990', 'divorced': '7 SEP 2030', 'husband_id': 'I3', 'husband_name': 'Tim /Smith/', 'wife_id': 'I4', 'wife_name': 'Jen /Smith/', 'children': ['I6']}, 
        {'ID': 'F4', 'married': '20 SEP 1991', 'divorced': 'NA', 'husband_id': 'I8', 'husband_name': 'John /Doe/', 'wife_id': 'I5', 'wife_name': 'Jane /Cooper/', 'children': []}, 
        {'ID': 'F5', 'married': '11 OCT 2019', 'divorced': 'NA', 'husband_id': 'I11', 'husband_name': 'Nathan /Jones/', 'wife_id': 'I7', 'wife_name': 'Jennette /Smith/', 'children': ['I10']}]
        
        self.assertTrue(datesBeforeToday(person1, family)) #birthday, marriage, happens before today
        self.assertTrue(datesBeforeToday(person2, family)) #birthday, marriage, death happens before today
        self.assertTrue(datesBeforeToday(person3, family)) #birthday happens before today, not married
        self.assertFalse(datesBeforeToday(person4, family)) #birth is after today
        self.assertFalse(datesBeforeToday(person5, family)) #married in 2030

    def test_user_story_2(self):

        # Person born beofre  marriage
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        
        # person born before marriate -- multiple marraiges
        person2 = {'ID': 'I1', 'name': 'Jill /Smith/', 'gender': 'F', 'birthday': '01 JAN 1961', 'age': 61, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1', 'F2']}

        # person born after marraige
        person3 = {'ID': 'I1', 'name': 'Jared /Smith/', 'gender': 'M', 'birthday': '26 JUN 2002', 'age': 20, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F3']}
        
        # person born after 1 marraige & before one marraige 
        person4 = {'ID': 'I1', 'name': 'Wonder /Wall/', 'gender': 'M', 'birthday': '01 JAN 1992', 'age': 953, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1', 'F2']}

        # person born after multiple marraiges 
        person5 = {'ID': 'I1', 'name': 'Wonder /Wall/', 'gender': 'M', 'birthday': '01 JAN 3413', 'age': 88, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F3', 'F1', 'F2']}

        family = [{'ID': 'F1', 'married': '16 MAY 1969', 'divorced': 'NA', 'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'Jill /Smith/', 'children': ['I3']}, 
        {'ID': 'F2', 'married': '16 NOV 1993', 'divorced': 'NA', 'husband_id': 'I3', 'husband_name': 'Tim /Smith/', 'wife_id': 'I5', 'wife_name': 'Jane /Cooper/', 'children': ['I7', 'I9']}, 
        {'ID': 'F3', 'married': '7 AUG 1990', 'divorced': '7 SEP 2030', 'husband_id': 'I3', 'husband_name': 'Tim /Smith/', 'wife_id': 'I4', 'wife_name': 'Jen /Smith/', 'children': ['I6']}, 
        {'ID': 'F4', 'married': '20 SEP 1991', 'divorced': 'NA', 'husband_id': 'I8', 'husband_name': 'John /Doe/', 'wife_id': 'I5', 'wife_name': 'Jane /Cooper/', 'children': []}, 
        {'ID': 'F5', 'married': '11 OCT 2019', 'divorced': 'NA', 'husband_id': 'I11', 'husband_name': 'Nathan /Jones/', 'wife_id': 'I7', 'wife_name': 'Jennette /Smith/', 'children': ['I10']}]

        
        self.assertTrue(birthBeforeMarriage(person1, family)) 
        self.assertTrue(birthBeforeMarriage(person2, family)) 
        self.assertFalse(birthBeforeMarriage(person3, family))

        self.assertFalse(birthBeforeMarriage(person4, family))
        self.assertFalse(birthBeforeMarriage(person5, family))

    def test_user_story_3(self):

        # expect true - only 72
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}

        # expect true - only 149
        person2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '02 JAN 1873',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}

        # expect false - alive, but born in 1700s
        person3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '11 MAR 1764',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}

        # expect false - dead, but birthday is 1700s, and died in 1900s
        person4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JUL 1732',
                   'age': 72, 'alive': False, 'death': '02 MAR 1959', 'child': [], 'spouse': ['F1']}

        # expect false, dead, birthday in year 1
        person5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '02 JAN 1',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}

        self.assertTrue(lessThan150(personObj=person1))
        self.assertTrue(lessThan150(personObj=person2))
        self.assertFalse(lessThan150(personObj=person3))
        self.assertFalse(lessThan150(personObj=person4))
        self.assertFalse(lessThan150(personObj=person5))

    def test_user_story_4(self):

        # expect true - still together/not divorced so marriage will come before divorce in future
        family1 = {'ID': 'F1', 'married': '16 MAY 1969', 'divorced': 'NA', 'husband_id': 'I1', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I4', 'wife_name': 'Rosemary /Smith/', 'children': []}

        # expect true - married before divorcing 
        family2 = {'ID': 'F2', 'married': '5 JUN 1972', 'divorced': '1 FEB 1975', 'husband_id': 'I2', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I5', 'wife_name': 'Rosemary /Smith/', 'children': []}

        # expect false - marriage happens after divorce
        family3 = {'ID': 'F3', 'married': '20 MAR 2000', 'divorced': '14 NOV 1997', 'husband_id': 'I3', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I6', 'wife_name': 'Rosemary /Smith/', 'children': []}

        # expect false - marriage happens after divorce
        family4 = {'ID': 'F4', 'married': '14 JAN 1990', 'divorced': '10 JAN 1990', 'husband_id': 'I7', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I8', 'wife_name': 'Rosemary /Smith/', 'children': []}

        # expect true - marriage happens before divorce
        family5 = {'ID': 'F5', 'married': '30 OCT 2011', 'divorced': '31 OCT 2011', 'husband_id': 'I9', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I10', 'wife_name': 'Rosemary /Smith/', 'children': []}

        self.assertTrue(marrBefDiv(family1))
        self.assertTrue(marrBefDiv(family2))
        self.assertFalse(marrBefDiv(family3))
        self.assertFalse(marrBefDiv(family4))
        self.assertTrue(marrBefDiv(family5))

    def test_user_story_7(self):

        # expect true - death year comes after birth year
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '02 JAN 2022', 'child': [], 'spouse': ['F1']}

        # expect true - death year is same as birth year, but death month is after birth year
        person2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '02 JAN 1950',
                   'age': 72, 'alive': False, 'death': '02 FEB 1950', 'child': [], 'spouse': ['F1']}

        # expect true - death year + month are same as birth year + month, but death day is after birth day
        person3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '11 MAR 1955',
                   'age': 72, 'alive': False, 'death': '12 MAR 1955', 'child': [], 'spouse': ['F1']}

        # expect false - death year is same as birth year, but death month is before birth month
        person4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JUL 1959',
                   'age': 72, 'alive': False, 'death': '02 MAR 1959', 'child': [], 'spouse': ['F1']}

        # expect false - death year + month are same as birth year + month, but death day is before birth day
        person5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1970',
                   'age': 72, 'alive': False, 'death': '21 OCT 1970', 'child': [], 'spouse': ['F1']}

        self.assertTrue(birthBeforeDeath(personObj=person1))
        self.assertTrue(birthBeforeDeath(personObj=person2))
        self.assertTrue(birthBeforeDeath(personObj=person3))
        self.assertFalse(birthBeforeDeath(personObj=person4))
        self.assertFalse(birthBeforeDeath(personObj=person5))

    def test_user_story_8(self):


        person1 = {'ID': 'I11', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '08 MAR 1991',
                   'age': 18, 'alive': False, 'death': '02 JAN 2022', 'child': ['F1'], 'spouse': []}

        person2 = {'ID': 'I12', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '02 JAN 1977',
                   'age': 18, 'alive': False, 'death': '02 FEB 1950', 'child': ['F2'], 'spouse': []}

        person3 = {'ID': 'I13', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '21 MAR 2000',
                   'age': 18, 'alive': False, 'death': '12 MAR 1955', 'child': ['F3'], 'spouse': []}

        person4 = {'ID': 'I14', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '10 OCT 1990',
                   'age': 18, 'alive': False, 'death': '02 MAR 1959', 'child': ['F4'], 'spouse': []}

        person5 = {'ID': 'I15', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '29 OCT 2011',
                   'age': 18, 'alive': False, 'death': '21 OCT 1970', 'child': ['F5'], 'spouse': []}

        # expect true - person born after marriage
        family1 = [{'ID': 'F1', 'married': '16 MAY 1988', 'divorced': 'NA', 'husband_id': 'I1', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I4', 'wife_name': 'Rosemary /Smith/', 'children': ['I11']}]

        # expect false - person born more than 9 months after divorce
        family2 = [{'ID': 'F2', 'married': '5 JUN 1972', 'divorced': '1 FEB 1975', 'husband_id': 'I2', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I5', 'wife_name': 'Rosemary /Smith/', 'children': ['I12']}]

        # expect true - person born after marriage
        family3 = [{'ID': 'F3', 'married': '20 MAR 2000', 'divorced': 'NA', 'husband_id': 'I3', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I6', 'wife_name': 'Rosemary /Smith/', 'children': ['I13']}]

        # expect true - person born exactly 9 months after divorce
        family4 = [{'ID': 'F4', 'married': '14 JAN 1990', 'divorced': '10 JAN 1990', 'husband_id': 'I7', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I8', 'wife_name': 'Rosemary /Smith/', 'children': ['I14']}]

        # expect false - person born before marriage
        family5 = [{'ID': 'F5', 'married': '30 OCT 2011', 'divorced': 'NA', 'husband_id': 'I9', 
                    'husband_name': 'Jack /Smith/', 'wife_id': 'I10', 'wife_name': 'Rosemary /Smith/', 'children': ['I15']}]

        self.assertTrue(bornBefMarr(person1, family1))
        self.assertFalse(bornBefMarr(person2, family2))
        self.assertTrue(bornBefMarr(person3, family3))
        self.assertTrue(bornBefMarr(person4, family4))
        self.assertFalse(bornBefMarr(person5, family5))

    def test_user_story_27(self):
        # assert equal for an alive 72yr old
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}

        # assert equal for an alive 0 yr old
        person2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '29 SEP 2022',
                   'age': 0, 'alive': True, 'death': 'NA', 'child': [], 'spouse': []}

        # assert equal for an alive 1 year old
        person3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '11 MAR 2021',
                   'age': 1, 'alive': True, 'death': 'NA', 'child': [], 'spouse': []}

        # assert equal for a dead 0 yr old
        person4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JUL 1959',
                   'age': 72, 'alive': False, 'death': '02 AUG 1959', 'child': [], 'spouse': []}

        # assert equal for a dead 1 yr old
        person5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1970',
                   'age': 72, 'alive': False, 'death': '30 OCT 1971', 'child': [], 'spouse': []}

        # assert equal for a dead 30 yr old
        person6 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1981', 'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        
        self.assertEqual(72, computeAge(personObj=person1))
        self.assertEqual(0, computeAge(personObj=person2))
        self.assertEqual(1, computeAge(personObj=person3))
        self.assertEqual(0, computeAge(personObj=person4))
        self.assertEqual(1, computeAge(personObj=person5))
        self.assertEqual(30, computeAge(personObj=person6))
    
    
    def test_user_story_5(self):
        
        # assert true if husband and wife are not dead
        people1 = []
        hus1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        wife1 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        people1.append(hus1)
        people1.append(wife1)
        family1 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        
        # assert true if husband and wife have died after marriage
        people2 = []
        hus2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': '01 JAN 1970', 'child': [], 'spouse': ['F1']}
        wife2 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': '17 JUN 1969', 'child': [], 'spouse': ['F1']}
        people2.append(hus2)
        people2.append(wife2)
        family2 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        
        # assert false if husband dies before marriage
        people3 = []
        hus3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': '16 MAY 1968', 'child': [], 'spouse': ['F1']}
        wife3 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        people3.append(hus3)
        people3.append(wife3)
        family3 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        
        #assert false if wife dies before marriage
        people4 = []
        hus4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': '01 JAN 1970', 'child': [], 'spouse': ['F1']}
        wife4 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': '17 APR 1969', 'child': [], 'spouse': ['F1']}
        people4.append(hus4)
        people4.append(wife4)
        family4 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        
        #assert false if both die before marriage
        people5 = []
        hus5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': '01 MAY 1969', 'child': [], 'spouse': ['F1']}
        wife5 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': '15 MAY 1969', 'child': [], 'spouse': ['F1']}
        people5.append(hus5)
        people5.append(wife5)
        family5 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        
        self.assertTrue(MarriageBeforeDeath(family1, people1))
        self.assertTrue(MarriageBeforeDeath(family2, people2))
        self.assertFalse(MarriageBeforeDeath(family3, people3))
        self.assertFalse(MarriageBeforeDeath(family4, people4))
        self.assertFalse(MarriageBeforeDeath(family5, people5))
    
    def test_user_story_9(self):
        people1 = []
        hus1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        wife1 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        child1 = {'ID': 'I3', 'name': 'James /Smith/', 'gender': 'M', 'birthday': '01 JAN 1970', 'age': 50, 'alive': True, 'death': 'NA', 'child': ['F1'], 'spouse': ['']}
        people1.append(hus1)
        people1.append(wife1)
        family1 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        fam1 = [family1]
        
        # assert true if mother died after and husband died in reasonable time frame, within 9 months before
        people2 = []
        hus2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': '01 SEP 1969', 'child': [], 'spouse': ['F1']}
        wife2 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': '01 JAN 1971', 'child': [], 'spouse': ['F1']}
        child2 = {'ID': 'I3', 'name': 'James /Smith/', 'gender': 'M', 'birthday': '01 JAN 1970', 'age': 50, 'alive': True, 'death': 'NA', 'child': ['F1'], 'spouse': ['']}
        people2.append(hus2)
        people2.append(wife2)
        family2 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        fam2 = [family2]
        
        #assert false if husband dies more than 9 months before childs birth
        people3 = []
        hus3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': '01 FEB 1969', 'child': [], 'spouse': ['F1']}
        wife3 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        child3 = {'ID': 'I3', 'name': 'James /Smith/', 'gender': 'M', 'birthday': '01 JAN 1970', 'age': 50, 'alive': True, 'death': 'NA', 'child': ['F1'], 'spouse': ['']}
        people3.append(hus3)
        people3.append(wife3)
        family3 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        fam3 = [family3]
        
        # assert false if mother dies at any point before childs birth
        people4 = []
        hus4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        wife4 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': '01 JAN 1968', 'child': [], 'spouse': ['F1']}
        child4 = {'ID': 'I3', 'name': 'James /Smith/', 'gender': 'M', 'birthday': '01 JAN 1970', 'age': 50, 'alive': True, 'death': 'NA', 'child': ['F1'], 'spouse': ['']}
        people4.append(hus4)
        people4.append(wife4)
        family4 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        fam4 = [family4]
        
        # assert false if both parents die before childs brith
        people5 = []
        hus5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': '16 MAY 1965', 'child': [], 'spouse': ['F1']}
        wife5 = {'ID': 'I2', 'name': 'jill /Smith/', 'gender': 'F', 'birthday': '02 FEB 1952', 'age': 70, 'alive': True, 'death': '01 JAN 1965', 'child': [], 'spouse': ['F1']}
        child5 = {'ID': 'I3', 'name': 'James /Smith/', 'gender': 'M', 'birthday': '01 JAN 1970', 'age': 50, 'alive': True, 'death': 'NA', 'child': ['F1'], 'spouse': ['']}
        people5.append(hus5)
        people5.append(wife5)
        family5 = {'ID': 'F1', 'married': '16 MAY 1969' ,'husband_id': 'I1', 'husband_name': 'Jack /Smith/', 'wife_id': 'I2', 'wife_name': 'jill /Smith/', 'children' : []}
        fam5 = [family5]
        
        
        self.assertTrue(BirthBeforeParentsDeath(child1,fam1,people1))
        self.assertTrue(BirthBeforeParentsDeath(child2,fam2,people2))
        self.assertFalse(BirthBeforeParentsDeath(child3,fam3,people3))
        self.assertFalse(BirthBeforeParentsDeath(child4,fam4,people4))
        self.assertFalse(BirthBeforeParentsDeath(child5,fam5,people5))
        

    def test_user_story_6(self):
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        marriage1 = {'ID': 'T1','married': '21 OCT 1966', 'divorced':'NA', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        marriage2 = {'ID': 'T1', 'married': '21 OCT 1966','divorced':'21 OCT 1969', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        marriage3 = {'ID': 'T1', 'married': '21 OCT 1966','divorced':'21 OCT 2014', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        marriage4 = {'ID': 'T1', 'married': '21 OCT 1966','divorced':'21 OCT 2011', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        marriage5 = {'ID': 'T1', 'married': '21 OCT 1966','divorced':'21 OCT 2012', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person6 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        marriage6 = {'ID': 'T1', 'married': '21 OCT 1966','divorced':'21 OCT 2020', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        self.assertTrue(deathBeforeDivorce(personObj=person1, family=marriage1))
        self.assertTrue(deathBeforeDivorce(personObj=person2, family=marriage2))
        self.assertFalse(deathBeforeDivorce(personObj=person3, family=marriage3))
        self.assertTrue(deathBeforeDivorce(personObj=person4, family=marriage4))
        self.assertTrue(deathBeforeDivorce(personObj=person5, family=marriage5))
        self.assertFalse(deathBeforeDivorce(personObj=person6, family=marriage6))



    def test_user_story_10(self):
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        marriage1 = {'ID': 'T1','married': '21 OCT 1966', 'divorced':'NA', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        marriage2 = {'ID': 'T1', 'married': '21 OCT 1955','divorced':'21 OCT 1969', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        marriage3 = {'ID': 'T1', 'married': '21 OCT 1980','divorced':'21 OCT 2014', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        marriage4 = {'ID': 'T1', 'married': '21 OCT 1951','divorced':'21 OCT 2011', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        person5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        marriage5 = {'ID': 'T1', 'married': '21 OCT 1956','divorced':'21 OCT 2012', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "F1", 'wife_name': "Jannete /Smith/", 'children':[]  }

        self.assertTrue(marriageAfter14(personObj=person1, family=marriage1))
        self.assertFalse(marriageAfter14(personObj=person2, family=marriage2))
        self.assertTrue(marriageAfter14(personObj=person3, family=marriage3))
        self.assertFalse(marriageAfter14(personObj=person4, family=marriage4))
        self.assertFalse(marriageAfter14(personObj=person5, family=marriage5))

    def test_user_story_16(self):
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        person2 = {'ID': 'I2', 'name': 'Jannete /Cooper/', 'gender': 'F', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        
        person3 = {'ID': 'I3', 'name': 'JackJr /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': ['F1'], 'spouse': ['F2']}
        person4 = {'ID': 'I4', 'name': 'Jill /Green/', 'gender': 'F', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F2']}
        
        person5 = {'ID': 'I5', 'name': 'Cassy /Black/', 'gender': 'F', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': ['F2'], 'spouse': ['F3']}
        person6 = {'ID': 'I6', 'name': 'Timmy /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': ['F2'], 'spouse': ['F4']}
        
        # 7 marries 5
        person7 = {'ID': 'I7', 'name': 'DJ /Drew/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': ['F5'], 'spouse': ['F3']}
        
        # 8 marries 6
        person8 = {'ID': 'I8', 'name': 'Julia /Faraday/', 'gender': 'F', 'birthday': '01 JAN 1950', 'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F4', 'F5']}
        
        person9 = {'ID': 'I9', 'name': 'James /Red/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': ['F4'], 'spouse': []}
        
        person10 = {'ID': 'I10', 'name': 'Jon /Drew/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['I8']}
        
        person11 = {'ID': 'I11', 'name': 'Derek /Bell/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': ['F5'], 'spouse': []}
        
        # Family where 2 males have same last name - all children are male
        family1 = {'ID': 'F1','married': '21 OCT 1966', 'divorced':'NA', 'husband_id': "I1", 'husband_name':'Jack /Smith/','wife_id': "I2", 'wife_name': "Jannete /Smith/", 'children':['I3']  }

        # Family where 2 males have same last name - male and female child has different last name. Result length should still be 1 
        family2 = {'ID': 'F2', 'married': '21 OCT 1955','divorced':'21 OCT 1969', 'husband_id': "I3", 'husband_name':'JackJr /Smith/','wife_id': "I4", 'wife_name': "Jill /Green/", 'children':['I5', 'I6']  }

        # Family with 1 male (husband) - all female children w/ diff names
        family3 = {'ID': 'F3', 'married': '21 OCT 1980','divorced':'21 OCT 2014', 'husband_id': "I7", 'husband_name':'DJ /Drew/','wife_id': "I5", 'wife_name': "Cassy /Black/", 'children':['I8']  }

        # Family where 2 males have different last name - male child with different last name.
        family4 = {'ID': 'F4', 'married': '21 OCT 1951','divorced':'21 OCT 2011', 'husband_id': "I6", 'husband_name':'Timmy /Smith/','wife_id': "I8", 'wife_name': "Julia /Faraday/", 'children':['I9']  }
 
        # Family with 3 males - husband and male child 1 share a name, male child 2 has a different name
        family5 = {'ID': 'F5', 'married': '21 OCT 1956','divorced':'21 OCT 2012', 'husband_id': "I10", 'husband_name':'Jon /Drew/','wife_id': "I8", 'wife_name': "Julia /Faraday/", 'children':['I7', 'I11']  }
        
        people = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10, person11]
        
        self.assertEqual(maleLastNames(family1, people), {'/Smith/'})
        self.assertEqual(maleLastNames(family2, people), {'/Smith/'})
        self.assertEqual(maleLastNames(family3, people), {'/Drew/'})
        self.assertEqual(maleLastNames(family4, people), {'/Smith/', '/Red/'})
        self.assertEqual(maleLastNames(family5, people), {'/Drew/', '/Bell/'})

if __name__ == '__main__':
    unittest.main()
