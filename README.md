# NN-neural-network
"NN" pode referir-se a **rede neural** (em inglês, *neural network*), que é um modelo computacional inspirado no funcionamento do cérebro humano. As redes neurais são amplamente utilizadas em inteligência artificial e aprendizagem de máquina para resolver problemas como reconhecimento de padrões, classificação, previsão, tradução automática, entre outros.

### Estrutura de uma Rede Neural:
1. **Neurónios**: São as unidades básicas, semelhantes aos neurónios biológicos. Eles recebem entradas, processam informações e transmitem saídas.
2. **Camadas**:
   - **Camada de entrada**: Recebe os dados iniciais.
   - **Camadas ocultas**: Realizam o processamento, ajustando os pesos dos neurónios para aprender padrões.
   - **Camada de saída**: Produz o resultado final.
3. **Pesos e Bias**: Determinam a importância de cada entrada e ajustam o comportamento dos neurónios durante o treino.
4. **Funções de ativação**: Introduzem não-linearidade no modelo, permitindo que ele aprenda padrões complexos.

### Tipos de Redes Neurais:
- **Perceptron**: A forma mais simples, usada para problemas lineares.
- **MLP (Multi-Layer Perceptron)**: Rede neural com múltiplas camadas, útil para problemas não-lineares.
- **CNN (Convolutional Neural Network)**: Ideal para processamento de imagens e visão computacional.
- **RNN (Recurrent Neural Network)**: Boa para dados sequenciais, como texto ou áudio.
- **GAN (Generative Adversarial Network)**: Usada para geração de dados, como imagens ou vídeos.

### Aplicações:
- Reconhecimento de voz e texto.
- Tradução automática.
- Diagnóstico médico.
- Condução autónoma.
- Geração de conteúdo.

😊
**CNN** refere-se a uma **Rede Neural Convolucional** (*Convolutional Neural Network*), um tipo específico de rede neural projetada para processar e analisar dados que têm uma estrutura de grade, como imagens. CNNs são amplamente utilizadas em visão computacional e outras áreas que envolvem reconhecimento de padrões.

---

### **Como uma CNN funciona?**

1. **Camadas Convolucionais**:
   - A convolução é o processo central de uma CNN.
   - Nessa etapa, são usados *filtros* (ou *kernels*), que são pequenos conjuntos de pesos que percorrem a imagem de entrada para extrair características, como bordas, texturas ou formas.
   - O resultado dessa operação é um mapa de características (*feature map*).

2. **Camadas de Pooling (Subamostragem)**:
   - Reduzem a dimensão dos mapas de características, mantendo informações importantes e diminuindo a complexidade computacional.
   - Tipos comuns:
     - *Max pooling*: Retém o valor máximo em uma região.
     - *Average pooling*: Calcula a média dos valores em uma região.

3. **Camadas de Ativação**:
   - Aplicam funções não-lineares, como ReLU (*Rectified Linear Unit*), para introduzir não-linearidade ao modelo e permitir a aprendizagem de padrões mais complexos.

4. **Camadas Totalmente Conectadas**:
   - Transformam os mapas de características em uma única saída (como uma classificação).
   - Nessa etapa, cada neurónio está conectado a todos os neurónios da camada anterior.

5. **Camada de Saída**:
   - Fornece o resultado final (como a probabilidade de cada classe em problemas de classificação).

---

### **Estrutura Geral de uma CNN**

1. **Entrada**: 
   - Imagem ou outro tipo de dado.
   - Exemplo: Uma imagem RGB de 224x224x3.

2. **Camadas Convolucionais + Pooling**:
   - Extraem características importantes das entradas.

3. **Camadas Totalmente Conectadas**:
   - Integram as características extraídas e tomam decisões com base nelas.

4. **Saída**:
   - Predição/classificação.
   - Exemplo: "É um gato ou um cachorro?".

---

### **Exemplos de Aplicações de CNNs**

- **Visão Computacional**:
  - Reconhecimento facial.
  - Classificação de imagens (e.g., ImageNet).
  - Deteção de objetos (e.g., YOLO, SSD).

- **Saúde**:
  - Diagnóstico de doenças a partir de radiografias ou ressonâncias.

- **Condução Autónoma**:
  - Análise de imagens de câmaras para identificar estradas, sinais de trânsito e pedestres.

- **Outras Áreas**:
  - Análise de vídeos.
  - Super-resolução de imagens.
  - Estilização de imagens (*Deep Art*).

Aqui está um exemplo de um script em Python que implementa uma **Rede Neural Convolucional (CNN)** para classificar imagens usando a biblioteca Keras (que faz parte do TensorFlow). O script usa o conjunto de dados **MNIST**, que contém imagens de dígitos manuscritos (de 0 a 9).

