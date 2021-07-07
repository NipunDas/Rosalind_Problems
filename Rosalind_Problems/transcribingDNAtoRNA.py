read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

dnaString = read_file.readline().strip()

rnaString = ""

for char in dnaString:
    if char == "T":
        rnaString += "U"
    else:
        rnaString += char

write_file.write(rnaString)

read_file.close()
write_file.close()