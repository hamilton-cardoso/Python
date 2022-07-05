import os

def chamarMenu():
    escolha = int(input("Digite: \n"
                        "<1> para registrar ativo \n"
                        "<2> para persistir em arquivo \n"
                        "<3> para exibir ativos armazenados \n"
                        "<4> para gerar html do armazém: "))
    return escolha


def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()


def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" +
                      valor[1] + ";" + valor[2] + "\n")
    return "Persistido com sucesso"


def exibir():
    if os.path.exists('inventario.csv'):
        with open('inventario.csv', 'r') as inv:
            linhas = inv.readlines()
        return linhas
    else:
        return os.path.exists('inventario.csv')


def gerarHtml():
    with open('pagina.html', 'w') as pagina:
        html = '<html lang="pt-BR">\n' \
               '<head>\n' \
               '    <title>Inventário</title>\n' \
               '    <link rel="stylesheet" type="text/css" href="css/tabela.css">\n' \
               '</head>\n' \
               '<body>\n' \
               '    <h1>INVENTÁRIO</h1><br>\n' \
               '    <h2>Itens registrados</h2> \n' \
               '    <table id="customers">\n' \
               '        <tr>\n' \
               '            <th>Data Atualização</th>\n' \
               '            <th>Descrição</th> \n' \
               '            <th>Departamento</th> \n' \
               '        </tr>\n'

        pagina.write(html)

        resultado = exibir()
        for linha in resultado:
            lista = linha.split(';')
            pagina.write('        <tr>\n')
            pagina.write('            <td>' + lista[1] + '</td>\n')
            pagina.write('            <td>' + lista[2] + '</td>\n')
            pagina.write('            <td>' + lista[3] + '</td>\n')
            pagina.write('        </tr>\n')

        pagina.write('    </table>\n')
        pagina.write('</body>\n')
        pagina.write('</html>')
