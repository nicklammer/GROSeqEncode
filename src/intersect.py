#bedtools intersect

def bedtools_intersect(BEDS,outdir):
	outfile = outdir + 'rep_intersect.bed'
	os.system("bedtools intersect -a " + BEDS[0] + " -b " + ' '.join(BEDS[1:]) + " > " + outfile)
