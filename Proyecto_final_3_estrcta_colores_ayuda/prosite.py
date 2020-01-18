###############################################################################
import os
import re
from Bio import Seq
from Bio import SeqIO
from Bio.ExPASy import Prosite,Prodoc

def Identificador_dominios(doc,n):#El introducir el archivo como parametro lo hacemos para pasarle la i
	direcc_archivo=doc.replace("set_sequences_muscle_secuencia_",
							"dominios_PROSITE_secuencia_")
	n_secuencia=n
	if os.path.exists(direcc_archivo):
		f = open(direcc_archivo,"a")
	else:
		f = open(direcc_archivo,"w")
	with open(doc) as input_handle:
		print("\x1b[0;37m"+
			"\nDe los hits pertenecientes al blast realizado con la secuencia " +
			 "\x1b[1;33m"+ n_secuencia+ "\n")
		f.write("\nDe los hits pertenecientes al blast realizado con la secuencia " + 
				n_secuencia+ "\n")
		for secuencia in SeqIO.parse(input_handle, "fasta"):
			print("\x1b[0;37m"+
				"La proteina "+
				"\x1b[1;33m"+ str(secuencia.id) + 
				" " + str(secuencia.name) +
				"\x1b[0;37m"+ " posee los siguientes dominios: \n")
			f.write("La proteina "+ str(secuencia.id) + " " +
					 str(secuencia.name) + 
					 " posee los siguientes dominios: \n")
			handle_dat = open("data_prosite/prosite.dat","r")
			records = Prosite.parse(handle_dat)
			for record in records:
				if record.pattern=="":
					pass

				else: #Estos pasos se utilizan para adaptar el patrón PROSITE al modulo re

					patron=record.pattern
					patron=patron.replace("-","")
					patron=patron.replace(".","")
					patron=patron.replace("x",".")
					patron=patron.replace("X",".")
					patron=patron.replace("{","[^")
					patron=patron.replace("}","]")
					patron=patron.replace("(","{")
					patron=patron.replace(")","}")
					patron=patron.replace(">","$")

					if re.search(patron,str(secuencia.seq)):

						accesion=record.accession 
						#Mostrar al usuario los dominios Prosite de nuestros hits

						print("\x1b[0;37m"+
							"\t-Nombre del dominio: "+
							"\x1b[1;33m"+record.name+
							"\x1b[0;37m"+".")
						print("\x1b[0;37m"+
							"\t-Accesión: "+
							"\x1b[1;33m"+record.accession+
							"\x1b[0;37m"+".")
						print("\x1b[0;37m"+
							"\t-Descripción: "+
							"\x1b[1;33m"+record.description)
						print("\x1b[0;37m"+
							"\t-Patrón según PROSITE: "+
							"\x1b[1;33m"+record.pattern+"\n")

						#Guardar info anterior mostrada en un archivo

						f.write("\t-Nombre del dominio: "+record.name+".")
						f.write("\t-Accesión: "+record.accession+".")
						f.write("\t-Descripción: "+record.description)
						f.write("\t-Patrón según PROSITE: "+record.pattern+"\n")

						handle_doc = open("data_prosite/prosite.doc",
										 encoding="utf8", errors="ignore")
						records_doc = Prodoc.parse(handle_doc)
						for record in records_doc:
							accesiones=record.prosite_refs
							for i in range(0,len(accesiones)):
								if accesion==accesiones[i][0]:
									#imprimir en pantalla y guardar la info del prosite.doc
									print("\x1b[0;37m"+
										record.text)
									f.write(record.text)

	print("\x1b[0;37m"+
		"La información relacionada con los hits de la secuencia ha sido almacenada en '"+
		"\x1b[1;33m"+direcc_archivo+
		"\x1b[0;37m"+ "'.")
