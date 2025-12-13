import numpy as np

filePath = "Rolls.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    rollsStrList = fileContent.splitlines()
    accessibleRollsCount = 0
    columnCount = len(rollsStrList[0])
    rowCount = len(rollsStrList)
    adjacentsOffsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(0, rowCount):
        for j in range(0, columnCount):
            if rollsStrList[i][j] != "@":
                continue
            adjacentCount = 0
            for offset in adjacentsOffsets:
                adjacentCoordinates = tuple(np.add(np.array((i,j)), np.array(offset)).tolist())
                column = adjacentCoordinates[1]
                row = adjacentCoordinates[0]
                if row >= 0 and column >= 0 and row < rowCount and column < columnCount:
                    if rollsStrList[row][column] == "@":
                        adjacentCount = adjacentCount + 1
                    if adjacentCount >= 4:
                        break
            if adjacentCount < 4:
                accessibleRollsCount = accessibleRollsCount + 1

    print("The number of accessible rolls is " + str(accessibleRollsCount))