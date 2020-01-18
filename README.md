# blast_muscle_PROSITE
This is my programme developed as my Final Proyect for the subject Programming for bioinformatics.

The main objective of the Final Proyect for the subject Programming for bioinformatics was to create a programme that could analyse one or more sequences (given in fasta format). This programme had to do a blast between the sequences given and the sequences forming the genbank (or genbanks) also given. And with this result it should do a muscle alignment, a phylogenetic tree (Neighbor-Joining) and also identify all the PROSITE domains in the sequences.

I tried to upload all the files separately so that they could be seen without downloading them, but one of them ('prosite.dat') was too big to upload.

The programme has been developed in Python 3 and it has been designed to be executed in command line (Ubuntu).

The programme import these modules: os, sys, subprocess, Bio, pandas and re. It would also use blasp and muscle. So they should be installed in order to get a good running.

For the execution of the programme you should itroduce the file which contains the sequences you want to analyse and the genbanks you want to use in the folder downloaded.Then, in command line, you should write python main.py followed by first, the name of the file that contains the sequence(s) and then the name of the genbank(s).  
