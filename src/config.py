outdir = '../temp_files/'
#put in directory for BAM files. Currently scripts only accept 2 replicates.
BAMS1 = ['/scratch/Users/nila7826/GROSeq/JR_rep1/J52_trimmed.flip.fastq.bowtie2.sorted.bam','/scratch/Users/nila7826/GROSeq/JR_rep2/J5D451_GTCCGC_S3_L007and8_R1_001_trimmed.flip.fastq.bowtie2.sorted.bam']
BAMS2 = ['/scratch/Users/nila7826/GROSeq/JR_rep1/J62_trimmed.flip.fastq.bowtie2.sorted.bam','/scratch/Users/nila7826/GROSeq/JR_rep2/J6C451_GTGAAA_S4_L007and8_R1_001_trimmed.flip.fastq.bowtie2.sorted.bam']
#using 'single' for 1 TF or 'batch' for 2+
option = 'batch'
#config for 1 TF
BEDS = ['/scratch/Users/nila7826/ENCODE/JUND/ENCFF833ZRV.bed','/scratch/Users/nila7826/ENCODE/JUND/ENCFF973IDD.bed']
TF = 'JUND'
condition1 = 'DMSO'
condition2 = '+CA'
#config for 2+ TFs
#enter TFs as strings
TFs = ['SRF','JUND','ATF3','EGR1','FOSL1','MAX']
#the BED files here need to be a list of lists in order of the TFs in the TFs list
batchBEDs = [['/scratch/Users/nila7826/ENCODE/SRF/ENCFF001UEM.bed','/scratch/Users/nila7826/ENCODE/SRF/ENCFF001UEN.bed'],
			['/scratch/Users/nila7826/ENCODE/JUND/ENCFF833ZRV.bed','/scratch/Users/nila7826/ENCODE/JUND/ENCFF973IDD.bed'],
			['/scratch/Users/nila7826/ENCODE/ATF3/ENCFF001UDK.bed','/scratch/Users/nila7826/ENCODE/ATF3/ENCFF001UDL.bed'],
			['/scratch/Users/nila7826/ENCODE/EGR1/ENCFF001UDS.bed','/scratch/Users/nila7826/ENCODE/EGR1/ENCFF001UDT.bed'],
			['/scratch/Users/nila7826/ENCODE/FOSL1/ENCFF001UDW.bed','/scratch/Users/nila7826/ENCODE/FOSL1/ENCFF001UDX.bed'],
			['/scratch/Users/nila7826/ENCODE/MAX/ENCFF001UEA.bed','/scratch/Users/nila7826/ENCODE/MAX/ENCFF001UEB.bed'],
			#['/scratch/Users/nila7826/ENCODE/CTCF/ENCFF562WIV.bed','/scratch/Users/nila7826/ENCODE/CTCF/ENCFF944AQH.bed'],
			#['/scratch/Users/nila7826/ENCODE/H3K27ac/ENCFF079KEX.bed','/scratch/Users/nila7826/ENCODE/H3K27ac/ENCFF567LZS.bed'],
			]
batchcondition1 = 'DMSO'
batchcondition2 = '+CA'