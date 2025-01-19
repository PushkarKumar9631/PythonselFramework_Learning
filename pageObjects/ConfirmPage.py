from selenium.webdriver.common.by import By


class ConfirmPage:

    success_button = (By.XPATH, "//button[@class='btn btn-success']")
    countryField_locator = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "[type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")


    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']")

    def successButton(self):
        return self.driver.find_element(*ConfirmPage.success_button)

    # self.driver.find_element(By.ID, "country")

    def countryField(self):
        return self.driver.find_element(*ConfirmPage.countryField_locator)

    def countrySelected(self):
        return self.driver.find_element(*ConfirmPage.country)

    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def checkBoxClick(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)


    # self.driver.find_element(By.CLASS_NAME, "alert-success")

    def successMessageCatch(self):
        return self.driver.find_element(*ConfirmPage.successMessage).text
