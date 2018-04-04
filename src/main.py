import os
import some_script
import config
import intersect
import HTSeq_script

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

	htseq_results = HTSeq_script.run(chipfile,BAMS1,BAMS2)

	#plot.run(htseq_results,figuredir)



	print("hello world")
	some_script.execute()


def parse_tab_delimited_file(file1):
	with open(file1) as F:
		for line in F:
			line = line.strip('\n').split('\t')
			#line will be a list of the columns of your file
			chrom,start,stop = line

#Takes as input a list of bed files (full path)
def bedtools_intersect(BEDS,outdir):
	command = "bedtools intersect -a " + BEDS[0] + " -b " + ' '.join(BEDS[1:])
	print(command)
	outfile = outdir+'rep_intersect.bed'
	#os.system("bedtools intersect -a " + BEDS[0] + " -b " + ' '.join(BEDS[1:] + " > " + outfile)

if __name__ == "__main__":
	print("hello different world")
	run()
	os.system("ls")
	print(config.BEDS)
	a = "hello"
	print(a+" world2")
	outdir = '../temp_files/'
	bedtools_intersect(config.BEDS,outdir)
