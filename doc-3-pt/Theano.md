Theano é uma biblioteca de Python que facilita a definição, otimização e avaliação de expressões matemáticas envolvendo arrays multidimensionais, também conhecidos como tensores. Foi amplamente utilizada em pesquisa e desenvolvimento de algoritmos de aprendizado de máquina e redes neurais antes de ser substituída por bibliotecas mais modernas como TensorFlow e PyTorch.

Aqui está uma explicação e um exemplo básico de como usar o Theano:

### Explicação

1. **Definição de Expressões Matemáticas:** Theano permite definir expressões matemáticas de forma simbólica, o que significa que você pode construir operações matemáticas sem dados reais e, em seguida, compilá-las em funções eficientes.
2. **Otimização:** Theano realiza várias otimizações para melhorar a eficiência das operações matemáticas, como a fusão de operações e a utilização de GPUs para acelerar os cálculos.
3. **Compilação:** As expressões simbólicas são compiladas em funções eficientes que podem ser executadas com dados reais.

### Exemplo

Vamos criar um exemplo simples de uma rede neural usando Theano.

```python
import theano
import theano.tensor as T
import numpy as np

# Definindo as variáveis simbólicas
X = T.matrix('X')  # Entrada
y = T.vector('y')  # Saída verdadeira
W = theano.shared(np.random.randn(2), name='W')  # Pesos
b = theano.shared(0., name='b')  # Bias

# Definindo o modelo
y_pred = T.dot(X, W) + b  # Previsão
cost = T.mean(T.sqr(y_pred - y))  # Função de custo (erro quadrático médio)

# Calculando o gradiente
grad_W, grad_b = T.grad(cost, [W, b])

# Definindo a função de atualização dos pesos
learning_rate = 0.01
updates = [(W, W - learning_rate * grad_W), (b, b - learning_rate * grad_b)]

# Compilando a função de treinamento
train = theano.function(inputs=[X, y], outputs=cost, updates=updates)

# Dados de exemplo
X_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5]], dtype=np.float32)
y_data = np.array([5, 8, 11, 14], dtype=np.float32)

# Treinando o modelo
for epoch in range(1000):
    cost_val = train(X_data, y_data)
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Custo: {cost_val}")

# Pesos treinados
print("Pesos:", W.get_value())
print("Bias:", b.get_value())
```

### Explicação do Exemplo

1. **Definindo Variáveis Simbólicas:** Começamos definindo as variáveis simbólicas `X` (entrada), `y` (saída verdadeira), `W` (pesos) e `b` (bias).
2. **Modelo:** Criamos uma expressão simbólica para a previsão (`y_pred`) e a função de custo (`cost`).
3. **Gradientes:** Calculamos os gradientes da função de custo em relação aos pesos e bias.
4. **Atualizações:** Definimos as regras de atualização dos pesos usando uma taxa de aprendizado (`learning_rate`).
5. **Compilação:** Compilamos a função de treinamento usando `theano.function`.
6. **Treinamento:** Treinamos o modelo usando dados de exemplo e imprimimos o custo a cada 100 épocas.

Theano foi uma ferramenta poderosa, mas atualmente é recomendável usar bibliotecas mais modernas como TensorFlow ou PyTorch para desenvolvimento de modelos de aprendizado de máquina.