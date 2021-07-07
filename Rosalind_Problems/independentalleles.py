read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

data = read_file.readline().split()

#number of generations
k = int(data[0])

#N organisms (used for probability calculations)
N = int(data[1])

numChildren = 2**k

read_file.close()
write_file.close()
