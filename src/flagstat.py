#samtools flagstat script

import os

def flagstat(BAMS1, BAMS2, outdir):
	count1 = 0
	count2 = 0
	millions_mapped_reads1 = []
	millions_mapped_reads2 = []
	for x in BAMS1:
		outfile = outdir + 'samtools_output_BAMS1_' + str(count1) + '.txt'
		os.system("samtools flagstat " + x + " > " + outfile) #idk how to output a file
		with open(outfile) as F:
			lines = F.readlines()
			millions_mapped_reads1.append(float(lines[4].strip('\n').split()[0])/1000000.0)
		count1 += 1
	for x in BAMS2:
		outfile = outdir + 'samtools_output_BAMS2_' + str(count2) + '.txt'
		os.system("samtools flagstat " + x + " > " + outfile) #idk how to output a file
		with open(outfile) as F:
			lines = F.readlines()
			millions_mapped_reads2.append(float(lines[4].strip('\n').split()[0])/1000000.0)
		count2 += 1

	return [millions_mapped_reads1,millions_mapped_reads2]