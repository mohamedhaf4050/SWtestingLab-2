from locator import * 
from element import BasePageElement

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

#To use the search SearchTextElement
class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    locator = 'q'

class MainPage(BasePage):
    #Create a python descriptor i.e., it uses the __get__
    search_text_element = SearchTextElement()  

    """Home page action methods come here. I.e. Python.org"""
    def is_title_matches(self):
        return "Python" in self.driver.title
    
    def click_go_button(self): 
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):
    #If any results are found from the search page
    def is_results_found(self):
        return "No results found." not in self.driver.page_source 

