
class BigInteger():

    #Constructor
    def __init__(self, value = 0) -> None:
        self._value = list(str(value))

    #Represents the BigInteger as a string
    def __str__(self) -> str:
        return ''.join(self._value)
    
    #Overloads the '==' operator.
    def __eq__(self,otherBigInt):
        if len(self._value) > len(otherBigInt._value):
            return False
        elif len(self._value) < len(otherBigInt._value):
            return False
        else:
            #After verifying equal lengths, Compare the individual integers
            i = 0
            while i < len(self._value):
                if int(self._value[i]) > int(otherBigInt._value[i]):
                    return False
                elif int(self._value[i]) < int(otherBigInt._value[i]):
                    return False
                else:
                    i+=1
        
        return True
    
    #Overloads the '>' operator
    def __gt__(self, otherBigInt):
        #Compare the lengths of the values
        if len(self._value) > len(otherBigInt._value):  
            return True
        elif len(self._value) < len(otherBigInt._value):
            return False
        else:
            #If lengths are equal, Compare the individual integers 
            i = 0
            while i < len(self._value):
                if int(self._value[i]) > int(otherBigInt._value[i]):
                    return True
                elif int(self._value[i]) < int(otherBigInt._value[i]):
                    return False
                else:
                    i+=1
    
    #Overloads the '>=' operator
    def __ge__(self, otherBigInt):
        if self.__gt__(otherBigInt)  or self.__eq__(otherBigInt) :
            return True
        else:
            return False

    #Helper Method that removes the first value (the main aim was the '-' in negative values) in a BigInteger Object
    def _pop(self):
        temp = self._value
        temp.pop(0)
        temp = BigInteger(''.join(temp))
        return temp
    
    #Helper Method that returns a BigInteger object as a single number
    def _int(self):
        bigInt = 0
        i = len(self._value) - 1
        pos = 0
        while i >= 0:
            bigInt += int(self._value[i]) * (10**pos)
            i-=1
            pos+=1
        return bigInt

    #Helper method that inserts a negative sign in front of a BigInteger Object
    def _negate(self):
        temp = self._value
        temp.insert(0,'-')
        temp = BigInteger(''.join(temp))
        return temp

    #Overloads the '+' operator
    def __add__(self, otherBigInt):
        x = len(self._value)-1
        y = len(otherBigInt._value)-1
        newNum = []
        rem = 0 

        #Checks for special cases where one or both of the  values are negative
        if self._value[0] == '-' and otherBigInt._value[0] != '-':
            return otherBigInt - self._pop()
        elif self._value[0] != '-' and otherBigInt._value[0] == '-':
            return self - otherBigInt._pop()
        elif self._value[0] == '-' and otherBigInt._value[0] == '-':
            tempInt = BigInteger(self._pop() + otherBigInt._pop())
            return tempInt._negate()

        #Loops through each BigInteger from the end to the beginning of the smallest BigInteger
        while x >= 0 and y >=0:
            unit = int(self._value[x]) + int(otherBigInt._value[y]) + rem
            rem = 0     #Resets the remainder variable
            if unit > 9:    
                unit -= 10
                rem = 1
            if len(newNum) == 0:
                newNum.append(str(unit))
            else: 
                newNum.insert(0,str(unit))
            
            x-=1; y-=1
        
        #If digits from 'Self' BigInteger remains, insert them also
        while x >= 0 :
            unit = int(self._value[x]) + rem
            newNum.insert(0,str(unit))
            rem = 0
            x-=1
        
        #If digits from 'otherBigInteger' BigInteger remains, insert them also
        while y >= 0 :
            unit = int(otherBigInt._value[y]) + rem
            newNum.insert(0,str(unit))
            rem = 0
            y-=1
        
        #If there's any remainder, insert it as well
        if rem != 0:
            newNum.insert(0,str(rem))

        newNum = ''.join(newNum)
        newNum = BigInteger(newNum)

        return newNum
        
    #Oveloads the '-' operator
    def __sub__(self, otherBigInt):
        x = len(self._value)-1
        y = len(otherBigInt._value)-1
        newNum = []
        rem = 0 
        
        #Checks for special cases where one or both of the  values are negative
        if self._value[0] == '-' and otherBigInt._value[0] != '-':
            tempInt = BigInteger(otherBigInt + self._pop())
            return tempInt._negate()
            
        elif self._value[0] != '-' and otherBigInt._value[0] == '-':
            return self + otherBigInt._pop()
        elif self._value[0] == '-' and otherBigInt._value[0] == '-':
            return otherBigInt._pop() + self

        #Loops through each BigInteger from the end to the beginning of the smallest BigInteger
        while x >= 0 and y >=0:
            unit = int(self._value[x]) - int(otherBigInt._value[y]) - rem
            rem = 0     #Resets the remainder variable
            if unit < 0:
                if x != 0 :
                    unit += 10
                    rem = 1
            if len(newNum) == 0:
                newNum.append(str(unit))
            else: 
                newNum.insert(0,str(unit))
            
            x-=1; y-=1
        
        #If digits from 'Self' BigInteger remains, insert them also
        while x >= 0 :
            unit = int(self._value[x]) - rem
            newNum.insert(0,str(unit))
            rem = 0
            x-=1
        #If digits from 'otherBigInteger' BigInteger remains, insert them also
        while y >= 0 :
            unit = -int(otherBigInt._value[y])
            newNum[0] = str(abs(int(newNum[0])))
            newNum.insert(0,str(unit))
            y-=1
        
        newNum = ''.join(newNum)
        newNum = BigInteger(newNum)

        return newNum

    #Overloads the '*' operator           
    def __mul__(self, otherBigInt):
        #This uses basic muliplication where the value to be multiplied (self) 
        # #is muliplied by each digit from the 'multiplier'(otherBigInt)
        #The results from each digit multiplication is then summed up
        
        y = len(otherBigInt._value)-1
        rem = 0
        pos = 0 

        #Checks for special cases where one or both of the  values are negative
        if self._value[0] == '-' and otherBigInt._value[0] != '-':
            tempInt = BigInteger(otherBigInt * self._pop())
            return tempInt._negate()
            
        elif self._value[0] != '-' and otherBigInt._value[0] == '-':
            tempInt = BigInteger(otherBigInt._pop() * self)
            return tempInt._negate()
        elif self._value[0] == '-' and otherBigInt._value[0] == '-':
            return otherBigInt._pop() * self._pop()

        newNum= []

        #Loops through otherBigInt digits. 
        while y>= 0:
            newNum.append([])  
            x = len(self._value)-1

            #Loop through 'self' BigInteger digits, multiplying each of them by  the current otherBigInt digit
            while x >= 0:
                unit = (int(self._value[x]) * int(otherBigInt._value [y])) + rem
                rem = 0
                if unit > 9:
                    rem =  unit // 10
                    unit %= 10
                    
                if len(newNum) == 0: 
                    newNum[-1].append(str(unit))
                else: 
                    newNum[-1].insert(0,str(unit))
                
                x-=1
            
            if rem != 0:
                newNum[-1].insert(0,str(rem))
                rem = 0

            i = 0
            
            while i < pos: #Appends zeros depending on the position otherBigInt digit
                newNum[-1].append(str(0)) 
                i+=1

            #Joins the list the list together and stores it as a BigInteger object in newNum
            temp= ''.join(newNum[-1])
            newNum[-1] = BigInteger(temp)
            pos +=1
            y-=1
        
        tempBigInt = BigInteger()

        #Sums up all the answers stored in newNum and returns the value
        for i in range(len(newNum)):
            tempBigInt += newNum[i]
        
        return tempBigInt

    #Helper Method for __floordiv__ and __mod__ methods
    def _division(self, otherBigInt):
        tempList = []
        rem = 0
        divisor = otherBigInt._int() 
        
        #This loop uses the long division method to arrive at the answer
        #The answer is a list containing the quotient(to be returned to the __floordiv__ method)
        #and a remainder( to be returned to the __mod__ method)
        for  i in range(len(self._value)):
            dividend = (10 * rem + int(self._value[i]))
            quotient  = dividend // divisor
            rem = dividend - (quotient * divisor)
            if len(tempList) != 0 or quotient!=0:   #Prevents zeros in front of the number e.g 00030
                tempList.append(str(quotient))
        result = [''.join(tempList),rem]
        return result
    
    #Overloads the '//' operator
    def __floordiv__(self,otherBigInt):

        #Checks for special cases where one or both of the  values are negative
        #The logic for negative integer division follows default Python negative integer division logic
        if self._value[0] == '-' and otherBigInt._value[0] != '-':
            tempInt = BigInteger(self._pop() // otherBigInt ) + BigInteger(1)
            return tempInt._negate()
            
        elif self._value[0] != '-' and otherBigInt._value[0] == '-':
            tempInt = BigInteger(self // otherBigInt._pop()) + BigInteger(1)
            return tempInt._negate()
        elif self._value[0] == '-' and otherBigInt._value[0] == '-':
            return  self._pop() // otherBigInt._pop()


        solution = self._division(otherBigInt)
        solution = BigInteger(solution[0])
        return  solution
    
    #Overloads the '%' operator
    def __mod__(self,otherBigInt):

        #Checks for special cases where one or both of the  values are negative
        #The logic for negative modulus follows default Python negative modulus logic
        if self._value[0] == '-' and otherBigInt._value[0] != '-':
            tempInt = BigInteger(self._pop() % otherBigInt )
            return otherBigInt + tempInt._negate()
            
        elif self._value[0] != '-' and otherBigInt._value[0] == '-':
            tempInt = BigInteger(self % otherBigInt._pop() )
            return (otherBigInt + tempInt._negate())._negate()
        elif self._value[0] == '-' and otherBigInt._value[0] == '-':
            return (self._pop() % otherBigInt._pop())._negate()

        solution = self._division(otherBigInt)
        solution = BigInteger(solution[1])
        return  solution

    #Overloads the '**' operator
    def __pow__(self, otherBigInt):
        #Checks for special cases where one or both of the  values are negative
        if self._value[0] == '-' and otherBigInt._value[0] != '-':
            return self._pop() ** otherBigInt 
            
        elif self._value[0] != '-' and otherBigInt._value[0] == '-':
            tempInt = (self ** otherBigInt._pop())._int()
            return 1/tempInt
        elif self._value[0] == '-' and otherBigInt._value[0] == '-':
            return  self._pop() ** otherBigInt

        tempInt = BigInteger(1)
        i = 0
        while i < otherBigInt._int():
            tempInt *= self
            i+=1
        return tempInt


test = BigInteger(-2)
test2 =BigInteger(27908)
test3 = BigInteger(392)
test4 = BigInteger(-10)
print((test4 ** test))