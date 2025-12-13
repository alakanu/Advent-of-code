otherIndex = 0
areaIndex = 1

def calculateArea(coord1, coord2):
    b = abs(coord1[0] - coord2[0]) + 1
    h = abs(coord1[1] - coord2[1]) + 1
    return b*h

filePath = "RedTiles.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    coordinatesRawStr = fileContent.splitlines()
    redTiles = [(int(splitCoords[0]), int(splitCoords[1])) for splitCoords in [unSplitCoords.split(",") for unSplitCoords in coordinatesRawStr]]
    redTilesCount = len(redTiles)
    areaJaggedMatrix = []

    for tileIndex in range(0, redTilesCount - 1):
        areaJaggedMatrix.append([])
        for otherTileIndex in range(tileIndex + 1, redTilesCount):
            areaJaggedMatrix[-1].append((otherTileIndex, calculateArea(redTiles[tileIndex], redTiles[otherTileIndex])))
        areaJaggedMatrix[tileIndex].sort(key= lambda x : x[1])
        
    maxBoxAndAreaIndices = (0, areaJaggedMatrix[0][-1][0])
    for tileIndex in range(1, redTilesCount - 1):
        if areaJaggedMatrix[tileIndex][-1][areaIndex] > areaJaggedMatrix[maxBoxAndAreaIndices[0]][maxBoxAndAreaIndices[1]][areaIndex]:
            maxBoxAndAreaIndices = (tileIndex, len(areaJaggedMatrix[tileIndex]) -1)
    t1Index = maxBoxAndAreaIndices[0]
    t2Index = areaJaggedMatrix[maxBoxAndAreaIndices[0]][maxBoxAndAreaIndices[1]][otherIndex]
    result = areaJaggedMatrix[maxBoxAndAreaIndices[0]][maxBoxAndAreaIndices[1]][areaIndex]

    print("The result is " + str(result) + " obtained by picking " + str(redTiles[t1Index]) + " and " + str(redTiles[t2Index]))