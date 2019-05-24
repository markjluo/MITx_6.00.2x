import matplotlib.pyplot as plt

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or fields[0] == 'Boston' or fields[0] == 'Day':
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)



low, high = loadFile()
diff = high - low
plt.plot(range(1, 32), )