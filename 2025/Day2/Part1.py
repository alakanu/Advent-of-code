
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
        leftStrLen = len(leftStr)
        rightStrLen = len(rightStr)
        if leftStrLen == rightStrLen and leftStrLen != 0 and leftStrLen % 2 != 0:
            continue
        left = int(leftStr)
        right = int(rightStr)
        currentId = left
        while(currentId <= right):
            id = currentId
            idStr = str(id)
            idStrLen = len(idStr)
            currentId = currentId + 1
            if idStrLen % 2 != 0:
                continue
            midPointIndex = idStrLen // 2
            isInvalidId = True
            for i in range(0, midPointIndex):
                if idStr[i] != idStr[midPointIndex + i]:
                    isInvalidId = False
                    break
            if isInvalidId and not id in invalidIdsSet:
                invalidIdsSet.add(id)
                invalidIdAccumulator = invalidIdAccumulator + id

    print("The sum of invalid IDs is  " + str(invalidIdAccumulator))