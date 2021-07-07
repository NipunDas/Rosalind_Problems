read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

string = read_file.readline().strip()

acount = 0
ccount = 0
gcount = 0
tcount = 0

for char in string:
    if char == "A":
        acount += 1
    elif char == "C":
        ccount += 1
    elif char == "G":
        gcount += 1
    elif char == "T":
        tcount += 1

write_file.write(str(acount) + " " + str(ccount) + " " + str(gcount) + " " + str(tcount))

read_file.close()
write_file.close()