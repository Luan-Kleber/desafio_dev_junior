from datetime import datetime

def calculaJuros(valor, data_vencimento):

    data_venc = datetime.strptime(data_vencimento, "%d/%m/%Y")
    data_hoje = datetime.now()

    dias_atraso = (data_hoje - data_venc).days

    if dias_atraso <= 0:
        return f"Pagamento dentro do prazo. Valor final: R$ {valor:.2f}"

    juros = valor * (2.5/100) * dias_atraso
    valor_final = valor + juros

    return (
        f"Dias de atraso: {dias_atraso}\n"
        f"Juros: R$ {juros:.2f}\n"
        f"Valor final a pagar: R$ {valor_final:.2f}"
    )

valor = float(input("Informe o valor original: R$ "))
data_vencimento = input("Informe a data de vencimento (dd/mm/yyyy): ")

print("\n" + calculaJuros(valor, data_vencimento))
