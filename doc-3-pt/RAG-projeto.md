

Um projeto **RAG (Robô Autônomo Guiado)** com visão e capacidade de aprender e mapear caminhos em **Windows 10** pode ser desenvolvido utilizando Python e bibliotecas como **OpenCV** (para visão computacional), **NumPy** (para cálculos matemáticos), e um algoritmo de aprendizado como **Q-learning** para ensinar o robô a navegar e mapear caminhos.
---

### **1. Estrutura do Projeto**
**Objetivos:**
- Criar um robô virtual com sensores de visão (câmera).
- Mapear o ambiente com base nos dados da câmera.
- Aprender a navegar utilizando um algoritmo de aprendizado por reforço.

**Componentes:**
1. **Simulação do ambiente**:
   - Usaremos uma janela gráfica para representar o robô e o ambiente.
2. **Câmera (simulada ou real)**:
   - Utilizar uma fonte de vídeo (câmera USB ou gravação) para processar imagens.
3. **Algoritmo de navegação**:
   - Q-learning para decisão de movimentos.
4. **Mapeamento do ambiente**:
   - Representar o ambiente em uma matriz 2D ou gráfico.

---

### **2. Ferramentas e Bibliotecas**
Instale as bibliotecas necessárias com os seguintes comandos no terminal/prompt:

```bash
pip install opencv-python-headless numpy matplotlib pygame
```

---

### **3. Estrutura do Código**
#### **A. Inicialização do Ambiente**
Inclui a criação da janela gráfica e o controle do robô.

```python
import pygame
import numpy as np

# Configurações iniciais
LARGURA, ALTURA = 800, 600
TAMANHO_ROBO = 20

# Iniciar o pygame
pygame.init()
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("RAG - Robô Autônomo Guiado")
relogio = pygame.time.Clock()

# Posição inicial do robô
posicao_robo = [LARGURA // 2, ALTURA // 2]
velocidade = 5
```

---

#### **B. Simulação de Visão**
Usaremos OpenCV para processar uma câmera ou vídeo.

```python
import cv2

# Inicializar a câmera (ou usar vídeo simulado)
camera = cv2.VideoCapture(0)  # Altere para um arquivo de vídeo se necessário

def processar_visao():
    ret, frame = camera.read()
    if ret:
        # Converter para escala de cinza
        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detecção de bordas para obstáculos
        bordas = cv2.Canny(cinza, 100, 200)
        return bordas
    return None
```

---

#### **C. Mapeamento do Ambiente**
Representamos o ambiente em uma matriz 2D, onde cada célula indica se está livre ou ocupada.

```python
MAPA = np.zeros((ALTURA // TAMANHO_ROBO, LARGURA // TAMANHO_ROBO))

def atualizar_mapa(bordas):
    global MAPA
    for y in range(0, bordas.shape[0], TAMANHO_ROBO):
        for x in range(0, bordas.shape[1], TAMANHO_ROBO):
            if bordas[y, x] > 0:  # Borda detectada
                MAPA[y // TAMANHO_ROBO, x // TAMANHO_ROBO] = 1  # Obstáculo
```

---

#### **D. Navegação e Aprendizado**
Usamos o algoritmo **Q-learning** para decidir as ações do robô.

```python
AÇÕES = ['cima', 'baixo', 'esquerda', 'direita']
q_table = np.zeros((MAPA.shape[0], MAPA.shape[1], len(AÇÕES)))

def escolher_acao(estado, epsilon=0.1):
    if np.random.rand() < epsilon:
        return np.random.choice(len(AÇÕES))  # Explorar
    return np.argmax(q_table[estado])  # Exploitar

def atualizar_q_table(estado, acao, recompensa, proximo_estado, alpha=0.1, gamma=0.9):
    max_proximo = np.max(q_table[proximo_estado])
    q_table[estado][acao] += alpha * (recompensa + gamma * max_proximo - q_table[estado][acao])
```

---

#### **E. Loop Principal**
Combina a visão, mapeamento e navegação.

```python
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Processar visão
    bordas = processar_visao()
    if bordas is not None:
        atualizar_mapa(bordas)

    # Atualizar posição do robô baseado no Q-learning
    estado_atual = (posicao_robo[1] // TAMANHO_ROBO, posicao_robo[0] // TAMANHO_ROBO)
    acao = escolher_acao(estado_atual)

    if AÇÕES[acao] == 'cima':
        posicao_robo[1] -= velocidade
    elif AÇÕES[acao] == 'baixo':
        posicao_robo[1] += velocidade
    elif AÇÕES[acao] == 'esquerda':
        posicao_robo[0] -= velocidade
    elif AÇÕES[acao] == 'direita':
        posicao_robo[0] += velocidade

    # Atualizar tela
    janela.fill((0, 0, 0))  # Preencher com preto
    pygame.draw.rect(janela, (0, 255, 0), (*posicao_robo, TAMANHO_ROBO, TAMANHO_ROBO))
    pygame.display.flip()
    relogio.tick(30)

# Encerrar
pygame.quit()
camera.release()
cv2.destroyAllWindows()
```

---

### **4. Explicação do Funcionamento**
1. **Visão e Mapeamento**:
   - O robô captura imagens usando a câmera.
   - Processamos as imagens para detectar obstáculos e atualizar o mapa.

2. **Aprendizado por Reforço**:
   - O robô explora o ambiente e aprende o melhor caminho para evitar obstáculos.

3. **Simulação**:
   - A janela gráfica exibe o robô movendo-se no ambiente enquanto atualiza o mapa.

---

### **5. Melhorias Futuros**
- Adicionar sensores ultrassônicos reais para obstáculos.
- Implementar controle PID para maior precisão nos movimentos.
- Conectar o robô a um microcontrolador (como o Arduino) para controlar o hardware.
