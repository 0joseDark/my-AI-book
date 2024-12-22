# Usando a CPU para Inteligência Artificial e Machine Learning

## Introdução
Este guia apresenta exemplos de como utilizar a CPU para tarefas de aprendizado de máquina em Python. Os exemplos incluem o uso de bibliotecas como Scikit-learn para aprendizado supervisionado e TensorFlow para redes neurais.

---

## Exemplos Práticos

### 1. Classificação com Scikit-learn
Neste exemplo, utilizamos a CPU para treinar um modelo de classificação com Scikit-learn.

#### Código:
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar o conjunto de dados Iris
data = load_iris()
X, y = data.data, data.target

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")
```

#### Explicação:
- Carregamos o conjunto de dados Iris.
- Dividimos os dados em conjuntos de treinamento e teste.
- Treinamos um classificador Random Forest.
- Avaliamos o desempenho do modelo com a métrica de acurácia.

---

### 2. Redes Neurais com TensorFlow e CPU
Neste exemplo, criamos e treinamos uma rede neural para classificação de dígitos usando TensorFlow.

#### Código:
```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# Carregar o conjunto de dados MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar os dados
x_train, x_test = x_train / 255.0, x_test / 255.0

# Criar o modelo
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Avaliar o modelo
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Acurácia no teste: {accuracy:.2f}")
```

#### Explicação:
- Usamos o TensorFlow para criar uma rede neural densa.
- Carregamos o conjunto de dados MNIST e normalizamos os valores dos pixels.
- Treinamos o modelo por 5 épocas e avaliamos sua performance.

---

## Configuração para CPU
Por padrão, tanto Scikit-learn quanto TensorFlow utilizam a CPU. Certifique-se de que sua instalação do TensorFlow esteja configurada corretamente para CPU. Para verificar:

```python
import tensorflow as tf
print("Dispositivos disponíveis:", tf.config.list_physical_devices('CPU'))
```

---

Esses exemplos mostram como utilizar a CPU para aprendizado de máquina de forma eficiente.
```
