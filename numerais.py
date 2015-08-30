extenso = 'zero um dois três quatro cinco seis sete oito nove'.split(" ")

def to_text(num):         
     text = ''
     for i in str(num):
          text += extenso[int(i)] + ', '
     text = text[ : -2]
     return text

def convert(num):
     return str(extenso.index(num))
     
def to_number(numeros):
     numeros = numeros.split(", ")
     num = ''
     lista = list(map(convert, numeros))
     for i in lista:
          num += i

     return int(num)


assert 153927183 == to_number('um, cinco, três, nove, dois, sete, um, oito, três')
assert 'um, cinco, três, nove, dois, sete, um, oito, três' == to_text(153927183)
