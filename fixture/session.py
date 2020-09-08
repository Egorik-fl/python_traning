

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        wd.find_element("id_username").click()
        wd.find_element("id_username").send_keys(username)
        wd.find_element(".login").click()
        wd.find_element("id_password").click()
        wd.find_element("id_password").send_keys(password)
        wd.find_element(".submit-row > input").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element("a:nth-child(4)").click()
        wd.set_window_size(1315, 837)