import numpy as np
import math

def findNextWhiteSpaceIndexOrEnd(lineStr, startIndex, lineLength):
    i = startIndex
    while i < lineLength and lineStr[i] != " ":
        i = i + 1
    return i

def findNextNonWhiteSpaceIndexOrEnd(lineStr, startIndex, lineLength):
    i = startIndex
    while i < lineLength and lineStr[i] == " ":
        i = i + 1
    return i

filePath = "MathsSheet.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    mathsSheetLines = fileContent.splitlines()
    numbersLinesCount = len(mathsSheetLines) - 1
    numbersLinesLengths = [len(line) for line in mathsSheetLines[:numbersLinesCount]]
    operatorsLineIndex = numbersLinesCount
    operatorsLineLength = len(mathsSheetLines[operatorsLineIndex])
    numbersLinesCursors = [0 for _ in range(0, numbersLinesCount)]
    operatorsLineCursor = 0
    result = 0
    while numbersLinesCursors[0] < numbersLinesLengths[0]:

        operands = []
        for lineIndex in range(0, numbersLinesCount):
            nextNonWhiteSpaceIndex = findNextNonWhiteSpaceIndexOrEnd(mathsSheetLines[lineIndex], numbersLinesCursors[lineIndex], numbersLinesLengths[lineIndex])
            newLineCursor = nextNonWhiteSpaceIndex
            if nextNonWhiteSpaceIndex < numbersLinesLengths[lineIndex]:
                numberBeginIndex = nextNonWhiteSpaceIndex
                nextWhiteSpaceIndex = findNextWhiteSpaceIndexOrEnd(mathsSheetLines[lineIndex], numberBeginIndex, numbersLinesLengths[lineIndex])
                numberEndIndex = nextWhiteSpaceIndex
                numberStr = mathsSheetLines[lineIndex][numberBeginIndex:numberEndIndex]
                operands.append(int(numberStr))
                newLineCursor = nextWhiteSpaceIndex
            numbersLinesCursors[lineIndex] = newLineCursor

        operatorBeginCursor = findNextNonWhiteSpaceIndexOrEnd( mathsSheetLines[operatorsLineIndex], operatorsLineCursor, operatorsLineLength)
        operatorsLineCursor = operatorBeginCursor
        operatorCharacter = "Error"
        if operatorBeginCursor < operatorsLineLength:
            operatorCharacter = mathsSheetLines[operatorsLineIndex][operatorBeginCursor]
            operatorsLineCursor =  operatorsLineCursor + 1

        match operatorCharacter:
            case "*":
                result = result + math.prod(operands)
            case "+":
                result = result + sum(operands)
            

    print("The grand total is " + str(result))