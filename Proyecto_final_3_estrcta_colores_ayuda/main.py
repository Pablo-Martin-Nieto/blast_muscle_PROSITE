###############################################################################
import os
import sys
import time

import Extractor_secuencias_genbank as E
import blastp as B
import ayuda as A
import muscle as M
import prosite as P


n_argmtos=len(sys.argv)
for i in sys.argv:
	if (i == "-h" or
		i == "-help"):
		A.ayuda()
		sys.exit()
	
if n_argmtos<3:
	A.error_inicio()
	sys.exit()
else:
	#Crea carpeta resutado y obliga a cambiar de nombre en caso de que ya exista una
	if os.path.exists("results"):
		while True:
			print("\x1b[0;37m"+
				"El documento 'results' ya existe.")
			print("\x1b[0;37m"+
				"Para continuar debe cambiar dicha carpeta de nombre.")
			nombre_nuevo=str(input("\x1b[1;32m"+
				"¿Cual desea que sea el nuevo nombre?: "))
			try:
				os.rename("results", nombre_nuevo)
				os.mkdir("results")
				break
			except:
				print("\x1b[1;31m"+
					"No se ha podidio realizar ese cambio de nombre. Pruebe con otro nombre. ")
	

	print("\x1b[0;37m"+
		"\n------------------- BIENVENIDO AL USO DEL PROGRAMA -------------------\n")
	E.Si_existe_me_lo_cargo_doc("results/database.fasta")
	if n_argmtos==3: #Si solo metemos un genbank 
		query=sys.argv[1]
		genbank=sys.argv[2]
		E.Extractor_secuencias_genbank(genbank)
		print("\x1b[0;37m"+
			"Se están extrayendo las secuencias de su Genbank: " + 
			"\x1b[1;33m"+ genbank)
		#time.sleep(2)
		print("\x1b[0;37m"+
			"Las secuencias se han introducido en el fichero "+
			"\x1b[1;33m"+
			"'results/database.fasta'")
		print("")
	elif n_argmtos>3: #Si metemos más de un genbank
		query=sys.argv[1]
		for j in range(2,n_argmtos):
			genbank_j=sys.argv[j]
			E.Extractor_secuencias_genbank(genbank_j)
			print("\x1b[0;37m"+
				"Se están extrayendo las secuencias de su Genbank: " + 
				"\x1b[1;33m"+genbank_j)
			#time.sleep(2)
			print("\x1b[0;37m"+
				"Las secuencias se han introducido en el fichero "+
				"\x1b[1;33m"+
				"'results/database.fasta'")
		print("")
M.Cuantas_query(query)
print("\x1b[0;37m"+
	"En el archivo fasta que ha introducido hay " + 
	"\x1b[1;33m"+str(M.n_query)+ 
	"\x1b[0;37m"+" secuencia/s.")
print("\x1b[0;37m"+
	"El análisis se hará utilizando como querys:")
for i in range (1, M.n_query+1):
	print("\x1b[1;33m"+"\t-"+M.nombres_querys[i-1])
print("\n")
B.Solicitar_datos_filtrado() #Pide datos del filtrado
for i in range (1, M.n_query+1): #Análisis completo para cada una de las secuencias introducidas en el fasta

	print("\x1b[0;37m"+
		"\n----------COMIENZA EL ANÁLISIS PARA LA SECUENCIA "+ str(M.nombres_querys[i-1])+"----------")
	print("\n------------------- SE PROCEDERA A REALIZAR EL BLAST -------------------\n")
	B.Blastp("results/sec_"+str(i)+"/secuencia_"+
		str(i),"results/database.fasta") #Hace el blast
	print("\x1b[0;37m"+
		"\n------------------- SE PROCEDERA A REALIZAR EL MUSCLE -------------------\n")
	M.Fasta_del_muscle("results/sec_"+str(i)+
		"/pares_muscle_"+str(i))
	M.Hacer_alineamiento_muscle("results/sec_"+str(i)+
		"/set_sequences_muscle_secuencia_"+str(i))
	M.Hacer_arbol_NJ("results/sec_"+str(i)+
		"/muscle_alignment_secuencia_"+str(i))
	print("\x1b[0;37m"+
		"\n------------------- SE PROCEDERA A BUSCAR LOS DOMINIOS DE PROSITE EN LOS HITS-------------------\n")
	P.Identificador_dominios("results/sec_"+str(i)+
		"/set_sequences_muscle_secuencia_"+str(i), str(i))



