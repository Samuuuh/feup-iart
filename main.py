import copy
import time
from _collections import deque

 # Personal Libraries
from core.game import Game
from core.ai import Ai

def breathFirstSearch():
    """
        Breath First Search Algorithm
    """

    gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                1, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9]
    columns = 9
    rows = 3   
    
    game = Game(0, rows, columns, gameState)
    ai = Ai()
    # rows, columns, gameState = deal(rows, columns, gameState.copy())
    # Double Ended Queue to allow O(1) pop and append
    # Set to check if an element was already visited in O(1)
    queue = deque([game])
    visited = set()

    start = time.time()
    while True:
        if (len(visited) % 10000 == 0):
            print("Visited: {} Remaining: {}".format(len(visited), len(queue)))
        
        # Next GameState
        game = queue.popleft()

        # Found a solution [Empty Matrix]
        if game.isEmpty():
            print("Found a solution: ")
            print("Total Moves: {}".format(game.moves))
            break
        # GameState Already Visited
        elif repr(game.matrix) in visited:
            pass
        # Get available moves and add them to the queue
        else:
            visited.add(repr(game.matrix))
            append = queue.append

            operationList = ai.getAllMoves(game.rows, game.columns, game.matrix)
            newGameMoves = game.moves + 1
            for operation in operationList:
                newGame = Game(newGameMoves, game.rows, game.columns, game.matrix.copy())
                newGame.removePair(operation[0], operation[1])
                append(newGame)
            
            rowsDeal, columnsDeal, gameStateDeal = game.deal(game.rows, game.columns, game.matrix.copy())
            
            gameDeal = Game(game.moves, rowsDeal, columnsDeal, gameStateDeal)

            if rowsDeal < 7:
                append(gameDeal)

    end = time.time()
    print("Time elapsed: {}".format(end - start))


def depthFirstSearch():
    """
        Depth First Search Algorithm
    """
    gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                1, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9,]
    columns = 9
    rows = 3 
    
    game = Game(0, rows, columns, gameState)
    game.printGame()

    ai = Ai()
    # rows, columns, gameState = deal(rows, columns, gameState.copy())
    # Double Ended Queue to allow O(1) pop and append
    # Set to check if an element was already visited in O(1)
    queue = deque([game])
    visited = set()

    start = time.time()
    while True:
        if (len(visited) % 10000 == 0):
            print("Visited: {} Remaining: {}".format(len(visited), len(queue)))
        
        # Next GameState
        game = queue.pop()
        #game.printGame()

        # Found a solution [Empty Matrix]
        if game.isEmpty():
            print("Found a solution: ")
            print("Total Moves: {}".format(game.moves))
            break
        # GameState Already Visited
        elif repr(game.matrix) in visited:
            pass
        # Get available moves and add them to the queue
        else:
            visited.add(repr(game.matrix))
            append = queue.append

            operationList = ai.getAllMoves(game.rows, game.columns, game.matrix)
            #removePair = game.removePair

            newGameMoves = game.moves + 1
            for operation in operationList:
                newGame = Game(newGameMoves, game.rows, game.columns, game.matrix.copy())
                newGame.removePair(operation[0], operation[1])
                append(newGame)
            
            rowsDeal, columnsDeal, gameStateDeal = game.deal(game.rows, game.columns, game.matrix.copy())
            gameDeal = Game(game.moves, rowsDeal, columnsDeal, gameStateDeal)

            if rowsDeal < 7:
                queue.appendleft(gameDeal)

    end = time.time()
    print("Time elapsed: {}".format(end - start))

if __name__ == "__main__":
    depthFirstSearch()

    
