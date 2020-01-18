###############################################################################
from subprocess import Popen, PIPE
from Bio import Seq
from Bio import SeqIO
import pandas as pd
import sys

import muscle as M

def Blastp (query,subject):
	proceso = Popen(['blastp','-query', query,
					'-subject',subject,'-outfmt',
					'6 qseqid sseqid qcovs pident evalue' ],
					stdout=PIPE, stderr=PIPE)
	error_encontrado = proceso.stderr.read()
	listado = proceso.stdout.read()

	proceso.stderr.close()
	proceso.stdout.close()

	direccion=str(query)
	direccion=direccion.replace("secuencia_","blast_result_secuencia_")

	my_output = open(direccion,"w")
	my_output.write("Query\tSubject\tCoverage\tPident\tE_value\n")
	my_output = open(direccion,"a")
	my_output.write(listado.decode('utf-8'))
	my_output.close()

	my_error = open("results/log","w")
	my_error.write(error_encontrado.decode('utf-8'))
	my_error.close()
	print("\x1b[0;37m"+
		"El resultado del blast se ha almacenado en '"+
		"\x1b[1;33m"+direccion+
		"\x1b[0;37m"+"'.")

	#AQUÍ SE REALIZA EL FILTRADO DE DATOS

	datos=pd.read_csv(direccion,sep="\t",header=0)###AL CAMBIAR LO OTRO HAY QUE TENER CUIDADO CON ESTO
	file= open(direccion+"_filtrado","w")
	results_coverage=datos[datos.iloc[:,2]>coverage]
	results_ident=results_coverage[results_coverage.iloc[:,3]>ident]
	results_evalue=results_ident[results_ident.iloc[:,4]<evalue]
	file.write(str(results_evalue))
	print("\x1b[0;37m"+
		"\nLos hits que cumplen los parametros de reestricción seleccionados son:\n")
	print(results_evalue)
	print("\x1b[0;37m"+
		"\nEstos hits han sido almacenados en el fichero '"+
		"\x1b[1;33m"+direccion+"_filtrado"+
		"\x1b[0;37m"+"'.")

	direccion=direccion.replace("blast_result_secuencia_","pares_muscle_")

	file2= open(direccion,"w")
	file2.write(str(results_evalue.iloc[:,[0,1]]))
	file.close()
	file2.close()

def Solicitar_datos_filtrado():
	global coverage
	global ident
	global evalue

	print("\x1b[0;37m"+
		"El resultado del blast se va a filtrar por los valores de coverage, identidad e evalue.")
	print("Tomará los siguientes valores como referencia:")
	print("\x1b[1;33m"+"\t -Coverage = 90")
	print("\x1b[1;33m"+"\t -Identidad = 90.000")
	print("\x1b[1;33m"+"\t -E-value = 1.0e-06")
	print("\x1b[1;32m"+
		"¿Desea cambiar estos valores?")
	Respuesta1=str(input("\x1b[1;32m"+
		"Responda[y/n]"))
	veces_error=0
	while (Respuesta1 != "y" and
		Respuesta1 != "n" and
		Respuesta1 != "N" and
		Respuesta1 != "Y"):
		if(veces_error<3):
			Respuesta1=str(input("\x1b[1;31m"+
				"Por favor, responda [y/n]"))
			veces_error=veces_error+1
		else:
			sys.exit()
	if (Respuesta1=="y" or
		Respuesta1=="Y"):
		print("\x1b[1;32m"+
			"Por favor, introduzca los valores que desee utilizar:")
		try:
			coverage=int(input("Coverage[0-100]= "))
			ident=float(input("Identidad[0.000-100.000]= "))
			evalue=float(input("E-value[0.000-1.000]= "))
			print("\x1b[0;37m"+
				"De acuerdo.")
			print("Los valores utilizados para el filtro serán:")
			print("\x1b[1;33m"+"\t -Coverage = " + str(coverage))
			print("\x1b[1;33m"+"\t -Identidad = " + str(ident))
			print("\x1b[1;33m"+"\t -E-value = " + str(evalue))

			pass
		except:
			raise Exception("\x1b[1;31m"+
				"Tenías que introducir un número entero o decimal. Vuelve a ejecutar el programa.")
	else:
		coverage=90
		ident=90.000
		evalue=1.0e-06
		print("\x1b[0;37m"+
			"De acuerdo.")
		print("Los valores utilizados seran los anteriormente mencionados:")
		print("\x1b[1;33m"+"\t -Coverage = 90")
		print("\x1b[1;33m"+"\t -Identidad = 90.000")
		print("\x1b[1;33m"+"\t -E-value = 1.0e-06")