Este exemplo é para **Windows 10** e está em **português europeu**, com explicações passo a passo.

---

### **Instalar os Módulos Necessários**
Antes de começar, instale os módulos necessários executando no terminal:

```bash
pip install tensorflow matplotlib
```

### **Explicação do Código**
1. **Carregar os Dados**:
   - O conjunto de dados MNIST contém imagens 28x28 em escala de cinza.
   - `x_train` e `x_test` são imagens. `y_train` e `y_test` são os rótulos (números entre 0 e 9).

2. **Pré-processamento**:
   - Normaliza os valores dos píxeis para [0, 1].
   - Redimensiona as imagens para incluir o canal.

3. **Construir a CNN**:
   - Camada convolucional extrai características da imagem.
   - Camada de pooling reduz a dimensão espacial.
   - Camada totalmente conectada toma decisões baseando-se nas características.

4. **Treino**:
   - Usa 5 épocas (passagens por todo o conjunto de treino).
   - Divide 20% do conjunto de treino para validação.

5. **Avaliação**:
   - Mede a precisão do modelo no conjunto de teste.

6. **Visualização**:
   - Plota a precisão do treino e validação ao longo das épocas.

7. **Previsões**:
   - Mostra as previsões para as primeiras 5 imagens do conjunto de teste.

---

### **Executar no Windows 10**
1. Certifique-se de que tem o Python instalado (preferencialmente versão 3.8 ou superior).
2. Instale os módulos usando `pip`.
3. Salve o script acima num ficheiro `.py` (por exemplo, `cnn_mnist.py`).
4. Execute o script no terminal:

```bash
python cnn_mnist.py
```
Aqui está a lista de **comandos** utilizados no script e suas respectivas **explicações**, organizados por funcionalidade:

---

### **1. Importação de Bibliotecas**
```python
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
```
- **`import tensorflow as tf`**: Importa o TensorFlow, uma biblioteca usada para construir e treinar redes neurais.
- **`from tensorflow.keras import Sequential`**: Importa o modelo sequencial, que é uma pilha linear de camadas.
- **`from tensorflow.keras.layers`**: Importa as camadas necessárias para construir a CNN:
  - **`Conv2D`**: Camada convolucional para extrair características das imagens.
  - **`MaxPooling2D`**: Camada de pooling para reduzir a dimensão espacial.
  - **`Flatten`**: Achata os dados para uma única dimensão.
  - **`Dense`**: Camada densa totalmente conectada.
- **`from tensorflow.keras.datasets import mnist`**: Importa o conjunto de dados MNIST.
- **`from tensorflow.keras.utils import to_categorical`**: Converte rótulos (números) para o formato *one-hot encoding*.
- **`import matplotlib.pyplot as plt`**: Importa o Matplotlib para visualização gráfica.

---

### **2. Carregar e Pré-processar os Dados**
```python
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
```
- **`mnist.load_data()`**: Carrega o conjunto de dados MNIST (imagens e rótulos).
- **`astype("float32")`**: Converte os valores dos píxeis para ponto flutuante (necessário para normalização).
- **`/ 255.0`**: Normaliza os valores dos píxeis no intervalo [0, 1].
- **`reshape(-1, 28, 28, 1)`**: Adiciona um canal às imagens, necessário para a entrada da CNN.
- **`to_categorical(y_train, 10)`**: Converte os rótulos para *one-hot encoding*, onde cada rótulo é representado por um vetor binário (exemplo: `3 → [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]`).

---

### **3. Construir a CNN**
```python
modelo = Sequential()
modelo.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
modelo.add(MaxPooling2D(pool_size=(2, 2)))
modelo.add(Conv2D(64, (3, 3), activation='relu'))
modelo.add(MaxPooling2D(pool_size=(2, 2)))
modelo.add(Flatten())
modelo.add(Dense(128, activation='relu'))
modelo.add(Dense(10, activation='softmax'))
```
- **`Sequential()`**: Cria um modelo sequencial.
- **`add(Conv2D(...))`**: Adiciona uma camada convolucional:
  - `32`: Número de filtros.
  - `(3, 3)`: Tamanho dos filtros (janela de convolução).
  - `activation='relu'`: Função de ativação ReLU (Retified Linear Unit), que remove valores negativos.
  - `input_shape=(28, 28, 1)`: Forma da entrada (imagens de 28x28 com 1 canal).
