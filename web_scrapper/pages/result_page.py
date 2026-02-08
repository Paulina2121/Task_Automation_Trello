class ResultPage:
    RESULT_TEXT = "//span[@data-testid='textResult']"
    NAME_TEXT = "//td[@data-testid='name']"
    ADDRESS_TEXT = "//td[@data-testid='address']"
    
    results = {
        "result":"",
        "name":"",
        "address":""
    }

    def __init__(self, actions):
        self.actions = actions


    def get_results(self):
        self.results["result"] = self.actions.read(self.RESULT_TEXT)
        self.results["name"] = self.actions.read(self.NAME_TEXT)
        self.results["address"] = self.actions.read(self.ADDRESS_TEXT)

        return self.results


