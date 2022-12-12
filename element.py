#This page represents a specific elements on the page: 
#E.g., it represents the search bar, a specific input element, etc.
from selenium.webdriver.support.ui import WebDriverWait
class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    #For example let's create get and set the text 'Value' of any object passed to the 
    #__get__,and __set__ 

    # locator = "q"
    def __set__(self, obj, value):
        #Set the text of any element to the value supplied..
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value) 

    def __get__(self, obj, owner):
        #Gets the text of the specified element
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")

    
 