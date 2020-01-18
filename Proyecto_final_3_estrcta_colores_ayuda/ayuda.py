def error_inicio():
	print("\x1b[1;31m"+
		"\n###################ERROR###################\n")
	print("\x1b[0;37m"+
		"Para el correcto funcionamiento de este programa debes introducir los siguientes argumentos:")
	print("\t1-Documento en formato fasta con tu secuencia")
	print("\t2-Uno o varios Genbanks de donde se extraeran las secuencias contra las cuales se va a alinear tu secuencia query")
	print("Espero esto te haya servido de ayuda.")
	print("Para más información pulsa python main.py -h o -help")


def ayuda():
	print("\x1b[0;37m"+
		"\n___________________________________________BIENVENIDO A LA AYUDA DE ESTE PROGRAMA___________________________________________\n")
	print("""
		\n___________________________________________¿QUÉ DEBO INTRODUCIR?___________________________________________\n
		Este programa tiene como objetivo realizar un análisis a partir de una o varias secuencias y uno o varios genbanks dados.\n
		Para ello debes introducir:\n
		\t1_Secuencia(s) en formato fasta.
		\t2_Genbank(s).\n
		------------------------------------------------------------------
		--> *Aclaración sobre 1*: Debes introducir un único archivo que contenga la o las secuencias sobre las que quieras realizar el análisis.
		--> *Aclaración sobre 2*: Debes introducir todos los genbank sobre los que quieras que se realice el análisis. Es importante que introduzcas el o los genbanks después del archivo fasta que contenga las secuencias.
		\n___________________________________________¿QUÉ HACE EL PROGRAMA?___________________________________________\n
		El programa va a realizar el análisis y va a mostrar ciertas cosas en pantalla. El análisis se compone de lo siguiete:
		\t1_La realización de un blast.
		\t2_La realización de un alineamiento muscle.
		\t3_La realización de un árbol filogenético Neighbor-Joining.
		\t4_La detección de dominios de proteínas presentes en la base de datos Prosite.\n
		--> Tras la realización del blast el programa va a solicitar los parámetros de filtrado de este. Estos parámetros son Coverage, Identidad y E-value. Si no se indican nuevos parámetros se utilizaran los que tiene el programa por defecto que son Coverage=90, Identidad=90.000 y E_value= 1.0e-06.\n
		\n_____________________________¿QUE RESULTADOS PROPORCIONA?¿QUE CONTIENE LA CARPETA 'results'?_____________________________\n
		El programa creará una carpeta "results" que contendrá lo siguiente:
		\t1_'database.fasta' --> Es la base de datos creada a partir de todas las secuencias extraidas de los genbanks.
		\t2_'log' --> Es un archivo que contiene los posibles errores que se hayan podido dar durante la ejecución.
		\t3_Una carpeta por cada secuencia que contendrá los siguientes archivos (siendo n el número de secuencia):
		\t\t1_'secuencia_n' --> Contiene la secuencia del análisis en formato fasta.
		\t\t2_'blast_result_secuencia_n' --> Contiene el resultado del blast realizado de nuestra secuencia n frente a la base de datos creada con los genbanks.
		\t\t3_'blast_result_secuencia_n_filtrado' --> Contiene el resultado del blast filtrado por los parámetros que hayamos introducido.
		\t\t4_'pares_muscle_n' --> Contiene los pares de secuencia que cumplen el filtrado y con los que se hará el muscle.
		\t\t5_'set_sequences_muscle_secuencia_n' --> Contiene las secuencias que cumplen el filtrado en formato fasta.
		\t\t6_'muscle_alignment_secuencia_n' --> Contiene el alineamiento muscle.
		\t\t7_'arbol_secuencia_n.phy' --> Contiene el árbol realizado por Neighbor-Joining en formato .phy (formato Newick).
		\t\t8_'dominios_PROSITE_secuencia_n' --> Contiene los dominios encontrados dentro de cada secuencia. De cada dominio tiene:
		\t\t\t1_El nombre.
		\t\t\t2_La accesión.
		\t\t\t3_La descripción.
		\t\t\t4_El patrón.
		\t\t\t5_Información detallada de cada dominio. (Presente en prosite.doc)
		""")
