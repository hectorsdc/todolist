class Item:
    def __init__(self, title):
        self.title = title
        self.desc = None
        self.status = False
    
    def __str__(self):
        if(self.desc != None):
            return f"{self.title}, {self.desc}"
        else:
            return f"{self.title}"

    