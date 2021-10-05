import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Setup webdriver path downloaded at: https://chromedriver.chromium.org/downloads
# put the chromedriver.exe file into a folder called 'Driver' in the same folder as this file
chromedriver_path = r'.\chromedriver.exe'

# Set maximum window size
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.headless = True

# Path to webdriver 
browser = webdriver.Chrome(chromedriver_path, options=options)

# Browse to url
url = "https://vsb.mcgill.ca/vsb/criteria.jsp?welcome=1"
browser.get(url)

# Wait
time.sleep(3)

# Browse through first page by pressing 'Continue'
element = browser.find_element_by_xpath("//input[@value='Continue']")
element.send_keys(Keys.RETURN)

# Wait
time.sleep(3)

# args example: "Summer 2021", "CCOM 206", "Lec 701")
def check_availability(term: str, course_name: str, lecture: str) -> bool:
    # Select term 
    term_select_element = browser.find_element_by_css_selector("input[type='radio'][data-termlabel='{}']".format(term))
    term_select_element.click()
    
    # Wait
    time.sleep(3)
    
    # Enter course name
    course_name_element = browser.find_element_by_id("code_number")
    course_name_element.send_keys(course_name)
    course_name_element.send_keys(Keys.RETURN)
    
    # Wait
    time.sleep(3)
    
    # Select lecture
    for label in browser.find_elements_by_css_selector("label.vsbselectionnew"):
        if (label.find_element_by_css_selector("div div table tbody tr td+td strong").text == lecture):
            label.find_element_by_css_selector("div div table tbody tr td input").click()
            
    # Wait
    time.sleep(3)

# Run setup
setup("Fall 2021", "ECSE324", "Lec 702")