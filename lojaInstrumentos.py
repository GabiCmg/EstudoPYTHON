listaInstrumentos = []

continuar = input("Deseja adicionar um instrumento? S/N").upper()
while (continuar == "S"):
    quantInstrumentos = int(input("Deseja adicionar quantos?"))
    for i in range(0, quantInstrumentos):
        novoInstrumento = input("Adicione um instrumento:")
        if novoInstrumento.strip() == "":
            break
        else:
            listaInstrumentos.append(novoInstrumento)
    exibeLista = input("Deseja visualizar a lista? S/N").upper()
    if exibeLista == "S":
        listaInstrumentos.sort()
        print(listaInstrumentos)
    continuar = input("Deseja continuar adicionando um instrumento? S/N").upper()
print("Fim do programa.")