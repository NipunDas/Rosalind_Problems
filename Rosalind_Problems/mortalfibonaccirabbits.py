read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

data = read_file.readline().split()

n = int(data[0])
m = int(data[1])

month = 1
num_reproducing = 0
num_babies = 1
baby_data = []

while month < n:

    month += 1

    #storing baby data in an array
    baby_data.append(num_babies)
    temp = num_babies
    num_babies = num_reproducing

    #killing off rabbits that are too old
    if month > m:
        num_reproducing -= baby_data[month-m-1]

    num_reproducing += temp

write_file.write(str(num_reproducing + num_babies))

read_file.close()
write_file.close()