import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from matplotlib.patches import Rectangle

def plot1(HTSeq_results,figuredir):
	F = plt.figure()
	ax = F.add_subplot(111)
	ax.boxplot(HTSeq_results)
	ax.set_ylabel('log10(FPKM)?')
	ax.set_xlabel('Time after serum (min)')
	plt.xticks([1,2], ['0','45']) #will need to integrate this into config
	plt.savefig(figuredir+'results.png')

def foldchange(foldchange,figuredir):
	F = plt.figure()
	ax = F.add_subplot(111)
	ax.boxplot(foldchange)
	ax.set_ylabel('log10(Fold Change)')
	#ax.set_xlabel('Region?')
	plt.savefig(figuredir+'foldchange.png')

def scatter(HTSeq_results,figuredir):
	F = plt.figure()
	ax = F.add_subplot(111)
	ax.scatter(HTSeq_results[0],HTSeq_results[1], c='b')
	ax.set_xlabel('log10(FPKM) at 0 min')
	ax.set_ylabel('log10(FPKM) at 45 min')
	lims = [np.min([ax.get_xlim(), ax.get_ylim()]), np.max([ax.get_xlim(), ax.get_ylim()])]
	ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
	ax.set_aspect('equal')
	ax.set_xlim(lims)
	ax.set_ylim(lims)
	plt.savefig(figuredir+'scatter.png')

def scatter_and_box(HTSeq_results,pvalue,foldchange,figuredir):
	ax1 = plt.subplot2grid((4,6), (0,0), rowspan=4, colspan=4)
	ax2 = plt.subplot2grid((4,6), (0,5), rowspan=4)
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
	ax1.set_xlabel('log10(FPKM) at 0 min')
	ax1.set_ylabel('log10(FPKM) at 45 min')
	#this is to get a y=x line
	lims = [np.min([ax1.get_xlim(), ax1.get_ylim()]), np.max([ax1.get_xlim(), ax1.get_ylim()])]
	ax1.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
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
	ax2.set_ylabel('log10(Fold Change)')
	
	plt.savefig(figuredir+'scatter_and_box.png')