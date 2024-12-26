O **PicoYOLO** é uma versão leve do algoritmo YOLO (You Only Look Once) para detecção de objetos. Ele é otimizado para dispositivos com recursos limitados, como microcontroladores e sistemas embarcados. Para usar o PicoYOLO no Windows 10, em português europeu, o processo envolve instalar as dependências, configurar o ambiente e executar o modelo. Aqui está um guia detalhado:

---

### **1. Pré-requisitos**
Antes de começar, certifique-se de ter o seguinte:
- Um PC com Windows 10.
- Acesso à internet para baixar pacotes e dependências.
- Python 3.7 ou superior instalado.

---

### **2. Instalar Python e configurar o ambiente**
1. **Instalar o Python:**
   - Faça download do Python [aqui](https://www.python.org/downloads/).
   - Durante a instalação, selecione a opção **"Add Python to PATH"**.

2. **Criar um ambiente virtual:**
   - Abra o **Prompt de Comando** ou **PowerShell**.
   - Crie um ambiente virtual:
     ```bash
     python -m venv picoYOLO_env
     ```
   - Ative o ambiente:
     ```bash
     picoYOLO_env\Scripts\activate
     ```

---

### **3. Instalar dependências**
1. Instale o **PyTorch** e **TorchVision** (requisitos para o PicoYOLO):
   ```bash
   pip install torch torchvision
   ```

2. Instale outras dependências necessárias:
   ```bash
   pip install numpy matplotlib opencv-python
   ```

3. Se o projeto PicoYOLO estiver num repositório GitHub, clone-o:
   ```bash
   git clone https://github.com/<repositorio-picoyolo>.git
   cd picoyolo
   ```

4. Instale os requisitos do projeto:
   ```bash
   pip install -r requirements.txt
   ```

---

### **4. Configurar o modelo PicoYOLO**
1. **Obter os pesos pré-treinados:**
   - Faça download dos pesos pré-treinados para o PicoYOLO, geralmente disponibilizados como ficheiros `.pth` ou `.weights` no repositório.

2. **Editar o ficheiro de configuração:**
   - Localize o ficheiro de configuração do modelo (ex.: `config.py` ou `model_config.json`).
   - Atualize as configurações, como o caminho para os pesos e os parâmetros de entrada/saída.

3. **Configurar classes:**
   - No ficheiro de classes (ex.: `coco.names` ou `classes.txt`), liste os nomes das classes que o modelo deve reconhecer.

---

### **5. Testar o PicoYOLO**
1. **Executar o modelo:**
   - Use o script principal do repositório para detecção de objetos:
     ```bash
     python detect.py --image caminho_da_imagem.jpg
     ```
   - Substitua `detect.py` pelo script correto do repositório.

2. **Parâmetros adicionais:**
   - Para usar uma webcam ou vídeo:
     ```bash
     python detect.py --video caminho_do_video.mp4
     ```
   - Para salvar resultados:
     ```bash
     python detect.py --save_output caminho_do_output
     ```

---

### **6. Visualizar resultados**
1. Certifique-se de que a saída do modelo está configurada para salvar imagens ou vídeos com as detecções.
2. Use **OpenCV** ou **Matplotlib** para visualizar os resultados:
   ```python
   import cv2
   image = cv2.imread("resultado.jpg")
   cv2.imshow("Resultado", image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

---

### **7. Treinar o PicoYOLO (opcional)**
Se desejar treinar o modelo com um novo conjunto de dados:
1. **Preparar os dados:**
   - Organize os dados no formato YOLO, com imagens e ficheiros de anotação `.txt`.

2. **Configurar o treino:**
   - Edite o ficheiro de treino (ex.: `train.py`) para incluir o caminho para os dados e pesos iniciais.

3. **Executar o treino:**
   ```bash
   python train.py --data caminho_dos_dados --weights pesos_iniciais.pth
   ```

---

### **8. Problemas comuns e soluções**
1. **Erro de CUDA:**
   - Se o seu PC não tiver GPU compatível, force o uso de CPU:
     ```python
     device = torch.device("cpu")
     ```

2. **Dependências faltantes:**
   - Certifique-se de instalar todos os pacotes listados no ficheiro `requirements.txt`.

### **1. Identificar as dependências do projeto**
- Se você já tem um ambiente virtual configurado com os pacotes instalados, pode gerar o ficheiro automaticamente.
- Caso contrário, liste manualmente os pacotes que o projeto precisa.

---

### **2. Criar o ficheiro `requirements.txt` automaticamente**
1. **Ative o ambiente virtual:**
   ```bash
   picoYOLO_env\Scripts\activate
   ```
   
2. **Liste os pacotes instalados:**
   Execute o seguinte comando:
   ```bash
   pip freeze > requirements.txt
   ```
   Isso criará um ficheiro `requirements.txt` com os pacotes e versões instalados no ambiente virtual.

3. **Exemplo de saída gerada:**
   O ficheiro `requirements.txt` pode ter uma aparência semelhante a esta:
   ```
   numpy==1.24.3
   torch==2.0.1
   torchvision==0.15.2
   opencv-python==4.5.5.64
   matplotlib==3.7.2
   ```

---

### **3. Criar manualmente o ficheiro `requirements.txt`**
Se você quiser criar o ficheiro manualmente:
1. Abra um editor de texto (ex.: Notepad).
2. Liste os nomes dos pacotes e suas versões, como no exemplo acima.
3. Salve o ficheiro com o nome `requirements.txt` no diretório do projeto.

---

### **4. Instalar dependências a partir do ficheiro**
Quando outra pessoa (ou você mesmo, em outro ambiente) quiser configurar o projeto, basta usar:
```bash
pip install -r requirements.txt
```
Este comando instala todos os pacotes listados no ficheiro.

---

### **5. Boas práticas**
- Inclua as versões dos pacotes para evitar problemas de incompatibilidade.
- Atualize o ficheiro sempre que adicionar ou remover pacotes do projeto.
- Para projetos longos, considere separar requisitos opcionais em ficheiros adicionais, como `requirements-dev.txt`.
