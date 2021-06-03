import unittest

# write a method that takes in a a phone_number as a string
# if the string contains letters it is invalid
# if a strig does not have 10 digits it is invalid
# any other chracter should be ignored

<<<<<<< HEAD
#these changes are being made to the file in richard-code2
#knees week, arms are heavy. there's vomit on his sweater already, moms spagetti
=======
#These changes are being made to the file in richard-code
#check check, one two, one two

>>>>>>> 499a20c54603c7bd27464cdcd2587605c991e773
def isphone_number(phone_number):
    pn = phone_number
    pn = pn.lower()                 #convert any letters to lower case
    if (pn.islower() == True):      #test for any lowercase, if true...
        return False                #is not valid, return false
    else:
        pn = "".join(filter(str.isdigit, pn))   #else, filter phone number to numberic char
        if len(pn) != 10:                       #if not 10 char long, false
            return False  
        else:
            return True                         #if 10 char long, true



########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_phone_1(self):
        valid_number = isphone_number('555-555-5555')
        self.assertEquals(valid_number,True)
        
    def test_phone_2(self):
        valid_number = isphone_number('555!555 5555')
        self.assertEquals(valid_number,True)
    
    def test_phone_3(self):
        valid_number = isphone_number('5b5-5a5-5555')
        self.assertEquals(valid_number,False)
    
    def test_phone_4(self):
        valid_number = isphone_number('555-5a5-5555')
        self.assertEquals(valid_number,False)
    
    def test_phone_5(self):
        valid_number = isphone_number('555-555-555')
        self.assertEquals(valid_number,False)

    def test_phone_6(self):
        valid_number = isphone_number('5555-5555-5555')
        self.assertEquals(valid_number,False)

    

if __name__ == '__main__':
    unittest.main()
