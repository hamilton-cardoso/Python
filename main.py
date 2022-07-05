from Funcoes import *

inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<5:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        resultado = exibir()
        if resultado == False:
            print('Inventário ainda não existe, insira a opção <1> para registrar!')
            exit()

        for linha in resultado:
            lista = linha.split(";")
            print("Data.........: ", lista[1])
            print("Descrição....: ", lista[2])
            print("Departamento.: ", lista[3])
        opcao = chamarMenu()
    elif opcao==4:
        gerarHtml()
        print('Html gerado com sucesso!')
    opcao = chamarMenu()