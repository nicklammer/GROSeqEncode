#HTSeq for foldchange only

import HTSeq
import math
from scipy import stats

def run(BED,BAMS1,BAMS2,mil_reads):
	sortedbamfile1rep1 = HTSeq.BAM_Reader(BAMS1[0])
	sortedbamfile1rep2 = HTSeq.BAM_Reader(BAMS1[1])
	sortedbamfile2rep1 = HTSeq.BAM_Reader(BAMS2[0])
	sortedbamfile2rep2 = HTSeq.BAM_Reader(BAMS2[1])
	
	bedfile = list()
	with open(BED) as F:
		for line in F:
			line = line.strip('\n').split('\t')
			chrom,start,stop = line[:3]
			start = int(start)
			stop = int(stop)
			if len(chrom) <= 5:
				#i added a window because it looked like we were missing peaks without it
				if start < 1000:
					bedfile.append(HTSeq.GenomicInterval(chrom,0,stop+1000,'.'))
				#normalizing for length below is not totally accurate because of this, but it's probably okay
				else:
					bedfile.append(HTSeq.GenomicInterval(chrom,start-1000,stop+1000,'.'))

	counts1rep1 = list()
	for region in bedfile:
		counts1rep1.append(0.0)
		length = region.length+2000
		for almnt in sortedbamfile1rep1[region]:
			counts1rep1[-1] += 1.0
		counts1rep1[-1] /= (length/1000.0)
		counts1rep1[-1] /= mil_reads[0][0]

	counts1rep2 = list()
	for region in bedfile:
		counts1rep2.append(0.0)
		length = region.length+2000
		for almnt in sortedbamfile1rep2[region]:
			counts1rep2[-1] += 1.0
		counts1rep2[-1] /= (length/1000.0)
		counts1rep2[-1] /= mil_reads[0][1]

	counts2rep1 = list()
	for region in bedfile:
		counts2rep1.append(0.0)
		length = region.length+2000
		for almnt in sortedbamfile2rep1[region]:
			counts2rep1[-1] += 1.0
		counts2rep1[-1] /= (length/1000.0)
		counts2rep1[-1] /= mil_reads[1][0]

	counts2rep2 = list()
	for region in bedfile:
		counts2rep2.append(0.0)
		length = region.length+2000
		for almnt in sortedbamfile2rep2[region]:
			counts2rep2[-1] += 1.0
		counts2rep2[-1] /= (length/1000.0)
		counts2rep2[-1] /= mil_reads[1][1]

	counts1avg = [(x+y)/2.0 for x,y in zip(counts1rep1,counts1rep2)]
	counts2avg = [(x+y)/2.0 for x,y in zip(counts2rep1,counts2rep2)]
	#log10 but excludes 0 (removes both entries)
	counts1avgclean = counts1avg
	counts2avgclean = counts2avg
	#so i decided to find any zero in the first list and make it zero in the second list, then clean it up after
	for i in range(len(counts1avg)):
		if counts1avg[i] == 0.0:
			counts2avgclean[i] = 0.0
		elif counts2avg[i] == 0.0:
			counts1avgclean[i] = 0.0
	counts1avgclean = [x for x in counts1avgclean if x!=0.0]
	counts2avgclean = [x for x in counts2avgclean if x!=0.0]

	KStest = stats.ks_2samp(counts1avgclean,counts2avgclean)
	
	#fold change
	foldchange = []
	for i in range(len(counts2avg)):
		try:
			foldchange.append(counts2avg[i]/counts1avg[i])
		except:
			pass

	foldchangelog = []
	for x in foldchange:
		try:
			foldchangelog.append(math.log10(x))
		except:
			pass

	return [KStest, foldchangelog]