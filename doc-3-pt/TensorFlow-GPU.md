O TensorFlow é uma biblioteca de código aberto desenvolvida pelo Google para computação numérica e aprendizado de máquina. O TensorFlow possui suporte para execução em GPUs, o que pode acelerar significativamente o treinamento de modelos de aprendizado profundo devido ao grande poder de processamento paralelo das GPUs. Abaixo, vou explicar como configurar o TensorFlow para usar a GPU e fornecer um exemplo de código.

### Configuração do TensorFlow para GPU

#### Passo 1: Instalar os drivers da GPU
Antes de usar o TensorFlow com GPU, é necessário instalar os drivers da GPU que correspondem à sua placa de vídeo. Certifique-se de instalar a versão correta do driver fornecida pelo fabricante da GPU (NVIDIA, AMD, etc.).

#### Passo 2: Instalar o CUDA Toolkit e cuDNN
O TensorFlow para GPU requer o CUDA Toolkit e cuDNN (CUDA Deep Neural Network library) da NVIDIA. Você pode baixá-los do site da NVIDIA. Siga as instruções de instalação fornecidas para configurar corretamente o CUDA e cuDNN no seu sistema.

#### Passo 3: Instalar o TensorFlow para GPU
Depois de instalar os drivers, CUDA e cuDNN, você pode instalar o TensorFlow para GPU. É recomendado usar um ambiente virtual para evitar conflitos de dependências. Aqui está um exemplo usando `pip`:

```bash
# Crie e ative um ambiente virtual (opcional)
python -m venv tf_gpu_env
source tf_gpu_env/bin/activate  # Linux/macOS
# .\tf_gpu_env\Scripts\activate  # Windows

# Instale o TensorFlow para GPU
pip install tensorflow-gpu
```

### Verificando a Instalação

Após instalar o TensorFlow, você pode verificar se a GPU está sendo usada corretamente com o seguinte código:

```python
import tensorflow as tf

# Verifica se a GPU está disponível
print("GPU disponível:", tf.config.list_physical_devices('GPU'))
```

### Exemplo de Código: Treinando um Modelo Simples com GPU

Aqui está um exemplo de código que treina um modelo simples de rede neural em um conjunto de dados de amostra (MNIST) usando a GPU:

```python
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

# Carregar o conjunto de dados MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar os dados
x_train, x_test = x_train / 255.0, x_test / 255.0

# Definir o modelo
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer=Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Avaliar o modelo
loss, accuracy = model.evaluate(x_test, y_test)
print(f'Loss: {loss}, Accuracy: {accuracy}')
```

### Explicação do Código

1. **Importações**: Importamos o TensorFlow e os módulos necessários para carregar e preparar o conjunto de dados MNIST.
2. **Carregamento dos dados**: Carregamos o conjunto de dados MNIST, que contém imagens de dígitos escritos à mão.
3. **Normalização dos dados**: Normalizamos os valores dos pixels para o intervalo [0, 1].
4. **Definição do modelo**: Definimos um modelo sequencial simples com uma camada de entrada (Flatten), uma camada densa oculta (Dense) com 128 neurônios e a função de ativação ReLU, e uma camada de saída com 10 neurônios (um para cada dígito) e a função de ativação softmax.
5. **Compilação do modelo**: Compilamos o modelo usando o otimizador Adam, a função de perda `sparse_categorical_crossentropy` e a métrica de acurácia.
6. **Treinamento do modelo**: Treinamos o modelo com os dados de treinamento e validamos com os dados de teste.
7. **Avaliação do modelo**: Avaliamos o desempenho do modelo nos dados de teste.

Este exemplo demonstra como configurar e treinar um modelo de aprendizado profundo usando o TensorFlow com suporte a GPU, o que pode acelerar significativamente o processo de treinamento.