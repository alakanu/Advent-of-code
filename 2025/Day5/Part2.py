import numpy as np

filePath = "Database.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    database = fileContent.splitlines()
    blankLineIndex = 0
    for i in range(0, len(database)):
        if not database[i]:
            blankLineIndex = i
            break
    freshIngredientsRanges = [(int(freshRange.split("-")[0]), int(freshRange.split("-")[1])) for freshRange in database[:blankLineIndex]]

    combinedAny = True

    while combinedAny:
        combinedAny = False
        rangesCount = len(freshIngredientsRanges)
        i = rangesCount
        while not combinedAny and i > 0:
            i = i -1
            idRange = freshIngredientsRanges[i]
            for j in range(i - 1, -1, -1):
                otherIdRange = freshIngredientsRanges[j]
                if not(idRange[1] < otherIdRange[0] or otherIdRange[1] < idRange[0]):
                    freshIngredientsRanges[j] = (min(idRange[0], otherIdRange[0]), max(idRange[1], otherIdRange[1]))
                    freshIngredientsRanges.pop(i)
                    i = j
                    idRange = freshIngredientsRanges[i]
                    combinedAny = True
                    
    freshCount = 0
    for idRange in freshIngredientsRanges:
        freshCount = freshCount + idRange[1] - idRange[0] + 1
    
    print("The number of fresh ingredients is " + str(freshCount))