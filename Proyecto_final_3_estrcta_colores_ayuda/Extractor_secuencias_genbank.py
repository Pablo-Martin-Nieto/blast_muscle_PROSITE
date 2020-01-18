###############################################################################
import sys
import os
from Bio import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_protein

def Extractor_secuencias_genbank(genbank):
	if os.path.exists("results/database.fasta"):
		f = open("results/database.fasta","a")
	else:
		f = open("results/database.fasta","w")
	with open(genbank) as input_handle:
		for record in SeqIO.parse(input_handle, "genbank"):
			for feature in record.features:
				if feature.type == "CDS":
					d=feature.qualifiers
					for k in d.items():
						if (k[0]=="protein_id"):
							f.write(">"+ k[1][0] + "\n")
						if (k[0]=="translation"):
							f.write(k[1][0]+"\n")
	f.close()

def Si_existe_me_lo_cargo_doc(direccion):
	if os.path.exists(direccion):
		os.remove(direccion)

def Si_existe_me_lo_cargo_dir(direccion):
	if os.path.exists(direccion):
		os.rmdirs(direccion)