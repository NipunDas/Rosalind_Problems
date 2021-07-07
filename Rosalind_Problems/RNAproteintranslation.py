read_file = open("input.txt", "r")
write_file = open("output.txt", "w")
table_file = open("RNAcodontable.txt")

lines = table_file.readlines()

data = {}
for line in lines:
    words = line.strip().split()
    i = 0
    while i < len(words) - 1:
        data[words[i]] = words[i+1]
        i += 2

DNAlines = read_file.readlines()
DNAstring = ""

for line in DNAlines:
    DNAstring += line.strip()

proteinString = ""

j = 0
started = False
while j <= len(DNAstring) - 3:
    codon = DNAstring[j:j+3]
    if data[codon] == "Stop":
        break
    elif codon == "AUG":
        started = True
        proteinString += data[codon]
    elif started:
        proteinString += data[codon]
    j += 3

write_file.write(proteinString)

read_file.close()
write_file.close()
table_file.close()
