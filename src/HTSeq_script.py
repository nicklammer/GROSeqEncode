#script for counting reads from sorted BAMs in intersected BEDs
import HTSeq
import numpy

def run(BED,BAMS1,BAMS2):
	sortedbamfile1rep1 = HTSeq.BAM_Reader(BAMS1[0])
	sortedbamfile1rep2 = HTSeq.BAM_Reader(BAMS1[1])
	sortedbamfile2rep1 = HTSeq.BAM_Reader(BAMS2[0])
	sortedbamfile2rep2 = HTSeq.BAM_Reader(BAMS2[1])
	# bedfile = HTSeq.BED_Reader(BED) #this will probably work. If not, i need to parse it out myself

	bedfile = list()
	with open(BED) as F:
		for line in F:
			line = line.strip('\n').split('\t')
			chrom,start,stop = line[:3]
			bedfile.append(HTSeq.GenomicInterval(chrom,int(start),int(stop),'.'))


	print bedfile[:10]
	
	counts1rep1 = list()
	# counts1rep1 = numpy.zeros(len(bedfile))
	for region in bedfile:
		# region = bedfile[i]
		counts1rep1.append(0.0)
		for almnt in sortedbamfile1rep1[region]:
			counts1rep1[-1] += 1.0

	counts1rep2 = list()
	for region in bedfile:
		counts1rep2.append(0.0)
		for almnt in sortedbamfile1rep2[region]:
			counts1rep2[-1] += 1.0

	counts2rep1 = list()
	for region in bedfile:
		counts2rep1.append(0.0)
		for almnt in sortedbamfile2rep1[region]:
			counts2rep1[-1] += 1.0

	counts2rep2 = list()
	for region in bedfile:
		counts2rep2.append(0.0)
		for almnt in sortedbamfile2rep2[region]:
			counts2rep2[-1] += 1.0

	counts1avg = [(x+y)/2.0 for x,y in zip(counts1rep1,counts1rep2)]
	counts2avg = [(x+y)/2.0 for x,y in zip(counts2rep1,counts2rep2)]

	return [counts1avg, counts2avg]