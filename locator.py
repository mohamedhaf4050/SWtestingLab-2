#Any file we locate on the website gets located in this page:
from selenium.webdriver.common.by import By

# A class for that locates any element on the main page.
class MainPageLocators(object):
    #Locate the go_button using its ID and its value "submit"
    GO_BUTTON = (By.ID, 'submit')


#For example to locate the elements on the search page
#We can define a class to locate all the elements on the Search page
class SearchResultsPageLocators(object):
    pass

