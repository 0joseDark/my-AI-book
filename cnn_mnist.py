import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Passo 1: Carregar o conjunto de dados MNIST
print("A carregar o conjunto de dados MNIST...")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Passo 2: Pré-processar os dados
print("A pré-processar os dados...")
# Normalizar os valores dos píxeis para o intervalo [0, 1]
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Redimensionar para incluir o canal (grayscale: 1 canal)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Converter os rótulos em formato de uma-hot (one-hot encoding)
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Passo 3: Construir a CNN
print("A construir a CNN...")
modelo = Sequential()

# Adicionar uma camada convolucional (32 filtros, tamanho 3x3, ReLU)
modelo.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

# Adicionar uma camada de pooling (reduz tamanho pela metade)
modelo.add(MaxPooling2D(pool_size=(2, 2)))

# Adicionar uma segunda camada convolucional (64 filtros)
modelo.add(Conv2D(64, (3, 3), activation='relu'))
modelo.add(MaxPooling2D(pool_size=(2, 2)))

# Achatar os dados (flatten) para uma dimensão
modelo.add(Flatten())

# Adicionar uma camada totalmente conectada (128 neurónios)
modelo.add(Dense(128, activation='relu'))

# Adicionar a camada de saída (10 neurónios, uma para cada dígito)
modelo.add(Dense(10, activation='softmax'))

# Passo 4: Compilar o modelo
print("A compilar o modelo...")
modelo.compile(optimizer='adam',
               loss='categorical_crossentropy',
               metrics=['accuracy'])

# Passo 5: Treinar o modelo
print("A treinar o modelo...")
historico = modelo.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)

# Passo 6: Avaliar o modelo
print("A avaliar o modelo...")
perda, precisao = modelo.evaluate(x_test, y_test)
print(f"Precisão no conjunto de teste: {precisao*100:.2f}%")

# Passo 7: Visualizar os resultados
plt.plot(historico.history['accuracy'], label='Precisão Treino')
plt.plot(historico.history['val_accuracy'], label='Precisão Validação')
plt.xlabel('Época')
plt.ylabel('Precisão')
plt.legend()
plt.title('Desempenho da CNN')
plt.show()

# Passo 8: Fazer previsões
print("A fazer previsões...")
amostra = x_test[:5]
previsoes = modelo.predict(amostra)
for i, pred in enumerate(previsoes):
    plt.imshow(amostra[i].reshape(28, 28), cmap='gray')
    plt.title(f"Previsão: {pred.argmax()}")
    plt.show()
