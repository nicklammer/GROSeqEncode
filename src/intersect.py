#bedtools intersect
import os

def bedtools_intersect(BEDS,outdir,index):
	outfile = outdir + 'rep_intersect_'+str(index)+'.bed'
	os.system("bedtools intersect -a " + BEDS[0] + " -b " + ' '.join(BEDS[1:]) + " > " + outfile)
