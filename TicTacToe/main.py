import os, random, time

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

def updateGrid(player: str, userInput: int, userType: str) -> bool:
    pos = 1
    for r, row in enumerate(grid):
        for c, col in enumerate(grid[r]):
            state = grid[r][c]
            if state != "═":
                pos += 1
                if userInput == pos-1 and grid[r][c] != "X" and grid[r][c] != "O":
                    grid[r][c] = userType
                    os.system("clear")
                    return True
                elif userInput == pos-1 and grid[r][c] == "X" and grid[r][c] == "O":
                    os.system("clear")
                    printEssentials(player, grid)
                    inputCheckerOut = BadInputChecker(player, userType)
                    # stata = inputCheckerOut[0]
                    userInput = inputCheckerOut[1]
                    player = inputCheckerOut[2][0]
                    userType = inputCheckerOut[2][1]
                    
                    return False
                else:
                    os.system("clear") 
    

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

def updateTurns(stata: bool, player: str, user1Name: str, user2Name: str, userType: str, user1Type: str, user2Type: str) -> list:
    """Switches who the player that is going to be displayed and their type based on who just went"""
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
    

def updateTheData(player: str, user1Name: str, user2Name: str, userType: str, user1Type: str, user2Type: str, userInput: int) -> list:
    stata = updateGrid(player, userInput=userInput, userType=userType)
    return updateTurns(stata, player, user1Name, user2Name, userType, user1Type, user2Type)

def BadInputChecker(player: str, userType: str) -> list:
    """Tells user to input a number of one of the remaining slots"""
    theChecker = True
    while theChecker == True:
        os.system("clear")
        printEssentials(player, grid)
        userInput = input(f"Please input any of these numbers:| {findRemaining()} |: ")
        if str(userInput).isnumeric():
            # print("Woah now")
            if checkUserInput(int(userInput)) == True:
                # print("Print this")
                # time.sleep(3)
                stata = updateGrid(player, userInput, userType)
                playerUserType = updateTheData(player, user1Name, user2Name, userType, user1Type, user2Type, int(userInput))
                theChecker = False
        # else:
        #     while userInput.isnumeric() == False:
        #         userInput = input("Please input a real number!: ")
                # if userInput.isnumeric() == True:
                #     print("This is a test")
                #     time.sleep(4)
                #     playerUserType = updateTheData(player, user1Name, user2Name, userType, user1Type, user2Type, int(userInput))
                   
                    
                    # player = playerUserType[0]
                    # userType = playerUserType[1]
    # os.system("clear")
    
    return [stata, userInput, playerUserType]
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
os.system("clear")
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

            os.system("clear")
            gameState = 2
        
        if gameState == 2:
            os.system("clear")
            printEssentials(player, grid)
            userInput = input(f"Input any of these numbers:| {findRemaining()} |: ")
            if userInput == "stop":
                break

            didSomeonePutAStr = userInput.isnumeric()
            while didSomeonePutAStr != True:
                os.system("clear")
                printEssentials(player, grid)
                print("WOOOO")
                time.sleep(2)
                userInput = input(f"Please input any of these numbers:| {findRemaining()} |: ")
                didSomeonePutAStr = userInput.isnumeric()
                if didSomeonePutAStr:
                    stata = updateGrid(player, userInput=int(userInput), userType=userType)
                os.system("clear")
                inputCheckerOut = BadInputChecker(player, userType)
                stata = inputCheckerOut[0]
                userInput = inputCheckerOut[1]
                player = inputCheckerOut[2][0]
                userType = inputCheckerOut[2][1]
            
            didSomeonePutAStr = userInput.isnumeric()
            while didSomeonePutAStr:
                userInput = int(userInput)
                stata = updateGrid(player, userInput, userType=userType)
                if (userInput > 9):
                    inputCheckerOut = BadInputChecker(player, userType)
                    stata = inputCheckerOut[0]
                    userInput = inputCheckerOut[1]
                    player = inputCheckerOut[2][0]
                    userType = inputCheckerOut[2][1]          
                else:
                    didSomeonePutAStr = False

            playerUserType = updateTurns(stata=stata, player=player,user1Name=user1Name, user2Name=user2Name, userType=userType, user1Type=user1Type, user2Type=user2Type)
            player = playerUserType[0]
            userType = playerUserType[1]
        if gameState == 3:
            print("WooHoo!") 