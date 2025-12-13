import math

boxXIndex = 0
boxYIndex = 1
boxZIndex = 2
boxCircuitIndex = 3
noCircuit = -1
distanceBoxIndex = 0
distanceValueIndex = 1

def isSameCircuit(box1, box2):
    return box1[boxCircuitIndex] != noCircuit and box1[boxCircuitIndex] == box2[boxCircuitIndex]

def squaredEuclideanDistance(box1, box2):
     x = box1[boxXIndex] - box2[boxXIndex]
     y = box1[boxYIndex] - box2[boxYIndex]
     z = box1[boxZIndex] - box2[boxZIndex]
     return x*x + y*y + z*z

def findDistanceMinIndex(boxes, boxIndex, distances):
    return len(distances) -1

def makeNewBoxInCircuit(oldBox, circuitIndex):
    newBox = list(oldBox)
    newBox[boxCircuitIndex] = circuitIndex
    return tuple(newBox)

def handleCircuitCreation(boxes, boxIndex1, boxIndex2, circuits):
    b1Circuit = boxes[boxIndex1][boxCircuitIndex]
    b2Circuit = boxes[boxIndex2][boxCircuitIndex]
    if b1Circuit == noCircuit:
        if b2Circuit == noCircuit:
            newCircuitIndex = len(circuits)
            circuits.append([boxIndex1, boxIndex2])
            boxes[boxIndex1] = makeNewBoxInCircuit(boxes[boxIndex1], newCircuitIndex)
            boxes[boxIndex2] = makeNewBoxInCircuit(boxes[boxIndex2], newCircuitIndex)
        else:
            circuits[b2Circuit].append(boxIndex1)
            boxes[boxIndex1] = makeNewBoxInCircuit(boxes[boxIndex1] , b2Circuit)
    else:
        if b2Circuit == noCircuit:
            circuits[b1Circuit].append(boxIndex2)
            boxes[boxIndex2] = makeNewBoxInCircuit(boxes[boxIndex2] , b1Circuit)
        else:
            if b1Circuit != b2Circuit:
                for boxIndex in circuits[b2Circuit]:
                    circuits[b1Circuit].append(boxIndex)
                    boxes[boxIndex] = makeNewBoxInCircuit(boxes[boxIndex] , b1Circuit)
                circuits[b2Circuit].clear()

def makeInitialBox(coordList):
    coordList.append(noCircuit)
    return tuple(coordList)

filePath = "JunctionBoxes.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    coordinatesRawStr = fileContent.splitlines()
    junctionBoxes = [makeInitialBox([int(c) for c in coordinateStr.split(",")]) for coordinateStr in coordinatesRawStr]
    boxesCount = len(junctionBoxes)
    circuits = []

    distanceJaggedMatrix = []

    for boxIndex in range(0, boxesCount - 1):
        distanceJaggedMatrix.append([])
        for otherboxIndex in range(boxIndex + 1, boxesCount):
            distanceJaggedMatrix[-1].append((otherboxIndex, squaredEuclideanDistance(junctionBoxes[boxIndex], junctionBoxes[otherboxIndex])))
        distanceJaggedMatrix[boxIndex].sort(reverse=True, key= lambda x : x[1])
        
    connectionsToMake = 1000
    while connectionsToMake > 0:
        minBoxAndDistanceIndices = (-1, -1)
        for boxIndex in range(0, boxesCount - 1):
            distanceMinIndex = findDistanceMinIndex(junctionBoxes, boxIndex, distanceJaggedMatrix[boxIndex])
            if distanceMinIndex != -1 and (minBoxAndDistanceIndices == (-1, -1) or distanceJaggedMatrix[minBoxAndDistanceIndices[0]][minBoxAndDistanceIndices[1]][distanceValueIndex] > distanceJaggedMatrix[boxIndex][distanceMinIndex][distanceValueIndex]):
                minBoxAndDistanceIndices = (boxIndex, distanceMinIndex)

        boxIndex1 = minBoxAndDistanceIndices[0]
        distanceIndex = minBoxAndDistanceIndices[1]
        boxIndex2 = distanceJaggedMatrix[boxIndex1][distanceIndex][distanceBoxIndex]
        distanceJaggedMatrix[boxIndex1].pop(distanceIndex)
        handleCircuitCreation(junctionBoxes, boxIndex1, boxIndex2, circuits)
        # print("Found connection between " + str(junctionBoxes[minIndex[0]]) + " and " + str(distanceJaggedMatrix[minIndex[0]][minIndex[1]][0]) + " at distance " + str(distanceJaggedMatrix[minIndex[0]][minIndex[1]][1]))  
        connectionsToMake = connectionsToMake - 1

    threeBiggest = []

    for circuitIndex in range(0, len(circuits)):
        circuitSize = len(circuits[circuitIndex])
        if circuitSize == 0:
            continue
        if len(threeBiggest) < 3 or circuitSize > len(circuits[threeBiggest[-1]]):
            threeBiggest.append(circuitIndex)
            threeBiggest.sort(reverse=True, key=lambda c: len(circuits[c]))
            if len(threeBiggest) > 3:
                threeBiggest.pop(-1)

    result = len(circuits[threeBiggest[0]]) * len(circuits[threeBiggest[1]]) * len(circuits[threeBiggest[2]])


    print("The result is " + str(result))