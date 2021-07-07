read_file = open("input.txt", "r")
write_file = open("output.txt", "w")
table_file = open("RNAcodontable.txt", "r")

lines = table_file.readlines()

data = {}
for line in lines:
    words = line.strip().split()
    i = 0
    while i < len(words) - 1:
        if not(words[i+1] in data.keys()):
            data[words[i+1]] = []
        data[words[i+1]].append(words[i])
        i += 1

proteinString = read_file.readline().strip()

combinations = 1

for char in proteinString:
    combinations *= len(data[char])
    combinations = combinations % 1000000

combinations *= len(data["Stop"])
combinations = combinations % 1000000

write_file.write(str(combinations))

read_file.close()
write_file.close()
table_file.close()