from time import time

class Stoparica:
    def __init__(self):
        self.zacetek = time()

    def cas(self):
        return time() - self.zacetek