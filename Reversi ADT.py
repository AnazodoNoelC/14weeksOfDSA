from Array import Array2D

class Reversi():
    # Default Board Variables
    rows = 8 ; cols = 8;  b = ' B '; w = ' W ' ; clr =' * '

    #Constructor
    def __init__(self):
        self._whoseTurn = 1
        self.board = Array2D(8,8)
        self.movetype =[]           #Stores the direction of move(capture)
        self.moveEnd = dict()       #Stores the location where the capture ends with the move direction as key

        #Creates the initial board with blank squares
        for i in range(Reversi.rows):
            for j in range(Reversi.cols):
                self.board[i,j] = Reversi.clr
                self.config()       #Applies the initial configuration of reversi

    #stores the initial config    
    def config(self):
        self.board[3,3] = Reversi.w
        self.board[4,4] = Reversi.w
        self.board[3,4] = Reversi.b
        self.board[4,3] = Reversi.b

    #Prints out the textboard
    def textboard(self):
        boardtxt = list()
        for i in range(Reversi.rows):
            boardtxt.append([])
            for j in range(Reversi.cols):
                boardtxt[i].append(self.board[i,j])
            print(''.join(boardtxt[i]).center(50))

    #Returns whose turn to play        
    def whoseTurn(self):
        return self._whoseTurn       

    #Change Turns and returns whose turn to play
    def changeTurn(self):
        if self._whoseTurn == 1:
            self._whoseTurn = 2
        elif self._whoseTurn == 2:
            self._whoseTurn = 1
            
        return self._whoseTurn

    #Checks number of Owned by a player
    def numChips(self, player):
        assert player == 1 or player == 2, "Invalid Input, Enter 1 or 2"
        if player == 1:
            num = 0
            for i in range(Reversi.rows):
                for j in range(Reversi.cols):
                    if self.board[i,j] == Reversi.b:
                        num +=1
        else:
            num = 0
            for i in range(Reversi.rows):
                for j in range(Reversi.cols):
                    if self.board[i,j] == Reversi.w:
                        num +=1
        return num

    #Checks the number of Open Squares
    def numOpenSquares(self):
        num = 0
        for i in range(Reversi.rows):
                for j in range(Reversi.cols):
                    if self.board[i,j] == Reversi.clr:
                        num +=1
        return num

    """Verifies if the move is a legal move by checking a step in every direction around the location for an opponent's piece,
       Stores the move directions found and checks if the move forms a line of attack in at least one direction """
    def isLegalMove(self,row,col):
        if (row -1 in range(8) and col - 1 in range(8)) and self.board[row -1, col-1] == self._opposite():
                self.movetype.append('top-left')
        if (row -1 in range(8) and col in range(8)) and self.board[row -1, col] == self._opposite():
                self.movetype.append('up')
        if (row -1 in range(8) and col + 1 in range(8)) and self.board[row -1, col+1] == self._opposite():
                self.movetype.append('top-right')
        if (row  in range(8) and col - 1 in range(8))and self.board[row, col-1] == self._opposite():
                self.movetype.append('left')
        if (row  in range(8) and col + 1 in range(8)) and self.board[row , col+1] == self._opposite():
                self.movetype.append('right')
        
        if (row + 1  in range(8) and col - 1 in range(8)) and self.board[row+1, col-1] == self._opposite():
                self.movetype.append('bottom-left')
        if (row + 1  in range(8) and col  in range(8)) and self.board[row + 1, col] == self._opposite():
                self.movetype.append('down')
        if (row + 1  in range(8) and col + 1 in range(8))and self.board[row + 1, col+1] == self._opposite():
                self.movetype.append('bottom-right')
        
        
        if len(self.movetype) == 0:
            return False
        else :
            return self.lineOfAttack(row,col)

    """Stores the factors to be used in multiplying row and col variables, depending on the move direction"""
    def position(self, var):
        i = var
        if i == 'top-left':
            a = -1; b= -1
        elif i == 'up':
            a = -1; b= 0
        elif i == 'top-right':
            a = -1; b= 1
        elif i == 'left':
            a = 0; b= -1
        elif i == 'right':
            a = 0; b= 1
        elif i == 'bottom-left':
            a = 1; b= -1
        elif i == 'down':
            a = 1; b= 0
        elif i == 'bottom-right':
            a = 1; b= 1

        return a,b

    #Verifies that a line of attack can be formed
    def lineOfAttack(self, row, col):
        assert self.board[row,col] == Reversi.clr, 'Position is occupied'
        status = False
        for i in self.movetype:
            valid = 0
            a,b = self.position(i)      #Retrieves the factors for that move direction
            for c in range(2,8):        #checks along that direction (using the factors) starting from after the immediate neighbour
                nnrow = row + (c*a)     
                nncol = col+ (c*b)
                if nnrow in range(8) and nncol in range(8):         #Ensures Valid board location
                    if self.board[nnrow, nncol] ==  Reversi.clr:    #Ensures that moves are not made over blank locations
                        break
                    if self.board[nnrow, nncol] == self._same():    #Ends the move at the first same colored chip
                        self.moveEnd[i] = (nnrow,nncol)             #Stores the End move location
                        valid = 1
                        status = True
                        break
                        
            if valid ==  0:             #If the value of valid doesn't change during the iteration, then no line of attack was formed
                self.moveEnd[i] = 0

        return status        
        
        

    
    #Makes the move(s) after verifying the move is legal
    def makeMove(self,row,col):
        assert self.isLegalMove(row,col), 'Invalid Move!'
        self.board[row, col] = self._same()

        for i in self.movetype:
            if self.moveEnd[i] == 0:    #Ignores moves with no end move location
                continue

            a,b = self.position(i)      #Retrieves factors for that location
            endA =  self.moveEnd[i][0]  
            endB =  self.moveEnd[i][1]
            nnrow = row; nncol = col
            c = 1
            while nnrow != endA or nncol != endB:       #Loop continues while end locations have not been reached
                nnrow = row + (c*a)
                nncol = col+ (c*b)
                self.board[nnrow, nncol] = self._same()     #changes  the chips along the direction to the players colour
                c +=1
                

    #retrieves whose turn and returns the corresponding chip  
    def _same (self):
        player = self._whoseTurn
        if player == 1:
            return Reversi.b
        else:
            return Reversi.w

    #retrieves whose turn and returns the opposite chip  
    def _opposite (self):
        player = self._whoseTurn
        if player == 1:
            return Reversi.w
        else:
            return Reversi.b

    #Returns the winner, given that all the locations are occupied.
    def getWinner(self):
        if self.numOpenSquares() == 0:
            if self.numChips(1) < self.numChips(2):
                return 1
            elif self.numChips(1) > self.numChips(2):
                return 2
            else: 
                return 3
        else:
            return 0

    #Reset Movetype and moveend after each player has played
    def refresh(self):
        self.movetype =[]
        self.moveEnd = dict()
        

