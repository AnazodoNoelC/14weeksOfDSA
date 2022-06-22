
class Time:
    def __init__(self,hours, minutes, seconds):
        if seconds > 59:
            sfactor = seconds // 60
            minutes += sfactor
            seconds -= sfactor * 60

        self._seconds = seconds
        if minutes > 59:
            mfactor = minutes // 60
            hours += mfactor
            minutes -= mfactor * 60

        self._minutes = minutes
        
        self._hours = hours
       
        

    def hours(self):
        return self._hours
    
    def minutes(self):
        return self._minutes

    def seconds(self):
        return self._seconds

    def _allInSeconds(self):
        InSeconds = self._hours * 3600 + self._minutes * 60 + self._seconds
        return InSeconds

    def numSeconds(self, otherTime):
        diff = self._allInSeconds() - otherTime._allInSeconds()
        return abs(diff)

    def isAM(self):
        if self._allInSeconds() <= 12 * 3600:
            return True
        return False
    
    def isPM(self):
        if self._allInSeconds() > 12 * 3600:
            return True
        return False
    
    def __gt__(self, otherTime):
        if self._allInSeconds() >  otherTime._allInSeconds():
            return True
        return False
    
    def __eq__(self, otherTime):
        if self._allInSeconds() == otherTime._allInSeconds():
            return True
        return False

    def __ge__(self, otherTime):
        if self >  otherTime or self ==  otherTime  :
            return True
        return False

    def __str__(self):
        return  "%2d:%2d:%2d" %( self.hours(), self.minutes(), self.seconds())


test = Time(12,3,0)
test2 = Time(11,0,131)

print(test2 )
