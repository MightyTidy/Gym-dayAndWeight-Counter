import tables

# Global Consts
i15 = 15
i5 = 5
i20 = 20
nestedListPullBackup = [["Incline pull machine", "Pull from above", 70, 20],
                        ["Back Pull machine", "Bench pull thing leaning forward", 55, 15],
                        ["Back Pull above machine", "Bench pull from above thing", 70, 15],
                        ["Bicep curl machine", "Curls Biceps", 30, 20], ["Back pull with dumbell", "pulls back", 15, 5],
                        ["Bicep curl no machine", "Curls Biceps", 12.5, 5]]
nestedListPull = [["Incline pull machine", "Pull from above", 70, 20],
                  ["Back Pull machine", "Bench pull thing leaning forward", 55, 15],
                  ["Back Pull above machine", "Bench pull from above thing", 70, 15],
                  ["Bicep curl machine", "Curls Biceps", 30, 20], ["Back pull with dumbell", "pulls back", 15, 5],
                  ["Bicep curl no machine", "Curls Biceps", 12.5, 5]]

nestedListPush = [["Overhead press machine", "push bars above shoulders up", 50, 10],
                  ["Chest press machine", "sitting bench push", 50, 10], ["Arm extension", "tricep push", 30, 10],
                  ["Bench press", "bench the press", 75, 5, ], ["Rope push", "push rope down", 30, 10],
                  ["Tricep push", "snow angel with triceps", 7.5, 3]]
nestedListPushBackup = [["Overhead press machine", "push bars above shoulders up", 50, 10],
                  ["Chest press machine", "sitting bench push", 50, 10], ["Arm extension", "tricep push", 30, 10],
                  ["Bench press", "bench the press", 75, 5, ], ["Rope push", "push rope down", 30, 10],
                  ["Tricep push", "snow angel with triceps", 7.5, 3]]
nestedListLegs = [["This is Leg"]]
nestedListLegsBackup = [["This is Leg"]]

CounterFile = open("GymCounter.txt", "r")
iString = CounterFile.readline()
gymdayCounterPull = iString[2]
gymdayCounterPush = iString[7]
gymdayCounterLegs = iString[12]
CounterFile.close()
gymdayCounterLegs = int(gymdayCounterLegs)
gymdayCounterPush = int(gymdayCounterPush)
gymdayCounterPull = int(gymdayCounterPull)
day = input("What day was today, push, pull, or legs. \nAlternatively type reset to reset the day count \n :")
if day == "push":
    gymdayCounterPush = gymdayCounterPush + 1
    pushCounterFile = open("GymCounter.txt", "w")
    tString = str(gymdayCounterPull), str(gymdayCounterPush), str(gymdayCounterLegs)
    tString = str(tString)
    pushCounterFile.write(tString)
    pushCounterFile.close()
if day == "pull":
    gymdayCounterPull = gymdayCounterPull + 1
    pushCounterFile = open("GymCounter.txt", "w")
    tString = str(gymdayCounterPull), str(gymdayCounterPush), str(gymdayCounterLegs)
    tString = str(tString)
    pushCounterFile.write(tString)
    pushCounterFile.close()
if day == "legs":
    gymdayCounterLegs = gymdayCounterLegs + 1
    pushCounterFile = open("GymCounter.txt", "w")
    tString = str(gymdayCounterPull), str(gymdayCounterPush), str(gymdayCounterLegs)
    tString = str(tString)
    pushCounterFile.write(tString)
    pushCounterFile.close()
if day != "legs" and day != "pull" and day != "push" and day != "reset":
    print("Invalid input, try again")
if day == "reset":
    pushCounterFile = open("GymCounter.txt", "w")
    resetString = "('0', '0', '0')"
    pushCounterFile.write(resetString)

