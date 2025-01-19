from selenium.webdriver.common.by import By


class CheckoutPage:

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    addToCartButton = (By.CSS_SELECTOR, ".card-footer button")
    checkOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']") # defining this as page object


    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def addToCart(self):
        return self.driver.find_element(*CheckoutPage.addToCartButton)

    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")

    def checkOut(self):
        return self.driver.find_element(*CheckoutPage.checkOutButton)




