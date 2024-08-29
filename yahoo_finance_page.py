from RPA.Browser.Selenium import Selenium

class YahooFinancePage(Selenium):
    
    def open_yahoo_finance(self):
        self.open_browser('https://finance.yahoo.com/', browser='chrome', headless=False)
    
    def click_sign_up(self):
        # Adjust the locator according to the actual page structure
        self.click_element("xpath=//a[contains(text(), 'Sign up')]")
    
    def fill_registration_form(self, username, email, password):
        # Adjust locators according to the actual page structure
        self.input_text("name=username", username)
        self.input_text("name=email", email)
        self.input_text("name=password", password)
    
    def submit_registration_form(self):
        # Adjust the locator according to the actual page structure
        self.click_element("xpath=//button[contains(text(), 'Sign Up')]")
    
    def wait_for_confirmation(self):
        # Adjust the locator according to the actual page structure
        self.wait_until_element_is_visible("xpath=//h1[contains(text(), 'Account Created')]")
