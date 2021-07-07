read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

DNAstring = read_file.readline().strip()
motif = read_file.readline().strip()

i = 0
while i <= len(DNAstring) - len(motif):
    if DNAstring[i:i+len(motif)] == motif:
        write_file.write(str(i+1) + " ")
    i += 1

read_file.close()
write_file.close()