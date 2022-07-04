with open("pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Este é um teste! </h1>")
    pagina.write("<br><h2> Abaixo seguem nomes das suas cores favoritas:  </h2>")
    pagina.write("<h3>")
    nome=""
    while nome!="SAIR":
        nome = input("Digite o nome de uma cor favorita ou SAIR: ").upper()
        if nome!="SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</h3></body>")