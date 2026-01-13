import pulp

buttonsIdx = 0
joltageIdx = 1

filePath = "LightsDiagrams.txt"

with open(filePath, "r") as file:
    machinesParams = []
    for line in file.read().splitlines():
        machinesParams.append([[], []])
        buttonsAndJoltageRequirements = line.replace(" ","").split("]")[1].split("{")
        
        joltageRequirementStr = buttonsAndJoltageRequirements[1].replace("}","")
        joltageRequirementStrList = joltageRequirementStr.split(",")
        for req in joltageRequirementStrList:
            machinesParams[-1][joltageIdx].append(int(req))


        countersCount = len(machinesParams[-1][joltageIdx])
        for buttonRawStr in buttonsAndJoltageRequirements[0][1:].split("("):
            machinesParams[-1][buttonsIdx].append([])
            buttonBeingParsed = machinesParams[-1][buttonsIdx][-1]
            for i in range(0, countersCount):
                buttonBeingParsed.append(False)
            for buttonIdxStr in buttonRawStr.replace(")", "").split(","):
                counterIndex = int(buttonIdxStr)
                buttonBeingParsed[counterIndex] = True


    problemIndex = 0
    result = 0
    for params in machinesParams:
        countersCount = len(params[joltageIdx])
        buttonsCount = len(params[buttonsIdx])
        problemName = "Problem" + str(problemIndex)
        print("Solving "+ problemName)
        problem = pulp.LpProblem(problemName, pulp.LpMinimize)
        maxRequirement = max(params[joltageIdx])
        buttonsVariables = [pulp.LpVariable(name="x" + str(i),lowBound=0, upBound=maxRequirement, cat=pulp.LpInteger) for i in range(0, buttonsCount)]
        problem += (pulp.lpSum(buttonsVariables), "Obj")
        for counterIndex in range(0, countersCount):
            counterVariables = []
            for buttonIndex in range(0, buttonsCount):
                if params[buttonsIdx][buttonIndex][counterIndex]:
                    counterVariables.append(buttonsVariables[buttonIndex])
            problem += (pulp.lpSum(counterVariables) == params[joltageIdx][counterIndex])
        solutionStatusCode = problem.solve(pulp.PULP_CBC_CMD(msg=False,threads=pulp.Any, timeLimit=10))
        print("Solution is " + str(pulp.LpStatus[solutionStatusCode]))
        problemIndex = problemIndex +1
        for moveVar in buttonsVariables:
            result = result + moveVar.value()

    print("The result is "+ str(result))