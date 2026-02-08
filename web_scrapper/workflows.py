from .pages.search_vat import SearchPage
from .pages.result_page import ResultPage
from .core.actions import Actions
from .pages.accept_cookies import Cookies

def search_and_get_result(driver, vat_id, country):
    actions = Actions(driver)

    cookie = Cookies(actions)
    cookie.accept_cookies()
    
    search_page = SearchPage(actions)
    page_title = search_page.get_task_title()
    if page_title.lower().strip() != "vies vat number validation":
        raise Exception("SE: Title doesn't match")

    search_page.search_vat(vat_id, country)
    result_page = ResultPage(actions)
    vat_results = result_page.get_results()
    return vat_results