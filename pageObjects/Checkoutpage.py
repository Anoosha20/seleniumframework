from selenium.webdriver.common.by import By

from pageObjects.Confirmpage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
    cardtitle = (By.CSS_SELECTOR, ".card-title a")
    cardfooter = (By.CSS_SELECTOR, ".card-footer button")
    cardButtonAdd = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    cardButtonCheckout= (By.XPATH, "//button[@class='btn btn-success']")

    def getcardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardtitle)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardfooter)

    def getcardButtonAdd(self):
        self.driver.find_element(*CheckOutPage.cardButtonAdd).click()

    def getcardButtonCheckout(self):
        self.driver.find_element(*CheckOutPage.cardButtonCheckout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

