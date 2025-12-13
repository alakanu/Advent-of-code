
filePath = "Banks.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    banksStrList = fileContent.splitlines()
    totalJoltage = 0

    for bankStr in banksStrList:
        maxTens = 0
        maxUnits = 0
        bankStrLen = len(bankStr)
        for i in range(0, bankStrLen - 1):
            currentTens = int(bankStr[i])
            if currentTens > maxTens:
                maxTens = currentTens
                maxUnits = int(bankStr[i + 1])
                for j in range(i + 2, bankStrLen):
                    currentUnits = int(bankStr[j])
                    if currentUnits > maxUnits:
                        maxUnits = currentUnits
        totalJoltage = totalJoltage + 10 * maxTens + maxUnits
    

    print("The max joltage is " + str(totalJoltage))