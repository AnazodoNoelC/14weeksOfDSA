class Fraction:
    # Constructor:
    def __init__(self, deciOrNum, denom =0) -> None:
        '''If a single value is passed, it stores it as a decimal or 
           floatting point value and it converts it to a fraction.
           If two values are passed it is stored as a fraction'''
        
        #For fractions
        if  denom != 0:
            if deciOrNum != 0:    
                self._raw = [deciOrNum,denom]
                self._fraction = self.simplify()
                self._float = self.toFloat()
            
            #0 over any number (0/denom) remains stored as 0
            else:
                self._fraction = 0
                self._float = 0

        #For Decimals
        else:
            self._float = float(deciOrNum)
            #self._fraction = None
            self._fraction = self.toFraction()
            
    '''if it's already a float it returns the float back, 
       else it converts from fraction to float'''        
    def toFloat(self):
        try:
            return self._float
            
        except: 
            self._float = self._fraction[0]/self._fraction[1]
            return self._float
        
    '''if it's already a fraction it returns the fraction back, 
       else it converts from float to fraction'''
    def toFraction(self):
        try:
            return self.simplify()
        
        except:
            i = str(self._float).split('.')
            denom = 10 ** (len(i[1]))
            num = int(i[1]) + int(i[0]) * denom
            self._raw = [num, denom]
            return self.simplify()
        

   
    #In Summary, (a/b + c/d == (ad +cb)/bd ); overloads the '+' operator
    def __add__(self, otherFrac):
        nnum = self._fraction[0]*otherFrac._fraction[1] +  self._fraction[1]*otherFrac._fraction[0]
        ndenom = self._fraction[1]*otherFrac._fraction[1]
        newFrac = Fraction(deciOrNum= nnum, denom = ndenom)
        newFrac.simplify()
        return newFrac
    
    #Simply put, (a/b - c/d == (ad - cb)/bd ); overloads the '-' operator  
    def __sub__(self, otherFrac):
        nnum = self._fraction[0]*otherFrac._fraction[1] - self._fraction[1]*otherFrac._fraction[0]
        ndenom = self._fraction[1]*otherFrac._fraction[1]
        newFrac = Fraction(deciOrNum= nnum, denom = ndenom)
        newFrac.simplify()
        return newFrac
    
    #Simply put, (a/b * c/d == ac/bd ); overloads the '*' operator
    def __mul__(self, otherFrac):
        nnum = self._fraction[0]*otherFrac._fraction[0]
        ndenom = self._fraction[1]*otherFrac._fraction[1]
        newFrac = Fraction(deciOrNum= nnum, denom = ndenom)
        newFrac.simplify()
        return newFrac

    #Simply put, [(a/b)/ (c/d) == a/b * d/c == ad/bc ); overloads the '/' operator
    def __truediv__(self, otherFrac):
        nnum = self._fraction[0]*otherFrac._fraction[1]
        ndenom = self._fraction[1]*otherFrac._fraction[0]
        newFrac = Fraction(deciOrNum= nnum, denom = ndenom)
        newFrac.simplify()
        return newFrac

    #reduces fractions to its lowest possible form
    def simplify(self):
        deciOrNum = self._raw[0]
        denom = self._raw[1]
        
        state1, state2 = 0,1
        while state1 != state2:
            state1 = [deciOrNum,denom]
            for i in range (2, int(denom)+1):
                if deciOrNum % i == 0 and denom% i == 0:
                    deciOrNum = int(deciOrNum/i)
                    denom = int(denom/i)
                    break
            
            state2 = [deciOrNum,denom]
        
        return [deciOrNum,denom] 
    
    #overloads the '>' operator
    def __gt__(self, otherFrac):
        if otherFrac._fraction[1] == self._fraction[1]:
            return self._fraction[0] > otherFrac._fraction[0]
        
        else:
            return self._fraction[0]*otherFrac._fraction[1] > self._fraction[1]*otherFrac._fraction[0]
        
    #overloads the '>=' operator
    def __ge__(self, otherFrac):
        if otherFrac._fraction[1] == self._fraction[1]:
            return self._fraction[0] >= otherFrac._fraction[0]
        
        else:
            return self._fraction[0]*otherFrac._fraction[1] >= self._fraction[1]*otherFrac._fraction[0]
        
    #overloads the '==' operator    
    def __eq__(self, otherFrac):
        if otherFrac._fraction[1] == self._fraction[1]:
            return self._fraction[0] == otherFrac._fraction[0]
        
        else:
            return self._fraction[0]*otherFrac._fraction[1] == self._fraction[1]*otherFrac._fraction[0]
    
    #overloads the str() funtion, and displays it in the form a/b
    def __str__(self) -> str:
        if self._fraction == 0:
            return '0'
        elif self._fraction[1] == 1:
            return "%d" %(self._fraction[0])
        else:
            return "%d / %d" %(self._fraction[0],self._fraction[1])
