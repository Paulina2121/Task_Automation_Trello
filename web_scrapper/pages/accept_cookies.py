from selenium.common.exceptions import StaleElementReferenceException

class Cookies:
    ACCEPT_BUTTON = "//a[text()='Accept all cookies']"

    def __init__(self, actions):
        self.actions = actions

    def accept_cookies(self):
        for _ in range(3):
            try:
                self.actions.click(self.ACCEPT_BUTTON)
                return
            except StaleElementReferenceException:
                continue
            except:
                return
