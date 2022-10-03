import unittest
from operations import *

# Command to run script:
# $Python3 test_stories.py

# TESTS GO HERE


class testStories(unittest.TestCase):
    def test_user_story_1(self):

        # expect true - birthday and death come before today
        person1 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '01 JAN 1950',
                   'age': 72, 'alive': False, 'death': '02 JAN 2022', 'child': [], 'spouse': ['F1']}

        # expect false - birth year come after today
        person2 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '02 JAN 2030',
                   'age': 72, 'alive': False, 'death': '02 FEB 1950', 'child': [], 'spouse': ['F1']}

        # expect false - death year come after today
        person3 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1970',
                   'age': 72, 'alive': False, 'death': '21 OCT 2040', 'child': [], 'spouse': ['F1']}

        # expect false - death year same, month after today
        person4 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 2030',
                   'age': 72, 'alive': False, 'death': '21 OCT 2022', 'child': [], 'spouse': ['F1']}

        # expect true - death year come after today
        person5 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1970',
                   'age': 72, 'alive': False, 'death': '21 OCT 2000', 'child': [], 'spouse': ['F1']}
        self.assertTrue(datesBeforeToday(personObj=person1))
        self.assertFalse(datesBeforeToday(personObj=person2))
        self.assertFalse(datesBeforeToday(personObj=person3))
        self.assertFalse(datesBeforeToday(personObj=person4))
        self.assertTrue(datesBeforeToday(personObj=person5))

    def test_user_story_2(self):

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

        self.assertTrue(lessThan150(personObj=person1))
        self.assertTrue(lessThan150(personObj=person2))
        self.assertFalse(lessThan150(personObj=person3))
        self.assertFalse(lessThan150(personObj=person4))

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
        person6 = {'ID': 'I1', 'name': 'Jack /Smith/', 'gender': 'M', 'birthday': '30 OCT 1981',
                   'age': 72, 'alive': False, 'death': '21 OCT 2012', 'child': [], 'spouse': ['F1']}

        self.assertEqual(72, computeAge(personObj=person1))
        self.assertEqual(0, computeAge(personObj=person2))
        self.assertEqual(1, computeAge(personObj=person3))
        self.assertEqual(0, computeAge(personObj=person4))
        self.assertEqual(1, computeAge(personObj=person5))
        self.assertEqual(30, computeAge(personObj=person6))

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

        self.assertTrue(divorceBeforeDeath(personObj=person1, family=marriage1))
        self.assertTrue(divorceBeforeDeath(personObj=person2, family=marriage2))
        self.assertFalse(divorceBeforeDeath(personObj=person3, family=marriage3))
        self.assertTrue(divorceBeforeDeath(personObj=person4, family=marriage4))
        self.assertTrue(divorceBeforeDeath(personObj=person5, family=marriage5))
        self.assertFalse(divorceBeforeDeath(personObj=person6, family=marriage6))



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

        #   ID: string
#   married: string: date
#   divorced: string: 'NA' or date
#   husband_id: id
#   husband_name: string
#   wife_id: id
#   wife_name: string
#   children: list of strings




if __name__ == '__main__':
    unittest.main()
