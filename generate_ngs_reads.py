from Bio import SeqIO
import random
from random import randint
import re

#Quality encoding: !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI
def mutations(norm_read):
	mut_position = randint(0,49)
	nuc_string = ['A','G','C','T']
	return norm_read[:mut_position]+nuc_string[randint(0,3)]+norm_read[mut_position+1:]
	

outfile = open("output_chr19.fastq", 'w')
for seq_record in SeqIO.parse("chr19.fa", "fasta"):
	human_geno = seq_record.seq
	#break
	
two_reads = []
temp = []
for i in range(100000):
	
	read_start = randint(0,len(human_geno))
	read_end = read_start+50
	
	read = ""
	for j in str(human_geno)[read_start:read_end]:
		read = read + j.upper()
	
	
	
	
	###since the mutations rate is 0.01 which means that out of 100 nucleotides one is wrong. For this I selected randomly one of the two consecutive sequences and then randomly mutate one of the position.
	if len(two_reads)>1:
		mut_read_number = randint(0,1)
		mut_read = mutations(two_reads[mut_read_number][2])
		mut_read_start = two_reads[mut_read_number][0]
		mut_read_end = two_reads[mut_read_number][1]
		
		other_read = two_reads[mut_read_number-1]
		#two_reads = []
		#print two_reads
		#print mut_read
		#print other_read
		
		quality = '!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHI'
		quality_mut_read = ""
		for k in range(50):
			quality_mut_read = quality_mut_read + random.choice(quality)
		
		quality_other_read = ""
		for m in range(50):
			quality_other_read = quality_other_read + random.choice(quality)
		
		
		outfile.write('@seq'+str(i-1)+':'+'chr19:'+str(mut_read_start)+':'+str(mut_read_end)+'\n'+mut_read+'\n'+'+\n'+quality_mut_read+'\n')
		
		outfile.write('@seq'+str(i)+':'+'chr19:'+str(other_read[0])+':'+str(other_read[1])+'\n'+other_read[2]+'\n'+'+\n'+quality_other_read+'\n')
		
		
		
		two_reads = []
		temp.append(read_start)
		temp.append(read_end)
		temp.append(read)
		two_reads.append(temp)
		temp = []
		#break
		
		
		
	
	else:
		temp.append(read_start)
		temp.append(read_end)
		temp.append(read)
		two_reads.append(temp)
		temp = []
		
	
mut_read_number = randint(0,1)
mut_read = mutations(two_reads[mut_read_number][2])
mut_read_start = two_reads[mut_read_number][0]
mut_read_end = two_reads[mut_read_number][1]
	
other_read = two_reads[mut_read_number-1]
#two_reads = []
#print two_reads
#print mut_read
#print other_read
quality = '!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHI'
quality_mut_read = ""
for k in range(50):
	quality_mut_read = quality_mut_read + random.choice(quality)
		
quality_other_read = ""
for m in range(50):
	quality_other_read = quality_other_read + random.choice(quality)
		
		
outfile.write('@seq'+str(i-1)+':'+'chr19:'+str(mut_read_start)+':'+str(mut_read_end)+'\n'+mut_read+'\n'+'+\n'+quality_mut_read+'\n')

outfile.write('@seq'+str(i)+':'+'chr19:'+str(other_read[0])+':'+str(other_read[1])+'\n'+other_read[2]+'\n'+'+\n'+quality_other_read+'\n')	
		
		