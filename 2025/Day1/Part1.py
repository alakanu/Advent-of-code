
filePath = "SecretCombination.txt"
with open(filePath, "r") as file:
    fileContent = file.read()
    steps = fileContent.splitlines()
    password = 0
    cursor = 50
    for step in steps:
        multiplier = -1 if step[0] == "L" else +1
        clicks = int(step[1:])
        cursor = (cursor + clicks * multiplier) % 100
        if cursor == 0:
            password = password + 1
    print("The password is " + str(password))