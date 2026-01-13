
configIdx = 0
movesIdx = 1
joltageIdx = 2

filePath = "ServersConnections.txt"

def getServerIndex(serverLabel, serversIndices, serversConnections,serversLabels):
    if serverLabel not in serversIndices:
        newIndex = len(serversConnections)
        serversConnections.append([])
        serversIndices[serverLabel] = newIndex
        serversLabels.append(serverLabel)
        return newIndex
    return serversIndices[serverLabel]

with open(filePath, "r") as file:
    serversIndices = dict()
    serversLabels = []
    serversConnections = []
    beginIndex = 0
    endIndex = -1
    for line in file.read().splitlines():
        sourceAndTargets = line.split(":")
        source = sourceAndTargets[0]
        sourceIndex = getServerIndex(source,serversIndices,serversConnections,serversLabels)
        if source == "you":
            beginIndex = sourceIndex
        connections = serversConnections[sourceIndex]
        for target in sourceAndTargets[1][1:].split():
            targetIndex = getServerIndex(target,serversIndices,serversConnections,serversLabels)
            if endIndex == -1 and target == "out":
                endIndex = targetIndex
            if targetIndex not in connections:
                connections.append(targetIndex)
    nodesCount = len(serversIndices)
    pathsList = [[beginIndex]]

    pathsCount = 0

    for pathLength in range(0, nodesCount - 1):
        newPathsList = []
        for path in pathsList:
            for nextServerIndex in serversConnections[path[-1]]:
                if nextServerIndex == endIndex:
                    pathsCount = pathsCount + 1
                else:
                    newPathsList.append(path.copy())
                    newPathsList[-1].append(nextServerIndex)
        pathsList = newPathsList



    print("The result is "+ str(pathsCount))