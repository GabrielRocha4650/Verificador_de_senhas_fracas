lista_senhasfracas = ["123456", "senha123", "qwerty", "admin", "password", "54321"]
#Lista de senhas fracas 

def ehfraca(senha):
    if len(senha) < 8 or senha in lista_senhasfracas:
        return True
    return False
#Verifica se cada senha e falsa se a senha tiver menos de 8 caracteres
#ou for identica a da lista acima.
        

def contar_fracas(lista_senhas):
    cont = 0
    # Percorre cada senha dentro da lista enviada por parâmetro
    for senha in lista_senhas:
        if ehfraca(senha):
            cont += 1
    return cont

lista_senhas = []

#Entrada de dados do usuario
for i in range(500):
    senha = input("Digite uma senha: ")
    lista_senhas.append(senha)

quant = contar_fracas(lista_senhas)

print("Quantidade de senhas fracas:",quant)

#Lista de senhas cadastradas pelo usuario consideradas fracas
for senha in lista_senhas:
    if ehfraca(senha):
        print(senha)
