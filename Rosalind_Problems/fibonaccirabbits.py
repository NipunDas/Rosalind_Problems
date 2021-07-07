read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

line = read_file.readline().strip()

data = line.split(" ")

n = int(data[0])
k = int(data[1])

num_reproducing = 0
num_babies = 1
month = 1

while month < n:
    temp = num_babies
    num_babies = num_reproducing * k
    num_reproducing += temp
    month += 1

write_file.write(str(num_reproducing + num_babies))

read_file.close()
write_file.close()