- **`add(MaxPooling2D(...))`**: Adiciona uma camada de pooling para reduzir a dimensão espacial.
- **`add(Flatten())`**: Achata os dados para uma única dimensão.
- **`add(Dense(...))`**: Adiciona camadas totalmente conectadas:
  - `128`: Número de neurónios na camada intermediária.
  - `10`: Número de neurónios na camada de saída (um para cada dígito).
  - `activation='softmax'`: Função de ativação para classificação multiclasse.

---

### **4. Compilar e Treinar o Modelo**
```python
modelo.compile(optimizer='adam',
               loss='categorical_crossentropy',
               metrics=['accuracy'])
historico = modelo.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
```
- **`compile(...)`**: Configura o modelo:
  - `optimizer='adam'`: Usa o otimizador Adam para ajustar os pesos.
  - `loss='categorical_crossentropy'`: Função de perda para classificação multiclasse.
  - `metrics=['accuracy']`: Mede a precisão durante o treino.
- **`fit(...)`**: Treina o modelo:
  - `epochs=5`: Número de vezes que o modelo verá todo o conjunto de treino.
  - `batch_size=32`: Tamanho do lote (quantidade de amostras processadas por vez).
  - `validation_split=0.2`: Usa 20% do conjunto de treino para validação.

---

### **5. Avaliar o Modelo**
```python
perda, precisao = modelo.evaluate(x_test, y_test)
print(f"Precisão no conjunto de teste: {precisao*100:.2f}%")
```
- **`evaluate(x_test, y_test)`**: Avalia o desempenho do modelo no conjunto de teste.
- **`perda`**: Valor da função de perda.
- **`precisao`**: Precisão do modelo no conjunto de teste.

---

### **6. Visualizar os Resultados**
```python
plt.plot(historico.history['accuracy'], label='Precisão Treino')
plt.plot(historico.history['val_accuracy'], label='Precisão Validação')
plt.xlabel('Época')
plt.ylabel('Precisão')
plt.legend()
plt.title('Desempenho da CNN')
plt.show()
```
- **`plt.plot(...)`**: Plota a precisão ao longo das épocas.
- **`plt.xlabel` e `plt.ylabel`**: Define os rótulos dos eixos.
- **`plt.legend()`**: Mostra a legenda dos gráficos.
- **`plt.title()`**: Adiciona um título ao gráfico.
- **`plt.show()`**: Exibe o gráfico.

---

### **7. Fazer Previsões**
```python
amostra = x_test[:5]
previsoes = modelo.predict(amostra)
for i, pred in enumerate(previsoes):
    plt.imshow(amostra[i].reshape(28, 28), cmap='gray')
    plt.title(f"Previsão: {pred.argmax()}")
    plt.show()
```
- **`predict(amostra)`**: Faz previsões para as primeiras 5 imagens do conjunto de teste.
- **`pred.argmax()`**: Retorna o índice do maior valor, que corresponde à classe prevista.
- **`plt.imshow()`**: Exibe cada imagem.
- **`plt.title()`**: Adiciona a previsão como título.
Para instalar o módulo **TensorFlow** no Windows 10, siga estes passos:

---

### **1. Verifique a versão do Python**
TensorFlow requer **Python 3.7 ou superior**. Abra o terminal (Prompt de Comando, PowerShell ou terminal do VS Code) e execute:
```bash
python --version
```
Se a versão for inferior a 3.7, atualize o Python [a partir do site oficial](https://www.python.org/downloads/).

---

### **2. Instale o TensorFlow**
No terminal, use o comando **`pip`** para instalar o TensorFlow:
```bash
pip install tensorflow
```

---

### **3. Verifique a instalação**
Após a instalação, confirme se o TensorFlow foi instalado corretamente executando:
```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```
Este comando deve retornar a versão do TensorFlow instalada, como por exemplo:
```
2.13.0
```

---

### **4. Resolução de possíveis erros**
- **Erro: "pip não é reconhecido"**  
  Certifique-se de que o Python e o `pip` estão adicionados ao PATH do sistema. Reinstale o Python e marque a opção **"Add Python to PATH"**.

- **Erro de versão incompatível**  
  Certifique-se de que está usando uma versão de Python compatível com TensorFlow.

- **Erro de dependências**  
  Atualize o `pip` antes da instalação:
  ```bash
  python -m pip install --upgrade pip
  ```

---

### **5. GPU (opcional)**
Se você deseja usar o TensorFlow com suporte a GPU (para maior desempenho), siga estas etapas adicionais:
1. Instale os drivers necessários da NVIDIA (CUDA e cuDNN).
2. Verifique os requisitos de versão no [guia oficial do TensorFlow](https://www.tensorflow.org/install/gpu).
3. Instale a versão GPU:
   ```bash
   pip install tensorflow
   ```
