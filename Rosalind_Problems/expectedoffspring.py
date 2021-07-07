read_file = open("input.txt", "r")
write_file = open("output.txt", "w")

data = read_file.readline().split()

genes = ["AA-AA", "AA-Aa", "AA-aa", "Aa-Aa", "Aa-aa", "aa-aa"]

#calculates percent of children that have the dominant genotype on average and thus display the dominant phenotype
def calculatePercent(genotype):
    count = 0
    if genotype[0].isupper() or genotype[3].isupper():
        count += 1
    if genotype[0].isupper() or genotype[4].isupper():
        count += 1
    if genotype[1].isupper() or genotype[3].isupper():
        count += 1
    if genotype[1].isupper() or genotype[4].isupper():
        count += 1
    
    return float(count)/4

#adding up all the percentages (multiplying by 2 b/c each couple produces 2 offspring)
total = 0
i = 0

for genotype in genes:
    total += (calculatePercent(genotype) * int(data[i]))
    i += 1

total *= 2

write_file.write(str(total))

read_file.close()
write_file.close()