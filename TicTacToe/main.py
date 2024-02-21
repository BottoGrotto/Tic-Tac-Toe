import os, random

grid: list = [[
                "¹", "²", "³"
                ],
              [
                "═", "═", "═"
                ],
              [
                "⁴", "⁵", "⁶"
                ],
              [
                "═", "═", "═"
                ],
              [
                "⁷", "⁸", "⁹"
                ],]

def printPlayer(player) -> None:
    print(f"{player}'s turn!")

def printOutGrid(list: list) -> None:
    output = ""
    for r, row in enumerate(grid):
        for c, col in enumerate(grid[r]):
            if grid[r][c] != "═" and c != 0:
                
                output += "║" + grid[r][c]
            elif c == 0:
                output += " " + grid[r][c]
            else: 
                output += "╬" + grid[r][c]
        if grid[r][c] != "═":
            if r < 4:
                output += "\n"
        else:
            output += "\n"
    print(output)

def updateGrid(userInput: int, userType: str) -> bool:
    pos = 1
    for r, row in enumerate(grid):
        for c, col in enumerate(grid[r]):
            state = grid[r][c]
            if state != "═":
                pos += 1
                if userInput == pos-1 and grid[r][c] != "X" and grid[r][c] != "O":
                    grid[r][c] = userType
                    os.system("cls")
                    return True
                elif userInput == pos-1 and grid[r][c] == "X" and grid[r][c] == "O":
                    os.system("cls")
                    return False
                else:
                    os.system("cls") 

def findRemaining() -> list:
    listToReturn = []
    count = 0
    for r, row in enumerate(grid):
        for c, col in enumerate(grid[r]):
            state = grid[r][c]
            if state != "═" and state != "X" and state != "O":
                count += 1
                listToReturn.append(count)
            elif state == "X" or state == "O": 
                count += 1
    return listToReturn

def checkUserInput(userInput: int) -> bool:
    listToLoop = findRemaining()
    for num in listToLoop:
        if userInput == num or userInput >= listToLoop[-1]:
            return True
    return False

def printEssentials(player, grid) -> None:
    printPlayer(player)
    printOutGrid(grid)

def updateTurns(stata, player, user1Name, user2Name, userType, user1Type, user2Type) -> None:
    if stata == True:
        if player == user1Name:
            player = user2Name
            userType = user2Type
            return [player, userType]
        else: 
            player = user1Name
            userType = user1Type 
            return [player, userType]
    else:
        return [player, userType]
#  1 1 1
#  = = =
#  1 1 1
#  = = =
#  1 1 1
# def checkWin() -> bool:
#     if grid[0][0] == grid[2][1] and grid[4][2] == grid[2][1]:
#         winnerType = grid[0][0]
#         return [winnerType, True]
#     elif grid[0][2] == grid[2][1] and grid[4][0] == grid[2][1]:
#         winnerType = grid[0][2]
#         return [winnerType, True]
#     for c in grid:
#         if grid[0][c] == grid[1][c] and grid[1][c] == grid[1][c]:
#             winnerType = grid[0][0]
#             return [winnerType, True]
#     return ["", False]        
    
userInput = ""
userType = "X"
gameState = 1
player = ""
winnerType = "X"
stata = True
os.system("cls")
if __name__ == "__main__":
    while userInput != "stop":
        if gameState == 1:
            user1Name = input("User 1's Name: ")
            user2Name = input("User 2's Name: ")
            if user2Name == user1Name:
                user2Name += " 2"
            randomUser = random.randint(1,2)
            if randomUser == 1:
                player = user1Name
                user1Type = "X"
                user2Type = "O"
            else:
                player = user2Name
                user2Type = "X"
                user1Type = "O"

            os.system("cls")
            gameState = 2

        if gameState == 2:
            os.system("cls")
            printEssentials(player, grid)
            userInput = input("Choose place to switch: ")
            if userInput == "stop":
                break

            didSomeonePutAStr = userInput.isnumeric()
            while didSomeonePutAStr != True:
                userInput = input("Please input a number!: ")
                didSomeonePutAStr = userInput.isnumeric()
                stata = updateGrid(userInput=int(userInput), userType=userType)
                os.system("cls")
                playerUserType = updateTurns(stata=stata, player=player,user1Name=user1Name, user2Name=user2Name, userType=userType, user1Type=user1Type, user2Type=user2Type)
                player = playerUserType[0]
                userType = playerUserType[1]
                printEssentials(player, grid)
            
            didSomeonePutAStr = userInput.isnumeric()
            while didSomeonePutAStr:
                userInput = int(userInput)
                stata = updateGrid(userInput, userType=userType)
                if (userInput > 9):
                    theChecker = checkUserInput(int(userInput))
                    while theChecker == True:
                        printEssentials(player, grid)
                        userInput = input(f"Please input any of these numbers:| {findRemaining()} |: ")
                        if str(userInput).isnumeric():
                            stata = updateGrid(userInput=userInput, userType=userType)
                            theChecker = False
                        else:
                            while userInput.isnumeric() == False:
                                userInput = input("Please input a number!: ")
                            if userInput.isnumeric() == True:
                                stata = updateGrid(userInput=int(userInput), userType=userType)
                                playerUserType = updateTurns(stata=stata, player=player,user1Name=user1Name, user2Name=user2Name, userType=userType, user1Type=user1Type, user2Type=user2Type)
                                player = playerUserType[0]
                                userType = playerUserType[1]
                else:
                    didSomeonePutAStr = False
            
            playerUserType = updateTurns(stata=stata, player=player,user1Name=user1Name, user2Name=user2Name, userType=userType, user1Type=user1Type, user2Type=user2Type)
            player = playerUserType[0]
            userType = playerUserType[1]
        if gameState == 3:
            print("WooHoo!") 