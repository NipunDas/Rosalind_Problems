read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

string = read_file.readline().strip()

words = string.split(" ")

dict = {}

for word in words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    dict[word] = count

for key, value in dict.items():
    write_file.write(key + " " + str(value) + "\n")

read_file.close()
write_file.close()