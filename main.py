# GRUPO: Mariana de Castro, Michele Cristina Otta e Yejin Chung

# REFERÊNCIAS:
# https://www.hashtagtreinamentos.com/trabalhar-com-arquivos-de-texto-python?gad=1&gclid=Cj0KCQjwgNanBhDUARIsAAeIcAtAI1Z6jEOhn9Cxp_8hOTb_vFTtyK6HJ_hkkJsVlDYYljvFfHpe1usaAp2fEALw_wcB
# https://www.youtube.com/watch?v=AvUG8wZMh_E&t=1s
# https://www.youtube.com/watch?v=ad8toeTUXZs
# https://pt.stackoverflow.com/questions/375592/como-cortar-texto-de-string-em-python-delimitando-a-substring-inicial-para-a-po
# https://builtin.com/software-engineering-perspectives/python-substring-indexof

with open("entrada.txt", "r", encoding="utf-8") as arquivo:
  texto = arquivo.readlines()

  
operacoes = int(texto[0])


def produto_cartesiano(c1, c2):
  return[(i1, i2) for i1 in c1 for i2 in c2]


for i in range(operacoes):
  tipo_operacao = {'oi'}
  tipo_operacao.clear()
  tipo_operacao.add(texto[1 + 3 * i])
  
  conjunto1 = {1, 2, 'oi'}
  conjunto1.clear()
  c = texto[2 + 3 * i]
  comprimento = len(c)
  inicio = 0

  n_elementos = 0 
  inicial1 = 0
  for k in range(comprimento):
    j = c.find(",", inicial1)
    if(j!=-1):
      inicial1 = j+1
      n_elementos +=1
  n_elementos += 1

  for j in range(n_elementos):
    parada = c.find(',', inicio)
    sub = c[inicio:parada]
    conjunto1.add(sub)
    inicio = parada + 2

  
  conjunto2 = {1, 2, 'oi'}
  conjunto2.clear()
  c = texto[3 + 3 * i]
  comprimento = len(c)
  inicio = 0

  n_elementos2 = 0 
  inicial2 = 0
  for k in range(comprimento):
    j = c.find(",", inicial2)
    if(j!=-1):
      inicial2 = j+1
      n_elementos2 +=1
  n_elementos2 += 1

  for j in range(n_elementos2):
    parada = c.find(',', inicio)
    sub = c[inicio:parada]
    conjunto2.add(sub)
    inicio = parada + 2

  erro = '' in conjunto1
  if erro == True:
    conjunto1.remove("")
  erro2 = '' in conjunto2
  if erro2 == True:
    conjunto2.remove("")
  

  if tipo_operacao == {'U\n'}:
    resultado = conjunto1.union(conjunto2)
    print(f"\nUnião: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")
    
  elif tipo_operacao == {'I\n'}:
    resultado =  conjunto1.intersection(conjunto2)
    print(f"\nIntersecção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}    Resultado: {resultado}")
    
  elif tipo_operacao == {'D\n'}:
    resultado = conjunto1.difference(conjunto2)
    print(f"\nDiferença: conjunto 1 {conjunto1}, conjunto2 {conjunto2}. Resultado: {resultado}")

  elif tipo_operacao == {'C\n'}:
    resultado = produto_cartesiano(conjunto1, conjunto2)
    print(f"\nProduto cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: ")
    for item in resultado:
      print(item)
