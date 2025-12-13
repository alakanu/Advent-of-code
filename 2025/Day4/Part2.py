import numpy as np

filePath = "Rolls.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    rollsStrList = fileContent.splitlines()
    rollsGrid = [list(row) for row in rollsStrList]
    accessibleRollsCount = 0
    columnCount = len(rollsGrid[0])
    rowCount = len(rollsGrid)
    adjacentsOffsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    removedThisTurn = []
    removedAny = True

    while removedAny:
        for i in range(0, rowCount):
            for j in range(0, columnCount):
                if rollsGrid[i][j] != "@":
                    continue
                adjacentCount = 0
                for offset in adjacentsOffsets:
                    adjacentCoordinates = tuple(np.add(np.array((i,j)), np.array(offset)).tolist())
                    column = adjacentCoordinates[1]
                    row = adjacentCoordinates[0]
                    if row >= 0 and column >= 0 and row < rowCount and column < columnCount:
                        if rollsGrid[row][column] == "@":
                            adjacentCount = adjacentCount + 1
                        if adjacentCount >= 4:
                            break
                if adjacentCount < 4:
                    removedThisTurn.append((i,j))
                    accessibleRollsCount = accessibleRollsCount + 1
        for (row, column) in removedThisTurn:
            rollsGrid[row][column] = "."
        removedAny = len(removedThisTurn) > 0
        removedThisTurn.clear()

    print("The number of accessible rolls is " + str(accessibleRollsCount))