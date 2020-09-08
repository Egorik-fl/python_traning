from selenium import webdriver
from selenium.webdriver.common.by import By
# from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'I:\Python\aqwe\PET\testers\geckodriver.exe')
        self.vars = {}
        # self.session = SessionHelper(self)

    def criet(self):
        self.driver.find_element(By.LINK_TEXT, "News").click()
        self.driver.find_element(By.LINK_TEXT, "Articless").click()

    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4)").click()
        self.driver.set_window_size(1315, 837)

    def group_form(self, group):
        # fill group form
        self.driver.find_element(By.ID, "id_title").send_keys(group.title)
        self.driver.find_element(By.ID, "id_post").click()
        self.driver.find_element(By.ID, "id_post").send_keys(group.post)
        self.driver.find_element(By.CSS_SELECTOR, ".date-icon").click()
        self.driver.find_element(By.LINK_TEXT, "9").click()
        self.driver.find_element(By.CSS_SELECTOR, ".clock-icon").click()
        self.driver.find_element(By.LINK_TEXT, "Midnight").click()
        # save
        self.driver.find_element(By.NAME, "_save").click()

    def open_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".model-articles .addlink").click()

    def login(self, username, password):
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, ".login").click()
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()

    def open_home_page(self):
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

    def destroy(self):
        self.driver.quit()

    def delete_first_group(self):
        self.driver.find_element(By.LINK_TEXT, "Articless").click()
        self.driver.find_element(By.NAME, "_selected_action").click()
        self.driver.find_element(By.NAME, "action").click()
        dropdown = self.driver.find_element(By.NAME, "action")
        dropdown.find_element(By.XPATH, "//option[. = 'Delete selected articless']").click()
        self.driver.find_element(By.NAME, "action").click()
        self.driver.find_element(By.NAME, "index").click()
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").click()