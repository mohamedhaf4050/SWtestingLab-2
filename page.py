from locator import * 
from element import BasePageElement

#Define a class for each page on your website
#Both classes should inherit from base(page)

#BasePage is the base class that all our pages should inherit from
#If we have a common method that all pages will use then put it in basePage
# And inherit the BasePage 
class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

#To locate a specific element on the page using the element.py
class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = 'q'

class MainPage(BasePage):
    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()
    """Home page action methods come here. I.e. Python.org"""
    #Test 1 verifies that the provided text exsist in the page title
    def is_title_matches(self):
        #Verifies that the hardcoded text "Python" appears in the title of 
        return "Python" in self.driver.title
    
    #Test 2: To click the go button  
    def click_go_button(self):
        #Triggers the search button
        #First, we need to locate the by  its ID 
        #Using the locator defined in the locators page   
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    


#Results found page
class SearchResultsPage(BasePage):
    #Search results page action methods come here
    #If "No results found." is not in the page it returns true 
    #If it exsists in the page it returns false
    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source 

