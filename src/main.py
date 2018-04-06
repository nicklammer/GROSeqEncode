import os
import config
import intersect
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

	# print("HTSeq test run using 0 min time point")

	BAMS1 = config.BAMS1
	BAMS2 = config.BAMS2
	BEDS = config.BEDS
	intersect.bedtools_intersect(BEDS,filedir)

	HTSeq_results = HTSeq_script.run(chipfile,BAMS1,BAMS2)

	outfile = open(filedir+'results.txt','w')
	for list1 in HTSeq_results:
		list1 = [str(x) for x in list1]
		outfile.write('\t'.join(list1)+'\n')

	plot.run(HTSeq_results,figuredir)
	



if __name__ == "__main__":
	run()