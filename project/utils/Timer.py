import time

class Timer():
    def __init__(self, initialTime = time.time()):
        self.initialTime = initialTime
    def executionTime(self):
        return ('%.2fs'%(time.time()-self.initialTime))