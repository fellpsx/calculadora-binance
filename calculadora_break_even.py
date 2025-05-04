def calcular_break_even(capital, alavancagem):
    posicao = capital * alavancagem
    taxa_total = posicao * 0.001  # 0.10% total (entrada + saída a mercado)

    lucro_minimo = taxa_total
    pnl_percentual = (lucro_minimo / posicao) * 100
    roi_percentual = (lucro_minimo / capital) * 100

    return {
        "capital": capital,
        "alavancagem": alavancagem,
        "posicao_total": round(posicao, 2),
        "taxa_total_usd": round(taxa_total, 2),
        "lucro_necessario_usd": round(lucro_minimo, 2),
        "pnl_percentual": round(pnl_percentual, 4),
        "roi_percentual": round(roi_percentual, 4)
    }

print("=== CALCULADORA BREAK-EVEN BINANCE FUTURES ===")
capital = float(input("Digite o valor investido (ex: 170): "))
alavancagem = float(input("Digite a alavancagem (ex: 5): "))

resultado = calcular_break_even(capital, alavancagem)

print("\n--- RESULTADO ---")
print(f"Capital investido: ${resultado['capital']}")
print(f"Alavancagem: {resultado['alavancagem']}x")
print(f"Posição total: ${resultado['posicao_total']}")
print(f"Taxa total estimada (0.10%): ${resultado['taxa_total_usd']}")
print(f"Lucro mínimo para break-even: ${resultado['lucro_necessario_usd']}")
print(f"P&L mínimo necessário: {resultado['pnl_percentual']}%")
print(f"ROI líquido necessário: {resultado['roi_percentual']}%")