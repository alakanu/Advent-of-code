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
    ingredients = [int(ingredient) for ingredient in database[blankLineIndex + 1:]]
    freshCount = 0
    for id in ingredients:
        for freshIngredientRange in freshIngredientsRanges:
            if id >= freshIngredientRange[0] and id <= freshIngredientRange[1]:
                freshCount = freshCount + 1
                break

    print("The number of fresh ingredients is " + str(freshCount))