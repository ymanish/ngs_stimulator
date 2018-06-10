


infile = open("aln_chr19.sam", 'r').readlines()

error = 0
total_reads = 0

outfile = open("aln_chr19_error.txt", 'w')
for line in infile[2:]:

	total_reads = total_reads + 1

	old_start = int(line.split("\t")[0].split(":")[2])
	new_start = int(line.split("\t")[3])-1
	if old_start != new_start:
		error = error +1

error_rate = (float(error)/total_reads)*100		
outfile.write("Total_reads = "+str(total_reads)+"\n")
outfile.write("Unaligned_reads = "+str(error)+"\n")
outfile.write("Error_rate ="+str(error_rate)+"\n")