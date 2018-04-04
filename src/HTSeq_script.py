#script for counting reads from sorted BAMs in intersected BEDs
import HTSeq
import numpy

def run(BED,BAMS1,BAMS2):
	sortedbamfile1rep1 = HTSeq.BAM_Reader(BAM1[0])
	sortedbamfile1rep2 = HTSeq.BAM_Reader(BAM1[1])
	sortedbamfile2rep1 = HTSeq.BAM_Reader(BAM2[0])
	sortedbamfile2rep2 = HTSeq.BAM_Reader(BAM2[1])
	bedfile = HTSeq.BED_Reader(BED) #this will probably work. If not, i need to parse it out myself
	
	counts1rep1 = numpy.zeros(len(bedfile))
	for i in range(len(bedfile)):
		region = bedfile[i]
		for almnt in sortedbamfile1rep1[region]:
	   		counts1rep1[i] += 1.0

	counts1rep2 = numpy.zeros(len(bedfile))
	for i in range(len(bedfile)):
		region = bedfile[i]
		for almnt in sortedbamfile1rep2[region]:
	   		counts1rep2[i] += 1.0

	counts2rep1 = numpy.zeros(len(bedfile))
	for i in range(len(bedfile)):
		region = bedfile[i]
		for almnt in sortedbamfile2rep1[region]:
	   		counts2rep1[i] += 1.0

	counts2rep2 = numpy.zeros(len(bedfile))
	for i in range(len(bedfile)):
		region = bedfile[i]
		for almnt in sortedbamfile2rep2[region]:
	   		counts2rep2[i] += 1.0

	counts1avg = [(x+y)/2.0 for x,y in zip(counts1rep1,counts1rep2)]
	counts2avg = [(x+y)/2.0 for x,y in zip(counts2rep1,counts2rep2)]