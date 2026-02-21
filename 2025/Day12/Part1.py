
regionsSizes = []
regionsRequirements = []

filePath = "Input.txt"

with open(filePath, "r") as file:
    lines = file.read().splitlines()
    regionsBeginLine = 30
    for line in lines[regionsBeginLine:]:
        width = int(line[0:2])
        height = int(line[3:5])
        regionsSizes.append((width, height))
        requirements = []
        for requirement in line[7:].split(" "):
            requirements.append(int(requirement))
        regionsRequirements.append(requirements)

    count = 0
    for regionIndex in range(0, len(regionsRequirements)):
        boxSpace = sum(regionsRequirements[regionIndex]) * 9
        regionSpace = regionsSizes[regionIndex][0] * regionsSizes[regionIndex][1]
        if boxSpace <= regionSpace:
            count += 1
        
    print("The result is "+ str(count))