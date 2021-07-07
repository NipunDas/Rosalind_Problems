read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

original = read_file.readline().strip()

reverse = ""
i = len(original) - 1

while i >= 0:
    reverse += original[i]
    i -= 1

reverseComplement = ""

for char in reverse:
    if char == "A":
        reverseComplement += "T"
    elif char == "T":
        reverseComplement += "A"
    elif char == "C":
        reverseComplement += "G"
    elif char == "G":
        reverseComplement += "C"

write_file.write(reverseComplement)

read_file.close()
write_file.close()