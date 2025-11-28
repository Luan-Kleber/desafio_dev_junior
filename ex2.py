import uuid

dados = {
    "estoque":
        [
            {"codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150},
            {"codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75},
            {"codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200},
            {"codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320},
            {"codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90}
        ]
}


def movimentaEstoque(codigo_produto, tipo, quantidade, descricao):
    # gera identificador único
    id_mov = str(uuid.uuid4())[:8]

    produto = next((p for p in dados["estoque"] if p["codigoProduto"] == codigo_produto), None)

    if produto is None:
        return "Produto não encontrado."

    estoque_anterior = produto["estoque"]

    if tipo == "entrada":
        produto["estoque"] += quantidade
    elif tipo == "saida":
        if quantidade > produto["estoque"]:
            return "Erro: estoque insuficiente."
        produto["estoque"] -= quantidade
    else:
        return "Tipo inválido. Use 'entrada' ou 'saida'."

    return (
        "=======================================\n"
        f"Movimentação {id_mov} registrada.\n"
        f"Motivo: {descricao}\n"
        f"Produto: {produto['descricaoProduto']}\n"
        f"Estoque anterior: {estoque_anterior}\n"
        f"Estoque atualizado: {produto['estoque']}\n"
        "=======================================\n"
    )

def verificaCodigo(codigo, dados):

    for item in dados["estoque"]:
        valor = int(item["codigoProduto"])

        if codigo == valor:
            return True
        
    return False

def acaoNovamente():
    
    print(
        "=======================================\n"
        f"[1] => Sim\n[2] => Não\n"
        "=======================================\n"
    )

    while True:
        acao = int(input("Deseja Realizar outra movimentação nesse produto: "))

        if(acao == 1):
            return True
            break
        elif(acao == 2):
            return False
            break
        else:
            print("Código inválido ou inexistente, Digite novamente")

def menu(dados):
    
    opcoes = "=======================================\n"

    for item in dados["estoque"]:
        opcoes += f"[{item['codigoProduto']}] => {item['descricaoProduto']}.\n"

    opcoes += f"\n[0] => Sair\n"
    opcoes += "=======================================\n"

    return opcoes
    
while True:
    print(menu(dados))

    while True:
        codigo_produto = int(input("Escolha um das opções numéricas acima: "))

        if(codigo_produto == 0):
            print("Até Mais")
            exit()

        if not verificaCodigo(codigo_produto, dados):
            print("Código inválido ou inexistente, Digite novamente")
        else:
            break

    while True:

        for item in dados["estoque"]:
            id_produto = int(item["codigoProduto"])

            if codigo_produto == id_produto:
                estoque_atual = int(item["estoque"])

        print("\n=======================================")
        print(f"QUNTIDADE DE ESTOQUE DO PRODUTO: {estoque_atual}\n")
        print(f"[1] => Entrada de Estoque\n[2] => Saída de Estoque\n[3] => Voltar")
        print("=======================================\n")

        acao = int(input("Escolha um das opções numéricas acima: "))

        if(acao == 1):
            print("\n")
            qtde_repor = int(input("Insira o valor para atualizar o estoque: "))
            print("\n")

            print(movimentaEstoque(codigo_produto, "entrada", qtde_repor, "Reposição do fornecedor"))
        elif(acao == 2):
            print("\n")
            qtde_saida = int(input("Insira o valor para atualizar o estoque: "))
            print("\n")

            print(movimentaEstoque(codigo_produto, "saida", qtde_saida, "Venda para cliente"))
        elif(acao == 3):
            print("\n")
            break
        else:
            print("Código inválido ou inexistente, Digite novamente2")
            continue

        if not acaoNovamente():
                break