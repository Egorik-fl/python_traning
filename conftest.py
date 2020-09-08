import pytest
from fixture.applicat import Application


@pytest.fixture(scope="session")
# scope="session" выполнение всех тестов за 1 сесию, те открытие 1 браузера
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture