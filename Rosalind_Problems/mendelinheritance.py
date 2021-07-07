read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

def setVars():
    #declaring global variables
    global k
    global m
    global n
    global total

    k = int(organisms[0])
    m = int(organisms[1])
    n = int(organisms[2])
    total = k + m + n
    total = float(total)

line = read_file.readline().strip()

organisms = line.split(" ")

k = None
m = None
n = None
total = None

setVars()

#order doesn't matter of organisms 1 and 2
def calculateProbability(organism1, organism2):
    #declaring global variables
    global k
    global m
    global n
    global total

    if organism1 == "K":
        probability = k/total
        k -= 1
        total -= 1
    elif organism1 == "M":
        probability = m/total
        m -= 1
        total -= 1
    else:
        probability = n/total
        n -= 1
        total -= 1

    if organism2 == "K":
        probability *= (k/total)
    elif organism2 == "M":
        probability *= (m/total)
    else:
        probability *= (n/total)

    if organism1 != organism2:
        probability *= 2

    if (organism1 == "M" and organism2 == "N") or (organism1 == "N" and organism2 == "M"):
        probability *= 0.5
    elif (organism1 == "M") and (organism2 == "M"):
        probability *= 0.75
    elif (organism1 == "N") and (organism2 == "N"):
        probability = 0

    setVars()

    return probability

sum = (calculateProbability("K", "K") + calculateProbability("K", "M") + calculateProbability("K", "N") + calculateProbability("M", "M") + calculateProbability("M", "N") + calculateProbability("N", "N"))

write_file.write(str(sum))

read_file.close()
write_file.close()