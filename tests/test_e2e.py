import os.path
from datetime import datetime

# import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# from fileinput import filename

# @pytest.mark.usefixtures("setup") ## this is commented because we need not to use this because we are using BaseClass
class TestOne(BaseClass):  ## here i have called Baseclass where fixture is used and removed fixture line from above to
    ## our code look more cleaner

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        checkoutPage = CheckoutPage(self.driver)
        products = checkoutPage.getCardTitles()

        i = -1
        for product in products:
            i = i + 1
            productName = product.text
            if productName == "Blackberry":
                # Add item into cart
                checkoutPage.addToCart()[i].click()

        checkoutPage.checkOut().click()
        confirmPage = ConfirmPage(self.driver)
        confirmPage.successButton().click()
        confirmPage.countryField().send_keys("ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located(confirmPage.country))
        confirmPage.countrySelected().click()
        confirmPage.checkBoxClick().click()
        confirmPage.purchaseButton().click()
        wait.until(expected_conditions.visibility_of_element_located(confirmPage.successMessage))
        successText = confirmPage.successMessageCatch()

        assert "Success! Thank you!" in successText

        # fileName = "screen2.png" ## this is for simple naming, now for dyanamic file naming use below line

        file_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"  # this will generate dyanamic filename using timedate
        file_path = os.path.join(r"F:\PythonselFramework\tests\screenshots", file_name)

        if self.driver.get_screenshot_as_file(file_path):
            print(f"Screenshot successfully saved at: {file_path}")
        else:
            print("Failed to save the screenshot.")

