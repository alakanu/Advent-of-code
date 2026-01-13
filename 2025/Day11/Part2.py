
configIdx = 0
movesIdx = 1
joltageIdx = 2

filePath = "ServersConnections.txt"

serversIndices = dict()
serversLabels = []
serversConnections = []
reverseServersConnections = []
beginIndex = 0
endIndex = -1
dacIndex = -1
fftIndex = -1

def getServerIndex(serverLabel):
    if serverLabel not in serversIndices:
        newIndex = len(serversConnections)
        serversConnections.append([])
        reverseServersConnections.append([])
        serversIndices[serverLabel] = newIndex
        serversLabels.append(serverLabel)
        return newIndex
    return serversIndices[serverLabel]

def findPathsImpl(begin, end, maxLength, connections):
    pathsList = [[begin]]
    result = []
    while pathsList:
        newPathsList = []
        for path in pathsList:
            for nextServerIndex in connections[path[-1]]:
                if nextServerIndex == end:
                    result.append(path.copy())
                    result[-1].append(end)
                elif nextServerIndex not in path:
                    newPathsList.append(path.copy())
                    newPathsList[-1].append(nextServerIndex)
        pathsList = newPathsList
    return result

def findPaths(begin, end, maxLength):
    return findPathsImpl(begin,end, maxLength, serversConnections)

def findPathsReverse(begin, end, maxLength):
    return findPathsImpl(begin,end, maxLength, reverseServersConnections)

def findPathsCount(begin,end, excluding=-1):
    serversSuccessors = [[] for _ in serversConnections]
    frontier = [end]
    while frontier:
        newFrontier = []
        for current in frontier:
            for predecessor in reverseServersConnections[current]:
                if predecessor == excluding:
                    continue
                isUnexplored = len(serversSuccessors[predecessor]) == 0
                serversSuccessors[predecessor].append(current)
                for otherSuccessors in serversSuccessors[current]:
                    if otherSuccessors not in serversSuccessors[predecessor]:
                        serversSuccessors[predecessor].append(otherSuccessors)
                if predecessor != begin and isUnexplored and predecessor not in newFrontier:
                    newFrontier.append(predecessor)
        frontier = newFrontier

    serversPathCounters = [0 for _ in serversConnections]
    serversPathCounters[begin] = 1
    frontier = [begin]

    while frontier:
        newFrontier = []
        for current in frontier:
            for next in serversConnections[current]:
                if next == excluding or (next != end and not serversSuccessors[next]):
                    continue
                wasExplored = serversPathCounters[next] != 0
                if wasExplored:
                    newPathsDiscovered = serversPathCounters[next] * serversPathCounters[current]
                    serversPathCounters[next] = serversPathCounters[next] + newPathsDiscovered 
                    for successor in serversSuccessors[next]:
                        serversPathCounters[successor] = serversPathCounters[successor] + newPathsDiscovered
                else:
                    serversPathCounters[next] = serversPathCounters[next] + serversPathCounters[current]
                    if next != end:
                        newFrontier.append(next)
        frontier = newFrontier

    return serversPathCounters[end]



with open(filePath, "r") as file:
    for line in file.read().splitlines():
        sourceAndTargets = line.split(":")
        source = sourceAndTargets[0]
        sourceIndex = getServerIndex(source)
        if source == "svr":
            beginIndex = sourceIndex
        if source == "dac":
            dacIndex = sourceIndex
        if source == "fft":
            fftIndex = sourceIndex
        connections = serversConnections[sourceIndex]
        for target in sourceAndTargets[1][1:].split():
            targetIndex = getServerIndex(target)
            reverseConnections = reverseServersConnections[targetIndex]
            if endIndex == -1 and target == "out":
                endIndex = targetIndex
            if targetIndex not in connections:
                connections.append(targetIndex)
            if sourceIndex not in reverseConnections:
                reverseConnections.append(sourceIndex)

    pathsCount = 0

    b = findPathsCount(dacIndex, fftIndex)
    if b != 0:
        a = findPathsCount(beginIndex, dacIndex, fftIndex)
        if a != 0:
            c = findPathsCount(fftIndex, endIndex, dacIndex)
            pathsCount = a*b*c

    e = findPathsCount(fftIndex, dacIndex)
    if e != 0:
        d = findPathsCount(beginIndex, fftIndex, dacIndex)
        if d != 0:
            f = findPathsCount(dacIndex, endIndex, fftIndex)
            pathsCount = pathsCount + d * e * f

    print("The result is "+ str(pathsCount))