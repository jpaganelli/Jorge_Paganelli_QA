import unittest
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


driver = webdriver.Firefox()
warning = 'ng-form.form_body:nth-child(2) div:nth-child(4) div:nth-child(2) div:nth-child(1)'

class TestLogin(unittest.TestCase):
    def set_env(self, env):
        try:
            with open('.\config\config.json', 'r') as f:
                cfg = json.load(f)
            for data in cfg:
                if data["env"] == env:
                    return data
            raise Exception
        except: raise Exception


    def test_login_fail(self):
        data = self.set_env('PRD')
        driver.get(data["url"])
        message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, warning)))
        assert message.text == "", \
            "Failed login attempt message is visible"
        username_input = driver.find_element_by_name('username')
        pass_input = driver.find_element_by_name('password')
        button = driver.find_element_by_css_selector('.add-margin-top-normal button')
        username_input.send_keys(data["username"])
        pass_input.send_keys(data["password"])
        button.click()
        message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, warning)))
        assert message.text != "", \
            "Failed login attempt message is not displayed"
        driver.close()


if __name__ == '__main__':
    unittest.main()