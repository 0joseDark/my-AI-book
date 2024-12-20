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

