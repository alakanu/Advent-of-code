import pulp

configIdx = 0
movesIdx = 1
joltageIdx = 2

filePath = "LightsDiagrams.txt"

with open(filePath, "r") as file:
    machinesParams = []
    for line in file.read().splitlines():
        machinesParams.append([[], [], []])
        configAndRest = line.replace(" ","").split("]")
        for character in configAndRest[0][1:]:
            buttonShouldBeOn = False
            if character == "#":
                buttonShouldBeOn = True
            machinesParams[-1][configIdx].append(buttonShouldBeOn)
        numberOfButtons = len(machinesParams[-1][configIdx])

        movesAndJoltageRequirements = configAndRest[1].split("{")
        for moveRawStr in movesAndJoltageRequirements[0][1:].split("("):
            machinesParams[-1][movesIdx].append([])
            moveBeingParsed = machinesParams[-1][movesIdx][-1]
            for i in range(0, numberOfButtons):
                moveBeingParsed.append(False)
            moveStr = moveRawStr.replace(")", "")
            for buttonIdxStr in moveStr.split(","):
                buttonIdx = int(buttonIdxStr)
                moveBeingParsed[buttonIdx] = True

        joltageRequirementStr = movesAndJoltageRequirements[1].replace("}","")
        joltageRequirementStrList = joltageRequirementStr.split(",")
        for i in range(0, numberOfButtons):
            machinesParams[-1][joltageIdx].append(int(joltageRequirementStrList[i]))

    machineConfigs = []
    problemIndex = 0
    result = 0
    for params in machinesParams:
        buttonsCount = len(params[configIdx])
        movesCount = len(params[movesIdx])
        machineConfigs.append([])
        problemName = "Problem" + str(problemIndex)
        print("Solving "+ problemName)
        problem = pulp.LpProblem(problemName, pulp.LpMinimize)
        movesVariables = [pulp.LpVariable(name="x" + str(i), cat=pulp.LpBinary) for i in range(0, movesCount)]
        problem += (pulp.lpSum(movesVariables), "Obj")
        for buttonIndex in range(0, buttonsCount):
            buttonVariables = []
            for moveIndex in range(0, movesCount):
                if params[movesIdx][moveIndex][buttonIndex]:
                    buttonVariables.append(movesVariables[moveIndex])
            if params[configIdx][buttonIndex]:
                auxVariable = pulp.LpVariable("k" + str(buttonIndex), 0, buttonsCount * 2, pulp.LpInteger)
                problem += (pulp.lpSum(buttonVariables) - 2 * auxVariable - 1 == 0)
            else:
                auxVariable = pulp.LpVariable("k" + str(buttonIndex), 0, buttonsCount * 2, pulp.LpInteger)
                problem += (pulp.lpSum(buttonVariables) - 2 * auxVariable == 0)
        solutionStatusCode = problem.solve(pulp.PULP_CBC_CMD(msg=False,threads=pulp.Any, timeLimit=10))
        print("Solution is " + str(pulp.LpStatus[solutionStatusCode]))
        problemIndex = problemIndex +1
        for moveVar in movesVariables:
            result = result + moveVar.value()

    print("The result is "+ str(result))