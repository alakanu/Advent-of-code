
filePath = "SecretCombination.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    steps = fileContent.splitlines()
    password = 0
    cursor = 50
    for step in steps:
        multiplier = -1 if step[0] == "L" else +1
        clicks = int(step[1:])        
        unclampedNewCursor = (cursor + clicks * multiplier)
        timesItTouchesZero = abs(unclampedNewCursor) // 100
        if cursor != 0 and unclampedNewCursor <= 0:
            timesItTouchesZero = timesItTouchesZero + 1
        password = password + timesItTouchesZero
        cursor = unclampedNewCursor % 100
    print("The password is " + str(password))