# if gymdayCounterLegs==3: for weight in nestedListLegs: weight[2] = weight[2] + weight[3] if gymdayCounterPush==3:
# for weight in nestedListPush: weight[2] = weight[2] + weight[3] use float and only time it equals real number is on
# 4 and when it doesn't end on full number I round it to int and do it that many times
timesIncrementPull = gymdayCounterPull / 4
timesIncrementPush = gymdayCounterPush / 4
timesIncrementLegs = gymdayCounterLegs / 4
""" How to increment the numbas"""
if timesIncrementPull >= 1.0:
    timesIncrementPull = timesIncrementPull
    multInc = int(timesIncrementPull)
    for i in range(int(multInc)):
        for weight in nestedListPull:
            weight[2] = weight[2] + weight[3]
if timesIncrementPush >= 1.0:
    timesIncrementPush = timesIncrementPush
    multInc = int(timesIncrementPush)
    for i in range(int(multInc)):
        for weight in nestedListPush:
            weight[2] = weight[2] + weight[3]
if timesIncrementLegs >= 1.0:
    timesIncrementLegs = timesIncrementLegs
    multInc = int(timesIncrementLegs)
    for i in range(int(multInc)):
        for weight in nestedListLegs:
            weight[2] = weight[2] + weight[3]

print(": Exercise Name", " " * 10, ": Description", " " * 28, ":", "Weight : Increment :")
"""Below is the Exercise Name in the Table"""
if day == "pull":
    for item in nestedListPull:
        theLength = len(item[0])
        mathfordeslen = len((item[1]))
        desSpaces = mathfordeslen - 39
        desSpaces = desSpaces * (-1)
        toUseSpaces = theLength - 23
        toUseSpaces = toUseSpaces * (-1)
        WeightLen = len(str(item[2]))
        weightSpaces = WeightLen - 5
        weightSpaces = weightSpaces * (-1)
        incrementLen = len(str(item[3]))
        incSpaces = incrementLen - 8
        incSpaces = incSpaces * (-1)
        print(":", item[0], (" " * toUseSpaces), ":", item[1], (" " * desSpaces), ":", item[2], (" " * weightSpaces),
              ":"
              , item[3], (" " * incSpaces), ":")
        print("-" * 92)
if day == "push":
    for item in nestedListPush:
        theLength = len(item[0])
        mathfordeslen = len((item[1]))
        desSpaces = mathfordeslen - 39
        desSpaces = desSpaces * (-1)
        toUseSpaces = theLength - 23
        toUseSpaces = toUseSpaces * (-1)
        WeightLen = len(str(item[2]))
        weightSpaces = WeightLen - 5
        weightSpaces = weightSpaces * (-1)
        incrementLen = len(str(item[3]))
        incSpaces = incrementLen - 8
        incSpaces = incSpaces * (-1)
        print(":", item[0], (" " * toUseSpaces), ":", item[1], (" " * desSpaces), ":", item[2], (" " * weightSpaces),
              ":"
              , item[3], (" " * incSpaces), ":")
        print("-" * 92)
if day == "legs":
    for item in nestedListLegs:
        theLength = len(item[0])
        mathfordeslen = len((item[1]))
        desSpaces = mathfordeslen - 39
        desSpaces = desSpaces * (-1)
        toUseSpaces = theLength - 23
        toUseSpaces = toUseSpaces * (-1)
        WeightLen = len(str(item[2]))
        weightSpaces = WeightLen - 5
        weightSpaces = weightSpaces * (-1)
        incrementLen = len(str(item[3]))
        incSpaces = incrementLen - 8
        incSpaces = incSpaces * (-1)
        print(":", item[0], (" " * toUseSpaces), ":", item[1], (" " * desSpaces), ":", item[2], (" " * weightSpaces),
              ":"
              , item[3], (" " * incSpaces), ":")
        print("-" * 92)
# For length of string stuff
"""for item in nestedList:
    x = 0
    y = len(item[3])
    if y > x:
        x = y
print(x)

print(len(" Description "))"""
