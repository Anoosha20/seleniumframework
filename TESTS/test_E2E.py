from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Checkoutpage import CheckOutPage
from pageObjects.Homepage import Homepage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = Homepage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getcardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getcardFooter()[i].click()
        checkoutpage.getcardButtonAdd()
        confirmpage = checkoutpage.getcardButtonCheckout()
        log.info("entering country name as ind")
        confirmpage.getCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmpage.getCountryName()
        confirmpage.getCheckbox()
        confirmpage.getSubmit()
        textmatch = confirmpage.getText().text
        log.info("text received from application is " +textmatch)

        assert "Success! Thank you!" in textmatch