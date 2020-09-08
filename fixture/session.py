from selenium.webdriver.common.by import By


# class SessionHelper:
#
#     def __init__(self, app):
#         self.app = app
#
#     def login(self, username, password):
#         self.app.open_home_page()
#         self.driver.find_element(By.ID, "id_username").click()
#         self.driver.find_element(By.ID, "id_username").send_keys(username)
#         self.driver.find_element(By.CSS_SELECTOR, ".login").click()
#         self.driver.find_element(By.ID, "id_password").click()
#         self.driver.find_element(By.ID, "id_password").send_keys(password)
#         self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
#
#     def logout(self):
#         self.driver.find_element("a:nth-child(4)").click()
#         self.driver.set_window_size(1315, 837)