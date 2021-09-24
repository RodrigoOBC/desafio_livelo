from selenium import webdriver
from behave import fixture, use_fixture

class Browser(object):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    
    # Fecha o browser
    def browser_quit(self):
        self.driver.quit()
    
    # Limpa o browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()

    def before_scenario(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.set_page_load_timeout(30)
        driver.maximize_window()

    def after_scenario(self):
        self.browser_quit()