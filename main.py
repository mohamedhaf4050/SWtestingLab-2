import unittest
from selenium import webdriver
import page
import time

class PythonOrgSearch(unittest.TestCase): 
    """A sample test class to show how page object works"""
    def setUp(self): 
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    #Test 1:
    def test_title(self):
        print("Test 1")
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
    
    #Test 2:
    def test_search_in_python_org(self):
        print("Test 2")
        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)

        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)

        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")
        
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()