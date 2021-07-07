read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

DNAstring1 = read_file.readline().strip()
DNAstring2 = read_file.readline().strip()

i = 0
count = 0

while i < len(DNAstring1):
    if DNAstring1[i] != DNAstring2[i]:
        count += 1
    i += 1

write_file.write(str(count))

read_file.close()
write_file.close()