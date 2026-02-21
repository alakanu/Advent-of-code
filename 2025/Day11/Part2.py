
configIdx = 0
movesIdx = 1
joltageIdx = 2

filePath = "ServersConnections.txt"

serversIndices = dict()
serversLabels = []
serversConnections = []
beginIndex = 0
endIndex = -1
dacIndex = -1
fftIndex = -1

def getServerIndex(serverLabel):
    if serverLabel not in serversIndices:
        newIndex = len(serversConnections)
        serversConnections.append([])
        serversIndices[serverLabel] = newIndex
        serversLabels.append(serverLabel)
        return newIndex
    return serversIndices[serverLabel]

def findPathsCount(begin, end, excluding=-1):
    serversIsDeadEnd = [False for _ in serversConnections]
    counter = [0]
    if excluding != -1:
        serversIsDeadEnd[excluding] = True

    def depthFirst(node, currentPath):
        isDeadEnd = True
        newPath = currentPath + [node]
        for next in serversConnections[node]:
            if serversIsDeadEnd[next]:
                continue
            if next == end:
                # print("Found path: " + "->".join([serversLabels[i] for i in newPath + [next]]))
                counter[0] = counter[0] + 1
                isDeadEnd = False
                continue
            isDeadEnd = depthFirst(next, newPath) and isDeadEnd
        # if isDeadEnd:
        #     print("Found dead end: " + "->".join([serversLabels[i] for i in newPath]))
        serversIsDeadEnd[node] = isDeadEnd
        return isDeadEnd
    
    
    depthFirst(begin, [])
    return counter[0]
    

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
            if endIndex == -1 and target == "out":
                endIndex = targetIndex
            if targetIndex not in connections:
                connections.append(targetIndex)

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