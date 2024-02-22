import os, random, time, platform
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"blue": "blue", "green": "green", "red": "red", "purple": "rgb(106,90,205)"})
console = Console(theme=custom_theme)

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
    console.print(f"{player}'s turn!:", style="Bold rgb(127,255,212) underline")

def printOutInfo(user1Name: str, user2Name: str, user1Type: str, user2Type: str) -> None:
    user1Output = user1Name + ": " + user1Type + "\n"
    user2Output = user2Name + ": " + user2Type + "\n"
    lineLength = max(len(user1Output), len(user2Output))
    console.print(
            f"[purple]{"─"*lineLength}[/purple]\n"
            f"{user1Output}"
            f"{user2Output}"
            f"[purple]{"─"*lineLength}[/purple]"
          )

def printOutGrid(list: list) -> None:
    output = ""
    for r, row in enumerate(grid):
        for c, col in enumerate(grid[r]):

            if grid[r][c] != "═" and c != 0:
                output += "[green]║[/green]" + f"[blue]{grid[r][c]}[/blue]"
            elif c == 0 and grid[r][c] != "═":
                output += "[green] [/green]" + f"[blue]{grid[r][c]}[/blue]"
            elif c == 0:
                output += "[green] [/green]" + f"[green]{grid[r][c]}[/green]"
            else: 
                output += "[green]╬[/green]" + f"[green]{grid[r][c]}[green]"
        if grid[r][c] != "═":
            if r < 4:
                output += "\n"
        else:
            output += "\n"
    console.print(output, style="green")

def updateGrid(player: str, userInput: int, userType: str) -> bool:
    pos = 1
    for r, row in enumerate(grid):
        for c, col in enumerate(grid[r]):
            state = grid[r][c]
            if state != "═":
                pos += 1
                if userInput == pos-1 and grid[r][c] != "X" and grid[r][c] != "O":
                    grid[r][c] = userType
                    os.system(operator)
                    return True
                elif userInput == pos-1 and grid[r][c] == "X" and grid[r][c] == "O":
                    os.system(operator)
                    printEssentials(player, user1Name, user2Name, user1Type, user2Type, grid)
                    inputCheckerOut = BadInputChecker(player, userType)
                    # stata = inputCheckerOut[0]
                    userInput = inputCheckerOut[1]
                    player = inputCheckerOut[2][0]
                    userType = inputCheckerOut[2][1]
                    
                    return False
                else:
                    os.system(operator) 
    

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

def printEssentials(player: str, user1Name:str, user2Name: str, user1Type: str, user2Type: str, grid: list) -> None:
    printOutInfo(user1Name, user2Name, user1Type, user2Type)
    printPlayer(player)
    printOutGrid(grid)

def updateTurns(stata: bool, player: str, user1Name: str, user2Name: str, userType: str, user1Type: str, user2Type: str) -> list:
    """Switches who the player that is going to be displayed and their type based on who just went"""
    if stata == True:
        if player == user1Name:
            player = user2Name
            userType = user2Type
            return [player, userType, stata]
        else: 
            player = user1Name
            userType = user1Type 
            return [player, userType, stata]
    else:
        return [player, userType, stata]
    

def updateTheData(player: str, user1Name: str, user2Name: str, userType: str, user1Type: str, user2Type: str, userInput: int) -> list:
    stata = updateGrid(player, userInput=userInput, userType=userType)
    return updateTurns(stata, player, user1Name, user2Name, userType, user1Type, user2Type)

def BadInputChecker(player: str, userType: str) -> list:
    """Tells user to input a number of one of the remaining slots"""
    theChecker = True
    while theChecker == True:
        os.system(operator)
        printEssentials(player, user1Name, user2Name, user1Type, user2Type, grid)
        userInput = console.input(f"[red]Please[/red] input any of these numbers:| {" ".join(map(str, findRemaining()))} |: ")
        if str(userInput).isnumeric():
            if checkUserInput(int(userInput)) == True:
                stata = updateGrid(player, userInput, userType)
                playerUserType = updateTheData(player, user1Name, user2Name, userType, user1Type, user2Type, int(userInput))
                theChecker = False
    
    return [stata, userInput, playerUserType]

def checkWin(grid) -> list:
    # Sweeps down:
    for row in grid:
        console.print(row)
        if row != ["═", "═", "═"]:
            if row[0] == row[1] and row[1] == row[2]:
                print("YOU WIN up down")
                return True
        # time.sleep(2)
    # Sweeps to the right:
    for c, col in enumerate(grid[0]):
        if grid[0][c] == grid[2][c] and grid[2][c] == grid[4][c]:
            print("You win left right")
            return True
        
    # Diagonal Check:
    if grid[0][0] == grid[2][1] and grid[2][1] == grid[4][2]:
        print("You win diag left - right")
        return True
    elif grid[0][2] == grid[2][1] and grid[2][1] ==  grid[4][0]:
        print("You win diag right - left")
        return True
    return False
            
    
userInput = ""
userType = "X"
gameState = 1
player = ""
winnerType = "X"
stata = True
system = platform.system()
if system == "Windows":
    operator = "cls"
elif system == "Darwin":
    operator = "clear"

os.system(operator)
if __name__ == "__main__":
    count = 0
    while userInput != "stop":
        if gameState == 1:
            user1Name = console.input("[blue]User [red]One's[/red] Name: [/blue]")
            user2Name = console.input("[blue]User [red]Two's[/red] Name: [/blue]")
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

            os.system(operator)
            gameState = 2
        
        if gameState == 2:
            os.system(operator)
            printEssentials(player, user1Name, user2Name, user1Type, user2Type, grid)
            userInput = console.input(f"Input any of these numbers:| {" ".join(map(str, findRemaining()))} |: ")
            if userInput == "stop":
                break

            didSomeonePutAStr = userInput.isnumeric()
            while didSomeonePutAStr != True:
                os.system(operator)
                printEssentials(player, user1Name, user2Name, user1Type, user2Type, grid)
                userInput = console.input(f"[red]Please[/red] input any of these numbers:| {" ".join(map(str, findRemaining()))} |: ")
                if userInput.isnumeric():
                    playerUserType = updateTheData(player, user1Name, user2Name, userType, user1Type, user2Type, int(userInput))
                    player = playerUserType[0]
                    userType = playerUserType[1]

                didSomeonePutAStr = userInput.isnumeric()
                if didSomeonePutAStr:
                    stata = updateGrid(player, userInput=int(userInput), userType=userType)
            
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
            stata = playerUserType[2]
            if stata == True:
                count += 1
            if count >= 4:
                print(count)
                
                if count < 9:
                    winState = checkWin(grid)
                    if winState == True:
                        gameState = 3
                else:
                    time.sleep(1)
                    gameState = 3
                    console.print("Tie")

        if gameState == 3:
            print("")
            print("WooHoo!") 
            break