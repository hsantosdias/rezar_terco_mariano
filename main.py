def rezar(oracao, quantidade=1, intencao=""):
    """Função auxiliar para imprimir a oração e a intenção."""
    if intencao:
        print(f"[{intencao}] ", end="")
    print(f"Rezando: {oracao} ({quantidade}x)")

def rezar_terco_mariano():
    print("=== INÍCIO DO TERÇO ===")
    rezar("Sinal da Cruz")
    rezar("Oferecimento do Terço")
    rezar("Credo", intencao="Segurando a Cruz")
    
    # Contas iniciais após a cruz
    rezar("Pai-Nosso", intencao="Primeira conta grande")
    
    print("\n-- Homenagem à Santíssima Trindade --")
    intencoes_iniciais = ["Deus Pai", "Deus Filho", "Deus Espírito Santo"]
    for intencao in intencoes_iniciais:
        rezar("Ave-Maria", intencao=f"Em honra a {intencao}")
        
    rezar("Glória ao Pai")

    print("\n=== CONTINUAÇÃO: OS 5 MISTÉRIOS ===")
    # Loop principal que percorre as 5 dezenas (Mistérios)
    for misterio in range(1, 6):
        print(f"\n--- Contemplando o {misterio}º Mistério ---")
        rezar("Anúncio do Mistério e Meditação")
        
        rezar("Pai-Nosso", intencao="Conta grande do mistério")
        
        # Loop aninhado para as 10 Ave-Marias de cada dezena
        print("Iniciando a dezena...")
        for conta_pequena in range(1, 11):
            rezar("Ave-Maria", intencao=f"Conta pequena {conta_pequena}/10")
            
        rezar("Glória ao Pai", intencao="Fim da dezena")
        rezar("Jaculatórias", intencao="'Ó meu Jesus...', 'Ó Maria concebida...'")

    print("\n=== FINALIZAÇÃO DO TERÇO ===")
    rezar("Agradecimento")
    rezar("Salve Rainha")
    rezar("Ladainha de Nossa Senhora")
    
    print("\n-- Orações pelo Romano Pontífice e pela Igreja --")
    # Orações finais (1 Pai-Nosso, 1 Ave-Maria, 1 Glória)
    rezar("Pai-Nosso")
    rezar("Ave-Maria")
    rezar("Glória ao Pai")
    
    rezar("Saudação Final à Virgem Maria")
    rezar("Sinal da Cruz", intencao="Encerramento")
    print("=== TERÇO CONCLUÍDO ===")

# Executando o "código" do Terço
rezar_terco_mariano()