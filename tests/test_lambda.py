import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.feature("QAGuru")
@allure.description("Homework")
@allure.story("Изучал алюр")
@allure.suite("учил теги")
@allure.label("owner","boss")
@allure.severity(Severity.CRITICAL)
@allure.link("http://github.com", name="github")
def test_lambda_github():
    with allure.step("Открываем страницу Github"):
        browser.open("https://github.com")

    with allure.step("Поиск реппозитория"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('rollnicker/QAGuru9_7').press_enter()

    with allure.step("Открываем репозиторий"):
        s(by.link_text("rollnicker/QAGuru9_7")).click()

    with allure.step("Открываем вкладку Issues"):
        s('#issues-tab').click()

    with allure.step("Проверяем наличие Issue"):
        s(by.partial_text("Issue for test Allure")).should(be.visible)
