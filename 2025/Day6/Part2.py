import math

def findNextNonWhiteSpaceIndexOrEnd(lineStr, startIndex):
    i = startIndex
    while i >= 0 and lineStr[i] == " ":
        i = i -1
    return i

def isBlankColumn(lines, cursor):
    return all(line[cursor] == " " for line in lines)

filePath = "MathsSheet.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    mathsSheetLines = fileContent.splitlines()
    numbersLinesCount = len(mathsSheetLines) - 1
    numbersLines =  mathsSheetLines[:numbersLinesCount]
    numbersLinesCursor = len(mathsSheetLines[0]) - 1
    operatorsLineIndex = numbersLinesCount
    operatorsLineCursor = len(mathsSheetLines[operatorsLineIndex]) - 1
    result = 0
    while numbersLinesCursor >= 0:
        operands = []
        while numbersLinesCursor >= 0 and not isBlankColumn(numbersLines, numbersLinesCursor):
            numberDigitsList = []
            for lineIndex in range(0,numbersLinesCount):
                digitCharacter = mathsSheetLines[lineIndex][numbersLinesCursor]
                if digitCharacter != " ":
                    numberDigitsList.append(digitCharacter)
            numberStr = "".join(numberDigitsList)
            operands.append(int(numberStr))
            numbersLinesCursor = numbersLinesCursor - 1

        operatorsLineCursor = findNextNonWhiteSpaceIndexOrEnd(mathsSheetLines[operatorsLineIndex], operatorsLineCursor)
        operatorCharacter = "Error"
        if operatorsLineCursor >= 0:
            operatorCharacter = mathsSheetLines[operatorsLineIndex][operatorsLineCursor]
            operatorsLineCursor =  operatorsLineCursor - 1

        match operatorCharacter:
            case "*":
                result = result + math.prod(operands)
            case "+":
                result = result + sum(operands)

        while numbersLinesCursor >= 0 and isBlankColumn(numbersLines, numbersLinesCursor):
            numbersLinesCursor = numbersLinesCursor -1
            

    print("The grand total is " + str(result))