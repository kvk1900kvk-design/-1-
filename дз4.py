class МоваПрограмування:
    def __init__(self, імʼя):
        self.імʼя = імʼя

    def вивести_привітання(self):
        print(f"Привіт! Я мова програмування {self.імʼя}!")

class Python(МоваПрограмування):
    def __init__(self):
        super().__init__("Python")

class Java(МоваПрограмування):
    def __init__(self):
        super().__init__("Java")

class CPlusPlus(МоваПрограмування):
    def __init__(self):
        super().__init__("C++")