""" Imprime elementos de una lista sin usar ciclos """


def recursive_print(lista):
	if len(lista) == 1:
		print(lista[0])
	else:
		lista_izq = lista[:len(lista)//2]
		lista_der = lista[len(lista)//2:]
		recursive_print(lista_izq)
		recursive_print(lista_der)

recursive_print([x for x in range(1,1000)])

