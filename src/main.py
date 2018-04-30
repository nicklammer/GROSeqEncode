import os
import config
import intersect
import flagstat
import HTSeq_script
import HTSeq_foldchange
import plot
import pipe

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

	option = config.option
	BAMS1 = config.BAMS1
	BAMS2 = config.BAMS2
	million_reads = flagstat.flagstat(BAMS1,BAMS2,filedir)
	
	if option == 'single':
		chipfile = filedir + 'rep_intersect_0.bed'
		BEDS = config.BEDS
		condition1 = config.condition1
		condition2 = config.condition2
		TF = config.TF
		index = 0

		intersect.bedtools_intersect(BEDS,filedir,index)
		HTSeq_results = HTSeq_script.run(chipfile,BAMS1,BAMS2,million_reads)

		outfile = open(filedir+'results.txt','w')
		for list1 in HTSeq_results:
			list1 = [str(x) for x in list1]
			outfile.write('\t'.join(list1)+'\n')

		HTSeq_results_counts = [HTSeq_results[0],HTSeq_results[1]]
		HTSeq_results_pvalue = HTSeq_results[2][1]
		HTSeq_results_foldchange = HTSeq_results[3]

		plot.scatter_and_box(HTSeq_results_counts,HTSeq_results_pvalue,HTSeq_results_foldchange,condition1,condition2,TF,figuredir)

	elif option == 'batch':
		TFs = config.TFs
		batchBEDs = config.batchBEDs
		batchcondition1 = config.batchcondition1
		batchcondition2 = config.batchcondition2
		batchfoldchange = []

		for i in range(len(TFs)):
			chipfile = filedir + 'rep_intersect_'+str(i)+'.bed'
			#batchfoldchange.append(pipe.run(batchBEDs[i],BAMS1,BAMS2,i,million_reads,filedir,chipfile))
			intersect.bedtools_intersect(batchBEDs[i],filedir,i)
			batchfoldchange.append(HTSeq_foldchange.run(chipfile,BAMS1,BAMS2,million_reads))
		
		plot.batch_foldchange(batchfoldchange,batchcondition1,batchcondition2,TFs,figuredir)


	else:
		print ("Type 'single' or 'batch' in the config > option line")



if __name__ == "__main__":
	run()