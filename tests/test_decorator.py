import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def test_decorator():
    allure.dynamic.tag("tage")
    allure.dynamic.link("www.leningrad", "точка ру")
    allure.dynamic.label("labelity")
    open_browser()
    search_repository('rollnicker/QAGuru9_7')
    open_repository('rollnicker/QAGuru9_7')
    open_issues_tab()
    should_see_issue_with_name("Issue for test Allure")

@allure.step("Открыть главную страницу")
def open_browser():
    browser.open("https://github.com")

@allure.step("Поиск реппозитория {repo}")
def search_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo).submit()

@allure.step("Открываем репозиторий {repo}")
def open_repository(repo):
    s(by.link_text(repo)).click()

@allure.step("Открываем вкладку Issues")
def open_issues_tab():
    s('#issues-tab').click()

@allure.step("Проверяем наличие Issue с навзанием {name}")
def should_see_issue_with_name(name):
    s(by.partial_text(name)).should(be.visible)
