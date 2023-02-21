from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='/Users/svetlanalevinsohn/JobEasy/13-python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url