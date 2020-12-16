import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile.txt')  # mode = 'w' clear the log data from last execution
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        # reducing same lines :code
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(filehandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10) \
            .until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
        dropdown.select_by_index(0)
