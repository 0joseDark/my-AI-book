## **Configuração do Ambiente AI no Windows**

### **1. Pré-requisitos**
Antes de configurar o ambiente, certifique-se de que o seu sistema atende aos seguintes requisitos:
- Windows 10 ou superior.
- Processador compatível com 64 bits.
- Pelo menos 8 GB de RAM (16 GB ou mais recomendados).
- Espaço em disco suficiente (30 GB ou mais dependendo das ferramentas e datasets).

---

### **2. Instalação de Ferramentas Essenciais**

#### **2.1 Python**
1. **Baixar e instalar:**
   - Acesse o site oficial do [Python](https://www.python.org/downloads/).
   - Baixe a versão mais recente do Python para Windows (64 bits).
   - Durante a instalação, marque a opção **"Add Python to PATH"**.

2. **Verificar a instalação:**
   ```bash
   python --version
   pip --version
   ```

#### **2.2 Gerenciador de Pacotes Conda**
Conda é útil para gerenciar ambientes virtuais e dependências:
1. **Instalar o Miniconda ou Anaconda:**
   - Baixe o [Miniconda](https://docs.conda.io/en/latest/miniconda.html) ou o [Anaconda](https://www.anaconda.com/).

2. **Configurar o ambiente:**
   ```bash
   conda create -n ai_env python=3.10
   conda activate ai_env
   ```

#### **2.3 IDE para Desenvolvimento**
Escolha uma IDE para programar:
1. **Visual Studio Code:**
   - Baixe e instale o [VS Code](https://code.visualstudio.com/).
   - Instale extensões úteis: Python, Jupyter, e Pylance.
2. **Jupyter Notebook:**
   ```bash
   pip install jupyter notebook
   ```

---

### **3. Instalação de Bibliotecas AI**
Instale as bibliotecas necessárias para IA:
1. **Numpy e Pandas:**
   ```bash
   pip install numpy pandas
   ```
2. **Matplotlib e Seaborn (Visualização):**
   ```bash
   pip install matplotlib seaborn
   ```
3. **Scikit-learn (Machine Learning):**
   ```bash
   pip install scikit-learn
   ```
4. **TensorFlow (Deep Learning):**
   ```bash
   pip install tensorflow
   ```
5. **PyTorch (Deep Learning):**
   ```bash
   pip install torch torchvision torchaudio
   ```
6. **OpenCV (Visão Computacional):**
   ```bash
   pip install opencv-python
   ```
7. **NLTK e SpaCy (Processamento de Linguagem Natural):**
   ```bash
   pip install nltk spacy
   python -m spacy download en_core_web_sm
   ```

---

### **4. Configuração de GPU (Opcional)**
Se você possui uma GPU compatível com CUDA, configure-a para acelerar os treinamentos:
1. **Instalar drivers NVIDIA:**
   - Baixe os drivers mais recentes para a sua GPU no site oficial da [NVIDIA](https://www.nvidia.com/Download/index.aspx).
2. **Instalar CUDA Toolkit:**
   - Baixe o [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads).
3. **Instalar cuDNN:**
   - Baixe o [cuDNN](https://developer.nvidia.com/cudnn).

Certifique-se de que o TensorFlow ou PyTorch detecta a GPU:
```bash
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
python -c "import torch; print(torch.cuda.is_available())"
```

---

### **5. Configuração de Ferramentas Adicionais**

#### **5.1 Controle de Versão com Git**
1. **Instalar o Git:**
   - Baixe do site oficial: [Git para Windows](https://git-scm.com/download/win).
2. **Configurar o Git:**
   ```bash
   git config --global user.name "Seu Nome"
   git config --global user.email "seu@email.com"
   ```

#### **5.2 Docker (Para Contêineres)**
1. **Instalar o Docker Desktop:**
   - Baixe do site oficial: [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. **Configurar o Docker para Windows:**
   - Habilite o WSL 2 durante a instalação.

---

### **6. Testando o Ambiente**
1. Crie um script Python básico para verificar a instalação:
   ```python
   import numpy as np
   import tensorflow as tf
   import torch

   print("NumPy Version:", np.__version__)
   print("TensorFlow Version:", tf.__version__)
   print("PyTorch Version:", torch.__version__)
   ```

2. Execute o script:
   ```bash
   python test_env.py
   ```

---

### **7. Manutenção e Atualização**
- Atualize regularmente o Python e as bibliotecas:
  ```bash
  pip install --upgrade pip
  pip list --outdated
  pip install --upgrade <pacote>
  ```

- Mantenha seus ambientes organizados usando **conda** ou **virtualenv**.
