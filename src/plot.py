import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def run(HTSeq_results,figuredir):
	F = plt.figure()
	ax = F.add_subplot(111)
	ax.boxplot(HTSeq_results)
	plt.savefig(figuredir+'results.png')
