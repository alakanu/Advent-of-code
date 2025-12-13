
filePath = "Ranges.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    numericRangesStrList = fileContent.split(",")
    invalidIdAccumulator = 0
    invalidIdsSet = set()
    for numericRangeStr in numericRangesStrList:
        extentsAsStr = numericRangeStr.split("-")
        leftStr = extentsAsStr[0]
        rightStr = extentsAsStr[1]
        left = int(leftStr)
        right = int(rightStr)
        currentId = left
        while(currentId <= right):
            id = currentId
            currentId = currentId + 1
            if id in invalidIdsSet:
                continue
            idStr = str(id)
            idStrLen = len(idStr)
            halfSize = idStrLen // 2
            isInvalidId = False
            for testSize in range(1, halfSize + 1):
                if idStrLen % testSize != 0:
                    continue
                isInvalidId = True
                copiesCount = idStrLen // testSize
                for i in range(0, testSize):
                    for copyIndex in range(1, copiesCount):
                        if idStr[i] != idStr[i + copyIndex * testSize]:
                            isInvalidId = False
                            break
                    if isInvalidId == False:
                        break
                if isInvalidId:
                    break
            if isInvalidId:
                invalidIdsSet.add(id)
                invalidIdAccumulator = invalidIdAccumulator + id

    print("The sum of invalid IDs is " + str(invalidIdAccumulator))