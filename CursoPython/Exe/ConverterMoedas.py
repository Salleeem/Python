def converter_moeda(origem, destino, quantidade):
   
    moedas = {
        'usd': {'eur': 0.93, 'brl': 4.97, },
        'eur': {'usd': 1.08, 'brl': 5.35, },
        'brl': {'usd': 0.20, 'eur': 0.19, },
        
    }

    if origem in moedas and destino in moedas[origem]:
        taxa_conversao = moedas[origem][destino]
        valor_convertido = quantidade * taxa_conversao
        return valor_convertido
    else:
        return "Não foi possível realizar a conversão."

origem = input("Digite a moeda de origem (ex: usd, brl ou eur): ").lower()
destino = input("Digite o código da moeda de destino : ").lower()
quantidade = float(input("Digite a quantidade : "))

resultado = converter_moeda(origem, destino, quantidade)
print(f"{quantidade} {origem.upper()} equivale a {resultado} {destino.upper()}")



