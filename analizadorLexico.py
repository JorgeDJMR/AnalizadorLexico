import ply.lex as lex
import re
import codecs
import os
import sys

tdtok=[]

reservadas = {
	#inicio y fin dle programa
	'INICIO':'PRinicio',
	'FIN':'PRfin',

	#Ciclos
	'WHILE':'PRwhile',
	'FOR':'PRfor',
	'SWITCH':'PRswitch',


	#condicionales
	'IF':'PRif',
	'ELSE': 'PRelse',

	#Operadores logicos
	'&': 'PRy',
	'|': 'PRo',
	'!': 'PRnegacion',

	#Tipos de datos
	'INT': 'PRentero',
	'FLOAT': 'PRdecimal',
	'STRING': 'PRcadena',
	'BOOL': 'PRbool',








	#Profe
	'THEN':'THEN',
	'CONST':'CONST',
	'VAR':'VAR',
}


tokens = ['INT','STR','VA','FLOAT','MAS','MENOS',
	  'DIV','POR','TCigualque', 'TCdiferenteque',
	  'TCmenorque','TCmayorque', 'TCmenorigual',
	  'TCmayorigual','TCpiz','TCpde','TCigual',
	  'TCcomentario','TCciz','TCcde','TClliz',
	  'TCllde','TCpuntoc']

#tokens = tokens+reservadas


tokens = tokens+list(reservadas.values())

#Lo que yo hice
t_ignore = ' \t\r'
t_PRinicio = r'INICIO'
t_PRfin = r'FIN'

#condicionales
t_PRelse = r'ELSE'
t_PRif = r'IF'
t_PRswitch = r'SWITCH'

#Ciclos
t_PRwhile = r'WHILE'
t_PRfor = r'FOR'

#Operadores
t_PRy = r'&'
t_PRo = r'\|'
t_PRnegacion = r'!'

#Tipo de datos
t_PRentero = r'INT'
t_PRdecimal = r'FLOAT'
t_PRcadena = r'STRING'
t_PRbool = r'BOOL'

#Operadores de comparacion
t_TCigualque = r'=='
t_TCdiferenteque = r'!='
t_TCmenorque = r'<'
t_TCmayorque = r'>'
t_TCmenorigual = r'<='
t_TCmayorigual = r'>='

#Asignacion teclas
t_TCpiz = r'\('
t_TCpde = r'\)'
t_TCigual = r'='
t_TCcomentario = r'//'
t_TCciz = r'\['
t_TCcde = r'\]'
t_TClliz = r'\{'
t_TCllde = r'\}'
t_TCpuntoc = r';'






#Del profe
t_THEN = r'THEN'
t_CONST = r'CONST'
t_VAR = r'VAR'
t_MAS = '\+'
t_MENOS = '-'
t_DIV = '/'
t_POR = '\*'


def t_VA(t):
	r'[a-z][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMMENT(t):
	r'\#.*'
	pass

def t_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t
def t_FLOAT(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t
def t_STR(t):
	r'".+"'
	t.value = t.value
	return t
def t_error(t):
	print (" Caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)


directorio = 'C:\\Users\Jorge de Jesus M.R\\Documents\\Sexto semestre\\panchito\\ArchivosPython\\src\\'
archivo = "test.txt"
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

#e=0
while True:
	
	tok = analizador.token()
	if not tok:
		break
	it=[tok.type,tok.value,"1","2",tok.lineno,tok.lexpos]
	tdtok.append(it)
	

for x in range(len(tdtok)):	
	tdtok[x].append(x)

	print(tdtok[x])
	



	
