# calcular o juros simples

# entrada de dados
capital = int(input('qual o valor da capital?'))
taxa = int(input('qual o valor da taxa?'))
prazo = int(input('qual o prazo para o juros'))

# processamento
Juros = capital * taxa * prazo/ 100

# saida
print(f' juros = {Juros}')



