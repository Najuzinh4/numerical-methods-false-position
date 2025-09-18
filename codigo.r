# -------------------------------------------------------------
# Nome: Ana Júlia Gaspar       Nome: Renan Almeida Brandão
# RA: [221026568]              RA: [201027836]
# Linguagem: R
# Trabalho 1 - Cálculo Numérico Computacional
# Exercício 3 - Método da Posição Falsa
# -------------------------------------------------------------

# Definição da função f(x) = ln(x) - sin(x)
f <- function(x) {
  return(log(x) - sin(x))
}

# Implementação melhorada do Método da Posição Falsa
posicao_falsa <- function(a, b, tol = 1e-9, max_iter = 1000) {
  # Verificação rigorosa do intervalo
  if (f(a) * f(b) >= 0) {
    stop("Erro: f(a) e f(b) devem ter sinais opostos no intervalo [a, b]")
  }
  
  iter <- 0
  c_prev <- a  # Valor anterior de c para controle de convergência
  
  # Data frame para armazenar o histórico de iterações (opcional para análise)
  historico <- data.frame(iteracao = integer(), a = numeric(), b = numeric(), 
                         c = numeric(), f_c = numeric())
  
  repeat {
    # Calcula o ponto c pela fórmula da posição falsa
    c <- (a * f(b) - b * f(a)) / (f(b) - f(a))
    
    # Armazena a iteração no histórico
    historico <- rbind(historico, data.frame(
      iteracao = iter, a = a, b = b, c = c, f_c = f(c)
    ))
    
    # Critérios de parada:
    # 1. |f(c)| < tolerância E |c - c_prev| < tolerância
    # 2. Número máximo de iterações atingido
    if ((abs(f(c)) < tol && abs(c - c_prev) < tol) || iter >= max_iter) {
      break
    }
    
    # Atualiza o intervalo
    if (f(a) * f(c) < 0) {
      b <- c
    } else {
      a <- c
    }
    
    c_prev <- c
    iter <- iter + 1
  }
  
  return(list(raiz = c, iteracoes = iter, erro = abs(f(c)), historico = historico))
}

# Definir intervalo adequado [a, b] onde f(a)*f(b) < 0
# Vamos testar valores para encontrar um intervalo adequado
cat("f(1) =", f(1), "\n")
cat("f(2) =", f(2), "\n") 
cat("f(2.2) =", f(2.2), "\n")
cat("f(2.5) =", f(2.5), "\n")
cat("f(3) =", f(3), "\n")

# Intervalo onde há mudança de sinal: [2, 2.5]
a <- 2.0
b <- 2.5

# Executa o método
resultado <- posicao_falsa(a, b, tol = 1e-9)

# Mostra resultados detalhados no console
cat("\n=== RESULTADO DO MÉTODO DA POSIÇÃO FALSA ===\n")
cat("Função: f(x) = ln(x) - sin(x)\n")
cat("Intervalo inicial: [", a, ", ", b, "]\n", sep = "")
cat("Raiz aproximada: ", resultado$raiz, "\n")
cat("Valor de f(raiz): ", f(resultado$raiz), "\n")
cat("Número de iterações: ", resultado$iteracoes, "\n")
cat("Erro estimado: ", resultado$erro, "\n")
cat("Precisão alcançada: ", resultado$erro < 1e-9, "\n")

# Exibe as primeiras iterações para análise
cat("\nPrimeiras iterações:\n")
print(head(resultado$historico))

# Salva o resultado em um arquivo .txt
saida <- paste0(
  "=== RESULTADO DO MÉTODO DA POSIÇÃO FALSA ===\n",
  "Função: f(x) = ln(x) - sin(x)\n",
  "Intervalo inicial: [", a, ", ", b, "]\n",
  "Raiz aproximada: ", resultado$raiz, "\n",
  "f(raiz) = ", f(resultado$raiz), "\n",
  "Número de iterações: ", resultado$iteracoes, "\n",
  "Erro final: ", resultado$erro, "\n",
  "Precisão ε = 10⁻⁹ alcançada: ", ifelse(resultado$erro < 1e-9, "SIM", "NÃO"), "\n",
  "\nEste resultado foi gerado pelo Método da Posição Falsa implementado em R."
)

writeLines(saida, "resultado.txt")
cat("\nResultado salvo em 'resultado.txt'\n")