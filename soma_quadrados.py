def quadrados(n):
    lista = []
    for i in range(1, n+1):
        quadrado = i ** 2
        if quadrado <= n:
            lista.append(quadrado)
        else:
            return lista
    return lista


def menor_lista(n, lista):
	menor = []
	i = len(lista)-1
	while sum(menor) != n:
		if (lista[i] + sum(menor)) <= n:
			menor.append(lista[i])
		else:
			i -= 1

	return menor


def resultado(n):
	if n == 0:
		return [0]
	elif n in quadrados(n):
		return [n]
	else:
		lista = quadrados(n)
		menor = menor_lista(n, lista)
		while lista:
			if len(menor_lista(n, lista)) < len(menor):
				menor = menor_lista(n, lista)
			else:
				lista.pop()
		return menor



assert [0] == resultado(0)
assert [1] == resultado(1)
assert [9] == resultado(9)
assert [25] == resultado(25)
assert [1,1] == resultado(2)
assert [1,1,1] == resultado(3)
assert [4,4,4] == resultado(12)
assert [16,4] == resultado(20)
assert [9,9,4] == resultado(22)
