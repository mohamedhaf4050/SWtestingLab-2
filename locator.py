#Locates element on the page using ID, class, etc.
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
    #A class for search results locators. All search results locators should come here
    pass