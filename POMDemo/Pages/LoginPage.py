class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = "//*[@id='txtUsername']"
        self.password_textbox_id = "//*[@id='txtPassword']"
        self.login_button_id = "//*[@id='btnLogin']"

    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.username_textbox_id).clear()
        self.driver.find_element_by_xpath(self.username_textbox_id).send_keys(username)


    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_id).clear()
        self.driver.find_element_by_xpath(self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button_id).click()
