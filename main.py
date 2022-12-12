

import unittest
from selenium import webdriver
import page

# Test we're going to perform on the website
class PythonOrgSearch(unittest.TestCase): #Inherits from unittest.TestCase
    """A sample test class to show how page object works"""

    # Setup is the first method runs each time we test our website
    def setUp(self): 
        # Creating the webdriver we're going to use
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

        # Getting the website we want to test
        self.driver.get("http://www.python.org")

    #To create a test that automatically runs when we run our unit test
    #Create a method startswith "test": e.g., testMethod(), testNext(), testaaa()
    #Any method doesn't start with "test" is No a Test methods e.g.:
    #ntest(), Test(),TEST(), aasda(), atest()
    
    #Test 1:
    def test_title(self):
        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        
        #Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
    


    def tearDown(self):
            self.driver.close()
    
if __name__ == "__main__":
    unittest.main()