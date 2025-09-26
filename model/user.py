class User:
    def __init__(self, req : dict):
        data = req.get("message").get("chat")

        self.id = data.get("id")
        self.name = data.get("first_name") + " " + data.get("last_name")
    
    def getId(self):
        return self.id

    def getName(self):
        return self.name