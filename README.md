# ngs_stimulator
Run generate_ngs_reads.py script to get the reads. I used only one chromosome to reduce the computational time. This script takes input as chr19.fa file which is downloaded from ucsc genome browser.

Then run "bwa index chr19.fa"
Then run "bwa mem chr19.fa output_chr19.fastq > aln_chr19.sam"

Run estimate_aln_error.py script to get the error rate for the alignment of reads against the chr19 only. 
