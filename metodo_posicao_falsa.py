# -------------------------------------------------------------
# Nome: Ana Júlia Gaspar       Nome: Renan Almeida Brandão
# RA: [221026568]              RA: [201027836]
# Linguagem: Python
# Trabalho 1 - Cálculo Numérico Computacional
# Exercício 3 - Método da Posição Falsa
# -------------------------------------------------------------

import math
import numpy as np

# Definição da função f(x) = ln(x) - sin(x)
def f(x):
    return math.log(x) - math.sin(x)

# Implementação do Método da Posição Falsa
def posicao_falsa(a, b, tol=1e-9, max_iter=1000):
    """
    Encontra a raiz da função f(x) no intervalo [a, b] usando o Método da Posição Falsa
    
    Parâmetros:
    a, b: limites do intervalo
    tol: tolerância (precisão desejada)
    max_iter: número máximo de iterações
    
    Retorna:
    dicionário com raiz, iterações, erro e histórico
    """
    
    # Verificação do intervalo
    if f(a) * f(b) >= 0:
        raise ValueError("Erro: f(a) e f(b) devem ter sinais opostos no intervalo [a, b]")
    
    iter_count = 0
    c_prev = a
    historico = []
    
    print(f"{'Iteração':<10} {'a':<15} {'b':<15} {'c':<15} {'f(c)':<15}")
    print("-" * 70)
    
    while iter_count < max_iter:
        # Calcula o ponto c pela fórmula da posição falsa
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        # Armazena no histórico
        historico.append({
            'iteracao': iter_count,
            'a': a,
            'b': b,
            'c': c,
            'f_c': f(c)
        })
        
        # Exibe a iteração atual
        print(f"{iter_count:<10} {a:<15.10f} {b:<15.10f} {c:<15.10f} {f(c):<15.2e}")
        
        # Critério de parada
        if abs(f(c)) < tol and abs(c - c_prev) < tol:
            break
        
        # Atualiza o intervalo
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        c_prev = c
        iter_count += 1
    
    return {
        'raiz': c,
        'iteracoes': iter_count,
        'erro': abs(f(c)),
        'historico': historico
    }

# Função para testar valores da função
def testar_valores():
    """Testa valores da função para encontrar intervalo adequado"""
    print("Teste de valores da função f(x) = ln(x) - sin(x):")
    print("-" * 40)
    for x in [1.0, 1.5, 2.0, 2.2, 2.5, 3.0]:
        print(f"f({x:.1f}) = {f(x):.6f}")
    print()

# Função principal
def main():
    print("=" * 70)
    print("MÉTODO DA POSIÇÃO FALSA")
    print("Função: f(x) = ln(x) - sin(x)")
    print("Precisão: ε = 10⁻⁹")
    print("=" * 70)
    print()
    
    # Testa valores para encontrar intervalo adequado
    testar_valores()
    
    # Define o intervalo [2.0, 2.5] onde f(2.0) < 0 e f(2.5) > 0
    a = 2.0
    b = 2.5
    
    print(f"Intervalo escolhido: [{a}, {b}]")
    print(f"f({a}) = {f(a):.6f}")
    print(f"f({b}) = {f(b):.6f}")
    print()
    
    # Executa o método
    try:
        resultado = posicao_falsa(a, b)
        
        print("\n" + "=" * 70)
        print("RESULTADO FINAL")
        print("=" * 70)
        print(f"Raiz aproximada: {resultado['raiz']:.12f}")
        print(f"f(raiz) = {f(resultado['raiz']):.2e}")
        print(f"Número de iterações: {resultado['iteracoes']}")
        print(f"Erro final: {resultado['erro']:.2e}")
        print(f"Precisão ε = 10⁻⁹ alcançada: {'SIM' if resultado['erro'] < 1e-9 else 'NÃO'}")
        
        # Salva resultados em arquivo
        with open("resultado_python.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("=== RESULTADO DO MÉTODO DA POSIÇÃO FALSA ===\n")
            arquivo.write(f"Função: f(x) = ln(x) - sin(x)\n")
            arquivo.write(f"Intervalo inicial: [{a}, {b}]\n")
            arquivo.write(f"Raiz aproximada: {resultado['raiz']:.12f}\n")
            arquivo.write(f"f(raiz) = {f(resultado['raiz']):.2e}\n")
            arquivo.write(f"Número de iterações: {resultado['iteracoes']}\n")
            arquivo.write(f"Erro final: {resultado['erro']:.2e}\n")
            arquivo.write(f"Precisão ε = 10⁻⁹ alcançada: {'SIM' if resultado['erro'] < 1e-9 else 'NÃO'}\n")
            arquivo.write("\nImplementado em Python")
        
        print("\nResultado salvo em 'resultado_python.txt'")
        
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()