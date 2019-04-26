import time
from datetime import datetime
class Timer():
    def __init__(self, initialTime = time.time()):
        self.initialTime = initialTime
    def executionTime(self):
        return ('%.2fs'%(time.time()-self.initialTime))
    def tenMinutesFlag(self):
        return (time.time()-self.initialTime)/600
    def timerReset(self):
        self.initialTime = time.time()
    def timeNow(self):
        now = datetime.now()
        return ("%d:%d:%d"%(now.hour,now.minute,now.second))