import os
import some_script
import config

def run():
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
