read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

DNAstring = ""
currentLabel = None

lines = read_file.readlines()

data = {}

for line in lines:

    #rading in data and storing in dictionary by detecting >
    if line[0] == ">":
        if len(DNAstring) > 0:
            data[currentLabel] = DNAstring
            DNAstring = ""
        currentLabel = line[1:].strip()
    else:
        DNAstring += line.strip()

    #getting data from last DNA string (b/c there is no next >)
    if lines.index(line) == len(lines) - 1:
        data[currentLabel] = DNAstring

#stores information about string with most data
max = 0
maxKey = None

for key, string in data.items():
    GCcount = 0
    for char in string:
        if char == "C" or char == "G":
            GCcount += 1
    if 100 * float(GCcount)/len(string) > max:
        max = 100 * float(GCcount)/len(string)
        maxKey = key

write_file.write(maxKey + "\n" + str(max))