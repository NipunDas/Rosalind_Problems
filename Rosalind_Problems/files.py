read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

lines = read_file.readlines()

i = 0

while i < len(lines):
    if (i+1) % 2 == 0:
        write_file.write(lines[i].strip() + "\n")
    i += 1

read_file.close()
write_file.close()