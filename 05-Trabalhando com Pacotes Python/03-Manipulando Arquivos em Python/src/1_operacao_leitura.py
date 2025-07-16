arquivo = open("/home/tlchaves/Documentos/Estudos/DIO/Santander-python/Santander-2025---Back-End-com-Python/05-Trabalhando com Pacotes Python/03-Manipulando Arquivos em Python/src/lorem.txt",'r')
print(arquivo.read()) # retorna todo o arquivo de uma vez só 
print(arquivo.readline()) # retorna linha a linha sem carregar aquele arquivo na memoria 
print(arquivo.readlines()) # se for necessário carregar todo o conteudo tal qual o read porém quero separar esse conteudo em uma lista.

# # tip 
# while len(linha := arquivo.readline()):
#     print(linha)
arquivo.close()
