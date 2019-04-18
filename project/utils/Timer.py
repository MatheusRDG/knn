import time

class timer():
    def __init__(self, initialTime = time.time()):
        self.initialTime = initialTime
    def executionTime(self):
        return time.time()-self.initialTime