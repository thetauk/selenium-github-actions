from selenium.webdriver.common.by import By
from tauk.tauk_webdriver import Tauk

from test.tauk_test import TaukTest


class WelcomeTest(TaukTest):
    @Tauk.observe(custom_test_name="TaukWelcomeTest", excluded=False)
    def test_ClickPrimaryButton(self):
        self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=".btn-primary"
        ).click()