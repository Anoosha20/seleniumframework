import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import openpyxl
from Tsetdata.HomePageData import HomePageData
from pageObjects.Homepage import Homepage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = Homepage(self.driver)
        log.info("first name is "  +getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.getSubmit().click()
        message = homePage.getSuccessMessage().text
        assert ("success" in message)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
