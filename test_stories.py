import unittest
from operations import computeAge, birthBeforeDeath

# Command to run script: 
# $Python3 test_stories.py

# TESTS GO HERE
class testStories(unittest.TestCase):
    
    def test_user_story_2(self):
        
        # expect true - death year comes after birth year
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': False, 'death': '02 JAN 2022', 'child': [], 'spouse': ['F1']}
        
        # expect true - death year is same as birth year, but death month is after birth year
        person2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '02 JAN 1950', 'age': 72, 'alive': False, 'death': '02 FEB 1950', 'child': [], 'spouse': ['F1']}
        
         # expect true - death year + month are same as birth year + month, but death day is after birth day
        person3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '11 MAR 1955', 'age': 72, 'alive': False, 'death': '12 MAR 1955', 'child': [], 'spouse': ['F1']}
        
        # expect false - death year is same as birth year, but death month is before birth month
        person4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JUL 1959', 'age': 72, 'alive': False, 'death': '02 MAR 1959', 'child': [], 'spouse': ['F1']}
        
        # expect false - death year + month are same as birth year + month, but death day is before birth day
        person5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1970', 'age': 72, 'alive': False, 'death': '21 OCT 1970', 'child': [], 'spouse': ['F1']}
        
        self.assertTrue(birthBeforeDeath(personObj=person1))
        self.assertTrue(birthBeforeDeath(personObj=person2))
        self.assertTrue(birthBeforeDeath(personObj=person3))
        self.assertFalse(birthBeforeDeath(personObj=person4))
        self.assertFalse(birthBeforeDeath(personObj=person5))
        
    def test_user_story_27(self):    
        # assert equal for an alive 72yr old 
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950', 'age': 72, 'alive': True, 'death': 'NA', 'child': [], 'spouse': ['F1']}
        
        # assert equal for an alive 0 yr old
        person2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '29 SEP 2022', 'age': 0, 'alive': True, 'death': 'NA', 'child': [], 'spouse': []}
        
         # assert equal for an alive 1 year old
        person3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '11 MAR 2021', 'age': 1, 'alive': True, 'death': 'NA', 'child': [], 'spouse': []}
        
        # assert equal for a dead 0 yr old
        person4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JUL 1959', 'age': 72, 'alive': False, 'death': '02 AUG 1959', 'child': [], 'spouse': []}
        
        # assert equal for a dead 1 yr old
        person5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1970', 'age': 72, 'alive': False, 'death': '30 OCT 1971', 'child': [], 'spouse': []}
        
        # assert equal for a dead 30 yr old
        person6 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1981', 'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}
        
        self.assertEqual(72, computeAge(personObj=person1))
        self.assertEqual(0, computeAge(personObj=person2))
        self.assertEqual(1, computeAge(personObj=person3))
        self.assertEqual(0, computeAge(personObj=person4))
        self.assertEqual(1, computeAge(personObj=person5))
        self.assertEqual(30, computeAge(personObj=person6))

if __name__ == '__main__':
    unittest.main()
    