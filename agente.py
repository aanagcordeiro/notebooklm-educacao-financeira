print("Agente Financeiro iniciado 💰")

while True:
    pergunta = input("Pergunte algo (ou 'sair'): ")

    if pergunta.lower() == "sair":
        break

    if "economizar" in pergunta:
        print("Organize seus gastos e evite compras desnecessárias.")
    
    elif "investir" in pergunta:
        print("Comece com investimentos simples como renda fixa.")
    
    elif "dívida" in pergunta:
        print("Priorize pagar dívidas com juros altos.")
    
    else:
        print("Ainda estou aprendendo.")
