from config import PAGE_LOAD_TIMEOUT

class MainPage:
    TASK_TITLE = "//h1[@data-testid='task-title']"

    def __init__(self, actions):
        self.actions = actions

    def get_task_title(self):
        return self.actions.read(self.TASK_TITLE,PAGE_LOAD_TIMEOUT)

