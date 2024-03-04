def addDuration(durations:list):
    totalSeconds = 0
    for duration in durations:
        totalSeconds += int(duration[0]) * 60 + int(duration[2:])

    print("Total Seconds: {} | MM:SS {:02d}:{:02d}".format(totalSeconds, totalSeconds // 60, totalSeconds % 60))
    return totalSeconds

def calcCost(seconds):
    return seconds * 0.05

durations = [
    "2:38",
    "1:03",
    "2:05",
    "1:34",
    "1:46",
    "1:17",
    "1:26",
    "1:01",
    "1:01",
    "1:02",
    "1:02",
    "1:16",
    "1:01",
    "1:02",
    "1:02",
    "1:01",
    "1:01",
    "1:04",
    "1:02",
    "1:02",
    "1:01",
    "1:01",
    "1:04",
    "1:57"
]

print("Total Cost: ${:.2f}".format(calcCost(addDuration(durations))))

