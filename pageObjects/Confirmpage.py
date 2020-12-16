from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countryname = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    text = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCountryName(self):
        self.driver.find_element(*ConfirmPage.countryname).click()

    def getCheckbox(self):
        self.driver.find_element(*ConfirmPage.checkbox).click()

    def getSubmit(self):
        self.driver.find_element(*ConfirmPage.submit).click()

    def getText(self):
        return self.driver.find_element(*ConfirmPage.text)
