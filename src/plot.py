import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from matplotlib.patches import Rectangle

def scatter_and_box(HTSeq_results,pvalue,foldchange,condition1,condition2,TF,figuredir):
	ax1 = plt.subplot2grid((4,6), (0,0), rowspan=4, colspan=4)
	ax2 = plt.subplot2grid((4,6), (0,5), rowspan=4)
	ax1.set_title(TF+', '+condition1+' vs. '+condition2, fontsize=16, loc='right')
	#colors dots by density
	xy = np.vstack([HTSeq_results[0],HTSeq_results[1]])
	z = gaussian_kde(xy)(xy)
	#sorts by density so dense ones are on top
	idx = z.argsort()
	x = []
	y = []
	z_sorted = []
	for i in idx:
		x.append(HTSeq_results[0][i])
		y.append(HTSeq_results[1][i])
		z_sorted.append(z[i])
	ax1.scatter(x, y, c=z_sorted, edgecolor='')
	ax1.set_xlabel('log10(FPKM) '+condition1)
	ax1.set_ylabel('log10(FPKM) '+condition2)
	#this is to get a y=x line
	lims = [np.min([ax1.get_xlim(), ax1.get_ylim()]), np.max([ax1.get_xlim(), ax1.get_ylim()])]
	ax1.plot(lims, lims, 'k-', alpha=0.75, zorder=1)
	ax1.set_aspect('equal')
	ax1.set_xlim(lims)
	ax1.set_ylim(lims)
	#adds the p-value as a legend
	roundedp = '{:0.1e}'.format(pvalue)
	extra = Rectangle((0, 0), 50, 50, fc="none", fill=False, edgecolor='none', linewidth=0)
	ax1.legend([extra],('p = '+roundedp,"x"),bbox_to_anchor=(0., 1.02, 1., 0.102), loc='upper left')
	
	ax2.boxplot(foldchange)
	#sets the limits to be inverse maximum absolute
	ymin, ymax = ax2.get_ylim()
	if abs(ymax) > abs(ymin):
		ax2.set_ylim(ymax*-1,ymax)
	elif abs(ymax) < abs(ymin):
		ax2.set_ylim(ymin,ymin*-1)
	ax2.set_ylabel('log10('+condition2+'/'+condition1+')')
	
	plt.savefig(figuredir+TF+'_'+condition1+'_'+condition2+'.png')

def batch_foldchange(batchfoldchange,batchcondition1,batchcondition2,TFs,figuredir):
	F = plt.figure()
	ax = F.add_subplot(111)
	ax.boxplot(batchfoldchange)
	#sets the limits to be the largest absolute value
	ymin, ymax = ax2.get_ylim()
	if abs(ymax) > abs(ymin):
		ax2.set_ylim(ymax*-1,ymax)
	elif abs(ymax) < abs(ymin):
		ax2.set_ylim(ymin,ymin*-1)
	ax2.set_ylabel('log10('+batchcondition2+'/'+batchcondition1+')')
	plt.xticks(range(len(TFs)), TFs)
	plt.savefig(figuredir+'batch_foldchange.png')