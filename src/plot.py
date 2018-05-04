import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from matplotlib.patches import Rectangle

def scatter_and_box(HTSeq_results,pvalue,foldchange,condition1,condition2,TF,figuredir):
	ax1 = plt.subplot2grid((4,6), (0,0), rowspan=4, colspan=4)
	ax2 = plt.subplot2grid((4,6), (0,5), rowspan=4)
	ax1.set_title(TF+', '+condition1+' vs. '+condition2, fontsize=16, loc='center')
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
	ax1.legend([extra],('p = '+roundedp,"x"),bbox_to_anchor=(0., 0.905, 1., 0.105), loc='upper left')
	
	ax2.boxplot(foldchange)
	#sets the limits to be inverse maximum absolute (so that they're the same positive and negative)
	ymin, ymax = ax2.get_ylim()
	if abs(ymax) > abs(ymin):
		ax2.set_ylim(ymax*-1,ymax)
	elif abs(ymax) < abs(ymin):
		ax2.set_ylim(ymin,ymin*-1)
	ax2.set_ylabel('log10('+condition2+'/'+condition1+')')
	
	plt.savefig(figuredir+TF+'_'+condition1+'_'+condition2+'.png')

def batch_foldchange(batchfoldchange,pvalues,batchcondition1,batchcondition2,TFs,figuredir):
	F = plt.figure()
	ax = F.add_subplot(111)
	ax.boxplot(batchfoldchange)
	#sets the limits to be the largest absolute value
	ymin, ymax = ax.get_ylim()
	if abs(ymax) > abs(ymin):
		ax.set_ylim(ymax*-1,ymax)
	elif abs(ymax) < abs(ymin):
		ax.set_ylim(ymin,ymin*-1)
	ax.set_ylabel('log10('+batchcondition2+'/'+batchcondition1+')')
	xpos = [n+1 for n in range(len(TFs))]
	#the following things add p value and median above each xtick on top of the plot
	roundedp = ['{:0.1e}'.format(x) for x in pvalues]
	medians = []
	bp_dict = ax.boxplot(batchfoldchange)
	for m in bp_dict['medians']:
		x, y = m.get_ydata()
		medians.append(y)
	roundedmedians = [str(np.round(n, 2)) for n in medians]
	for i in range(len(medians)):
		ax.text(xpos[i], ymax + (ymax*0.05), roundedmedians[i], horizontalalignment='center', fontsize=12)
		ax.text(xpos[i], ymax + (ymax*0.15), 'p='+roundedp[i], horizontalalignment='center', fontsize=12)
	#this xticks label command needs to be here or else there will be no x labels
	plt.xticks(xpos, TFs, fontsize=12)
	plt.savefig(figuredir+'batch_foldchange.png')