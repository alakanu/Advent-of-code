
def findLeftmostBiggestNumberIndex(batteries):
    biggestIndex = 0
    biggest = int(batteries[biggestIndex])
    for i in range(0, len(batteries)):
        number = int(batteries[i])
        if number > biggest:
            biggest = number
            biggestIndex = i
    return biggestIndex

filePath = "Banks.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    banksStrList = fileContent.splitlines()
    requiredBatteriesCount = 12
    totalJoltage = 0

    for bankStr in banksStrList:
        batteriesIndices = []
        nextIndexForSearch = 0
        bankStrLen = len(bankStr)
        while len(batteriesIndices) < requiredBatteriesCount:
            batteriesRemainingToActivate = requiredBatteriesCount - len(batteriesIndices)
            biggestIndexInSubRange = findLeftmostBiggestNumberIndex(bankStr[nextIndexForSearch : bankStrLen - batteriesRemainingToActivate +1])
            activatedBatteryIndex = nextIndexForSearch + biggestIndexInSubRange
            batteriesIndices.append(int(bankStr[activatedBatteryIndex]))
            nextIndexForSearch = nextIndexForSearch + biggestIndexInSubRange + 1
        for i in range(0, requiredBatteriesCount):
            totalJoltage = totalJoltage + pow(10, requiredBatteriesCount - i - 1) * batteriesIndices[i]
    

    print("The max joltage is " + str(totalJoltage))