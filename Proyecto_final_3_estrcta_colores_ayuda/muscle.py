###############################################################################
from subprocess import Popen, PIPE
from Bio import Seq
from Bio import SeqIO
import pandas as pd
import sys
import os

import Extractor_secuencias_genbank as E

#Esta funcion la utilizamos para contar cuantos query se nos introduce en el fasta
#así como para generar archivos secuencia_1, _2, _3... separando las distintas 
#querys que nos entran.
def Cuantas_query(fasta):

	global n_query
	global nombres_querys
	global secuencias_query
	secuencias_query=[]
	nombres_querys=[]
	n_query=0

	with open(fasta) as input_handle:
		for record in SeqIO.parse(input_handle, "fasta"):
			nombres_querys.append(str(record.id)+" "+str(record.name))
			secuencias_query.append(str(record.seq))
			n_query += 1 #Cuenta el numero de id de secuencia en el archivo.
	input_handle.close()

	for i in range (1, n_query+1):
		E.Si_existe_me_lo_cargo_dir("results/sec_"+str(i))
		os.mkdir("results/sec_"+str(i))

	for i in range (1, n_query+1):
		f=open("results/sec_"+str(i)+"/secuencia_"+str(i),"w")
		f.write(">"+ str(nombres_querys[i-1]) + "\n")
		f.write(str(secuencias_query[i-1]) + "\n")


#Con esta funcion preparamos el fasta que luego introduciremos al muscle
def Fasta_del_muscle(doc):
	datos=pd.read_csv(doc,sep="\s+",header=0) #Vemos que hits cumplen nuestro filtro
	resultante=doc.replace("pares_muscle_","set_sequences_muscle_secuencia_")
	if os.path.exists(resultante):
		f = open(resultante,"a")
	else:
		f = open(resultante,"w")
	with open('results/database.fasta') as input_handle:
		for record in SeqIO.parse(input_handle, "fasta"):
			for i in datos["Subject"]: #Introducimos esos hits en formato fasta en unarchivo
				if i == record.id:
					f.write(">"+ str(record.id) + " "+ str(record.name)+ "\n")
					f.write(str(record.seq) + "\n")
	direc_query=resultante.replace("set_sequences_muscle_secuencia_","secuencia_")
	f2 = open(direc_query,"r")
	f2lectura=f2.read()
	f.write(f2lectura)



def Hacer_alineamiento_muscle(doc):
	resultante=doc.replace("set_sequences_muscle_secuencia_",
							"muscle_alignment_secuencia_")
	proceso = Popen(['muscle','-in',doc,
					'-out',resultante ],
					stdout=PIPE, stderr=PIPE)
	error_encontrado = proceso.stderr.read()
	alineamiento_muscle = proceso.stdout.read()

	proceso.stderr.close()
	proceso.stdout.close()

	my_error = open("results/log","w")
	my_error.write(error_encontrado.decode('utf-8'))
	my_error.close()

	print("\x1b[0;37m"+
		"El alineamiento del muscle se ha almacenado en '" +
		"\x1b[1;33m"+ resultante +
		"\x1b[0;37m"+"'.")


def Hacer_arbol_NJ(doc):
	resultante=doc.replace("muscle_alignment_secuencia_",
							"arbol_secuencia_")
	resultante=resultante+".phy"
	proceso = Popen(['muscle','-maketree', '-in',
					doc,'-out', resultante,
					'-cluster','neighborjoining' ],
					stdout=PIPE, stderr=PIPE)
	error_encontrado = proceso.stderr.read()
	arbol_muscle = proceso.stdout.read()

	proceso.stderr.close()
	proceso.stdout.close()

	my_error = open("results/log","w")
	my_error.write(error_encontrado.decode('utf-8'))
	my_error.close()

	print("\x1b[0;37m"+
		"El arbol Neighbor-Joining se ha almacenado en '"+
		"\x1b[1;33m"+ resultante +
		"\x1b[0;37m"+"'.")