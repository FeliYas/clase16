

class cadenatxt:
    def __init__(self, text):
        self.text = text

    def check_text(self):
        if not any(char.islower() for char in self.text) or not any(char.isupper() for char in self.text):
            raise ValueError("Error, debe contener mayuscula y minuscula")
