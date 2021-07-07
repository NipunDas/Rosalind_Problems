read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

lines = read_file.readlines()
DNAstrings = {}
DNAstring = ""
label = ""
for line in lines:
    if line[0] == ">" and len(label) != 0:
        DNAstrings[label] = DNAstring
        label = line.strip()[1:]
        DNAstring = ""
    elif line[0] == ">":
        label = line.strip()[1:]
    else:
        DNAstring += line.strip()
#adding last DNA string to dictionary
DNAstrings[label] = DNAstring

for key, value in DNAstrings.items():
    for key2, value2 in DNAstrings.items():
        if len(value) >= 3 and len(value2) >= 3 and value[len(value)-3:] == value2[:3] and value != value2:
            write_file.write(key + " " + key2 + "\n")

read_file.close()
write_file.close()