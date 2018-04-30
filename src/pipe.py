#bedtools, HTSeq, and plot in one script
import config
import intersect
import flagstat
import HTSeq_script
import HTSeq_foldchange

def run(BEDS,BAMS1,BAMS2,index,million_reads,outdir,chipfile):

	intersect.bedtools_intersect(BEDS,outdir,index)

	batchfoldchange = HTSeq_foldchange.run(chipfile,BAMS1,BAMS2,million_reads)
	
	return batchfoldchange