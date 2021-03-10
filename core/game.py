def valid(columns, rows, matrix, coordsA, coordsB):
    yA, xA = coordsA[0], coordsA[1]
    yB, xB = coordsB[0], coordsB[1]
    
    if 0 <= yA <= (rows - 1) and 0 <= xA <= 8 and 0 <= yB <= (rows - 1) and 0 <= xB <= 8:
        a = matrix[coordsA[0]][coordsA[1]]
        b = matrix[coordsB[0]][coordsB[1]]
        if a == None or b == None:
            return False

        if (a + b == 10) or (a == b):
            return True

    return False


def checkCondition(func):
    """
    Decorator to check if the two given numbers are a valid pair
    """
    def inner(self, coordsA, coordsB):
        yA, xA = coordsA[0], coordsA[1]
        yB, xB = coordsB[0], coordsB[1]
        
        if 0 <= yA <= (self.rows - 1) and 0 <= xA <= 8 and 0 <= yB <= (self.rows - 1) and 0 <= xB <= 8:
            a = self.matrix[coordsA[0]][coordsA[1]]
            b = self.matrix[coordsB[0]][coordsB[1]]
            if a == None or b == None:
                return False
            
            if (a + b == 10) or (a == b):
                print("The numbers are the same or their sum is ten")
                return func(self, coordsA, coordsB)

            else:
                print("Not a valid number pair")
                return
        else:
            print("Invalid Index")
            return

    return inner

class AI:
    def __init__(self):
        pass
    
    def noneBetweenPair(self, columns, rows, matrix, pair, pair2):
        pairDisplacementRow = pair2[0] - pair[0]
        pairDisplacementColumn = pair2[1] - pair[1]

        if(pairDisplacementRow == 0 and pairDisplacementColumn == 0):
            return False

        if(pairDisplacementRow != 0 and pairDisplacementColumn != 0):
            return False
        
        # Check if none beetween them
        # Check Top
        if(pairDisplacementRow > 0 and pairDisplacementColumn == 0):
            for i in range(1, pairDisplacementRow):
                if 0 <= pair[0]+i <= (rows - 1) and 0 <= pair[1] <= 8:
                    if(matrix[pair[0]+i][pair[1]] != None):
                        return False
            return True

        # Check Right
        if(pairDisplacementRow == 0 and pairDisplacementColumn > 0):
            for i in range(1, pairDisplacementColumn):
                if 0 <= pair[0] <= (rows - 1) and 0 <= pair[1]+i <= 8:
                    if(matrix[pair[0]][pair[1]+i] != None):
                        return False
            return True

        # Check Bot
        if(pairDisplacementRow < 0 and pairDisplacementColumn == 0):
            for i in range(1, abs(pairDisplacementRow)):
                if 0 <= pair2[0]+i <= (rows - 1) and 0 <= pair2[1] <= 8:
                    if(matrix[pair2[0]+i][pair2[1]] != None):
                        return False
            return True

         # Check Left
        if(pairDisplacementRow == 0 and pairDisplacementColumn < 0):
            for i in range(1, abs(pairDisplacementColumn)):
                if 0 <= pair2[0] <= (rows - 1) and 0 <= pair2[1]+i <= 8:
                    if(matrix[pair2[0]][pair2[1]+i] != None):
                        return False
            return True
        
        return True

    def getAllMoves(self, columns, rows, matrix):
        pairList = []
        for i in range(columns):
            for j in range(rows):
                pair = [j, i]
                for i2 in range(columns):
                    for j2 in range(rows):
                        pair2 = [j2, i2]

                        if(valid(columns, rows, matrix, pair, pair2) and self.noneBetweenPair(columns, rows, matrix, pair, pair2) and [pair2, pair] not in pairList):
                            pairList.append([pair, pair2])
        return pairList

class Game:
    """
    Game manager. Includes user actions
    """
    def __init__(self):
        # Number of moves 
        self.numMoves = 0

        self.columns = 9
        self.rows = 3   
        self.matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                        [1, 1, 1, 2, 1, 3, 1, 4, 1], 
                        [1, 1, 6, 1, 7, 1, 8, 1, 9]]

    def printGame(self):
        """
            Print the game board
        """
        print("Game Grid: ")
        for row in self.matrix:
            for element in row:
                if element != None:
                    print(element, end=" | ")
                else:
                    print(" ", end=" | ")
            print("\n", end="")
    
    @checkCondition
    def removePair(self, coordsA, coordsB):
        """
            0 <= row <= 2 
            0 <= column <= 8 
            coordsA -> [row, column] of digit A 
            coordsB -> [row, column] of digit B
        """
        # TO DO
        # same column with no other digits between them
        
        # No digits between them when scanning the grid from top to bottom, left to right. (right end wraps to left start, just one list)
        
        # Remove digits entries from table
        self.matrix[coordsA[0]][coordsA[1]] = None
        self.matrix[coordsB[0]][coordsB[1]] = None

    def deal(self):
        """
            All the remaining digits are readded to the end.
        """
        print("User/AI made a Deal!")
        # Create a matrix to append at the end filled with Null
        auxMatrix = [[None for i in range(9)] for i in range(self.rows)]

        # One dimension array of game matrix without Null elements 
        flattenMatrix = [element for row in self.matrix for element in row if element != None]

        for index, element in enumerate(flattenMatrix):
            row = index // 9
            column = index % 9
            auxMatrix[row][column] = element

        self.rows += 3
        self.matrix += auxMatrix

