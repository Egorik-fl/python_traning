# Generated by Selenium IDE

from model.group import Group


# exec_path = r'I:\Python\aqwe\PET\testers\geckodriver.exe'
# URL = r'http://127.0.0.1:8000/admin/login/'
# driver = webdriver.Firefox(executable_path=exec_path)
# driver.get(URL)


def test_admin(app):
    app.open_home_page()
    app.login(username="root", password="root")
    app.open_page()
    app.group_form(Group(title="qwe", post="qweqwe"))
    app.criet()
    app.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.login(username="root", password="root")
    app.open_page()
    app.group_form(Group(title="", post=""))
    app.criet()
    app.logout()