def main():
    print('Welcome to the Reversi Game')
    print('Player 1 to play \n Enter your move in the form (row,col)')

    game = Reversi()
    game.textboard()
    
    while True: 
        plInput = input()
        if plInput !=  'Pass':  
           
                move = list(plInput)
                row  = int(move[0])
                col = int(move[2])
                if len(move) == 3 and move[1] ==',':
                    try:
                        game.isLegalMove(row,col)
                    except:
                            #Ensures a valid move is played without affecting players turn or raising error by restarting loop
                            game.isLegalMove(row,col)
                            print('Invalid Move!\n Make sure your move is valid ')
                            continue
                else:
                    #Ensures a valid move is played without affecting players turn or raising error by restarting loop
                    print('Invalid move !\n  Enter your move in the form (row,col)')
                    continue

                row  = int(move[0])
                col = int(move[2])
                game.makeMove(row,col)
                game.textboard()
                if game.getWinner() != 0:
                    break
                print('Player ' + str(game.changeTurn())+ ' to play')
                game.refresh()
                
                #refreshes the checkGameState, thereby, preventing the game from ending when the game hasn't been passed two consecutive times
                checkGameState = dict() 
                
            
        else:
            print('Current Player passes \n Play continues with the next player')
            checkGameState = dict()
            checkGameState[game.whoseTurn] = 'Pass' #Stores which player has passed
            game.changeTurn()
            
        
        if len(checkGameState) == 2:     #if both players have no valid moves consecutively (both players passed), the game ends
            break
        
    print('Game Over!')
    if game.numChips(1) > game.numChips(2):
        print('Player 1 wins!')
    elif game.numChips(2) > game.numChips(2):
        print('Player 2 wins!')      


main()
        
        


    

