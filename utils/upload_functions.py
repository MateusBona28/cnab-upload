def convert_string_type(str):

    converted_string = ""

    if str == "1":
        converted_string = "Débito"
    elif str == "2":
        converted_string = "Boleto"
    elif str == "3":
        converted_string = "Financiamento"
    elif str == "4":
        converted_string = "Crédito"
    elif str == "5":
        converted_string = "Recebimento Empréstimo"
    elif str == "6":
        converted_string = "Vendas"
    elif str == "7":
        converted_string = "Recebimento TED"
    elif str == "8":
        converted_string = "Recebimento DOC"
    elif str == "9":
        converted_string = "Aluguel"

    return converted_string


def get_total_value(files):
    total = 0
    for file in files:
        if file.tipo == "Boleto" or file.tipo == "Financiamento" or file.tipo == "Aluguel":
            total -= float(file.valor)
        else:
            total += float(file.valor)
    return round(total, 2)
