class SearchPage:
    ID_CBX = "//select[@id='select-country']"
    COUNTRY_INPUT = "//input[@formcontrolname='vatNumber']"
    VERIFY_BUTTON = "//button[@data-testid='verifyBtn']//span[text()='Verify']"
    TASK_TITLE = "//h1[@data-testid='title']"

    def __init__(self, actions):
        self.actions = actions

    def get_task_title(self):
        return self.actions.read(self.TASK_TITLE)

    def search_vat(self, vat_id, country):
        self.actions.select(self.ID_CBX, country)
        self.actions.write(self.COUNTRY_INPUT, vat_id)
        self.actions.click(self.VERIFY_BUTTON)
