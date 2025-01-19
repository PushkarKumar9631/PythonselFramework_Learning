from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

# self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']") ## defined this as page object below  ## here '*' star symbol used as regular

    shop = (By.CSS_SELECTOR, "a[href*='shop']")  # here we are storing it as tupple in shop object

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)  ## here * is used for storing the data as needed