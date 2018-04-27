import os
import config
import intersect
import flagstat
import HTSeq_script
import plot

#Return parent directory
def parent_dir(directory):
	pathlist = directory.split('/')
	newdir = '/'.join(pathlist[0:len(pathlist)-1])

	return newdir

def run():
	#Home directory
	homedir = os.path.dirname(os.path.realpath(__file__))
	filedir = parent_dir(homedir)+'/temp_files/'
	figuredir = parent_dir(homedir)+'/figures/'
	chipfile = filedir + 'rep_intersect.bed'

	BAMS1 = config.BAMS1
	BAMS2 = config.BAMS2
	BEDS = config.BEDS
	
	intersect.bedtools_intersect(BEDS,filedir)

	million_reads = flagstat.flagstat(BAMS1,BAMS2,filedir)

	HTSeq_results = HTSeq_script.run(chipfile,BAMS1,BAMS2,million_reads)

	outfile = open(filedir+'results.txt','w')
	for list1 in HTSeq_results:
		list1 = [str(x) for x in list1]
		outfile.write('\t'.join(list1)+'\n')
	HTSeq_results_counts = [HTSeq_results[0],HTSeq_results[1]]
	HTSeq_results_pvalue = HTSeq_results[2][1]
	HTSeq_results_foldchange = HTSeq_results[3]
	
	#plot.plot1(HTSeq_results_plot1,figuredir)
	#plot.foldchange(HTSeq_results_foldchange,figuredir)
	#plot.scatter(HTSeq_results_plot1,figuredir)
	plot.scatter_and_box(HTSeq_results_counts,HTSeq_results_pvalue,HTSeq_results_foldchange,figuredir)



if __name__ == "__main__":
	run()