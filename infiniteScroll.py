# pip install selenium first

# Necessary Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

# Create a InfiniteScroll Class
class InfiniteScroll:
    def __init__(self, timeout):
        # Path to our chrome driver.
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        # Set a driver instance variable.
        self.driver = webdriver.Chrome(PATH)
        # This is the website the webdriver will connect to.
        self.driver.get("https://amazon.com")
        # Get the scroll height of the current page.
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        # Scroll down to bottom untill the new height of the page is equal to the last.
        while True:
            # Scroll down to bottom.
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            # Give the page time to load.
            sleep(timeout)
            # Calculate new scroll height and compare with last scroll height.
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            # Set a statement that if true we exit our loop
            if new_height == last_height:
                # Before exiting you can execute the code you want :)
                print("Executing code...")
                # If heights are the same exit the function
                break
            last_height = new_height

# Lets call our class 
InfiniteScroll(5)