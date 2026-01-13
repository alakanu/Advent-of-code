otherIndex = 0
areaIndex = 1

x = 0
y = 1

minX= 0
maxX = 1
minY = 2
maxY = 3
centreX = 4
centreY = 5


def calculateArea(coord1, coord2):
    b = abs(coord1[0] - coord2[0]) + 1
    h = abs(coord1[1] - coord2[1]) + 1
    return b*h

def makeRectangle(coord1, coord2):
    rect = [0,0,0,0, 0, 0]
    rect[minX] =  min(coord1[x], coord2[x])
    rect[maxX] =  max(coord1[x], coord2[x])
    rect[minY] =  min(coord1[y], coord2[y])
    rect[maxY] =  max(coord1[y], coord2[y])
    rect[centreX] = rect[minX] + (rect[maxX] - rect[minX]) /2
    rect[centreY] = rect[minY] + (rect[maxY] - rect[minY]) /2
    return tuple(rect)

def insideExclusive(start, end, val):
    return start < val and val < end

def insideEndExclusive(start, end, val):
    return start <= val and val < end

def insideStartExclusive(start, end, val):
    return start < val and val <= end

def goesAcrossTheRectangle(rect, coord1, coord2):
    coordMinX = min(coord1[x], coord2[x])
    coordMaxX = max(coord1[x], coord2[x])
    coordMinY = min(coord1[y], coord2[y])
    coordMaxY = max(coord1[y], coord2[y])
    if coord1[x] == coord2[x]:
        return insideExclusive(rect[minX], rect[maxX], coord1[x]) and (insideEndExclusive(coordMinY, coordMaxY, rect[minY]) or insideStartExclusive(coordMinY, coordMaxY, rect[maxY]))
    return insideExclusive(rect[minY], rect[maxY], coord1[y]) and (insideEndExclusive(coordMinX, coordMaxX, rect[minX]) or insideEndExclusive(coordMinX, coordMaxX, rect[maxX]))
    
def identifyQuadrant(rect, coord):
    if insideExclusive(rect[minX], rect[maxX], coord[x]) and insideExclusive(rect[minY], rect[maxY], coord[y]):
        return -1
    if coord[x] < rect[centreX]:
        return 3 if coord[y] > rect[centreY] else 0
    else:
        return 2 if coord[y] > rect[centreY] else 1

def rectangleIsInsideShape(coord1, coord2, tiles, tilesCount):
    rect = makeRectangle(coord1, coord2)
    visitedQuadrants = []
    initialQuadrant = identifyQuadrant(rect, tiles[0])
    if initialQuadrant == -1:
        return False
    visitedQuadrants.append(initialQuadrant)

    for i in range(0, tilesCount):
        j = (i + 1) % tilesCount
        previousQuadrant = visitedQuadrants[-1]
        nextQuadrant = identifyQuadrant(rect, tiles[j])
        if nextQuadrant == -1 or goesAcrossTheRectangle(rect, tiles[i], tiles[j]):
            return False
        if previousQuadrant != nextQuadrant:
            if len(visitedQuadrants) >= 2 and visitedQuadrants[-2] == nextQuadrant:
                visitedQuadrants.pop(-1)
            else:
                visitedQuadrants.append(nextQuadrant)
    return len(visitedQuadrants) >= 5 and visitedQuadrants[0] == visitedQuadrants[4]


filePath = "RedTiles.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    coordinatesRawStr = fileContent.splitlines()
    redTiles = [(int(splitCoords[0]), int(splitCoords[1])) for splitCoords in [unSplitCoords.split(",") for unSplitCoords in coordinatesRawStr]]
    redTilesCount = len(redTiles)

    currentMax = -1
    maxTiles = (0, 1)

    for tileIndex in range(0, redTilesCount - 1):
        for otherTileIndex in range(tileIndex + 1, redTilesCount):
            area = calculateArea(redTiles[tileIndex], redTiles[otherTileIndex])
            if rectangleIsInsideShape(redTiles[tileIndex], redTiles[otherTileIndex], redTiles, redTilesCount):
                if area > currentMax:
                    currentMax = area
                    maxTiles = (tileIndex, otherTileIndex)

    print("The result is " + str(currentMax) + " obtained by picking " + str(redTiles[maxTiles[0]]) + " and " + str(redTiles[maxTiles[1]]))