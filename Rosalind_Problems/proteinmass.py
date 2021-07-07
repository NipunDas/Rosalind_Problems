read_file = open("input.txt", "r")
write_file = open("output.txt", "w")
table_file = open("monoisotopicmass.txt", "r")

lines = table_file.readlines()

protein_masses = {}
for line in lines:
    mass_data = line.strip().split()
    protein_masses[mass_data[0]] = float(mass_data[1])

#Adding mass of water
protein_masses["Water"] = 18.01056

proteinString = read_file.readline().strip()

totalMass = 0
for char in proteinString:
    totalMass += protein_masses[char]

#totalMass += protein_masses["Water"]
write_file.write(str(totalMass))

read_file.close()
write_file.close()
table_file.close()
