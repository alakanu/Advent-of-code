filePath = "TachyonManifold.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    stages = fileContent.splitlines()
    stageSize = len(stages[0])
    stagesCount = len(stages)
    entryPoint = stages[0].index("S")
    splitter = "^"
    beamPositionAndTimelineCount = { entryPoint: 1 }

    for stageIndex in range(1, stagesCount):
        newStates = beamPositionAndTimelineCount.copy()
        for beamPosition, timelineCount in beamPositionAndTimelineCount.items():
            if stages[stageIndex][beamPosition] == splitter:                  
                if beamPosition -1 not in newStates:
                       newStates[beamPosition - 1] = 0
                newStates[beamPosition - 1] = newStates[beamPosition - 1] + timelineCount
                if beamPosition + 1 not in newStates:
                    newStates[beamPosition + 1] = 0
                newStates[beamPosition + 1] = newStates[beamPosition + 1] + timelineCount
                newStates.pop(beamPosition)
        beamPositionAndTimelineCount = newStates
    
    totalTimelinesCount = 0
    for beamPosition, timelineCount in beamPositionAndTimelineCount.items():
         totalTimelinesCount = totalTimelinesCount +  timelineCount

    print("There are " + str(totalTimelinesCount) +" different active timelines")