### **Configuração do Ambiente AI em Ubuntu/Linux**

#### **1. Atualizar o Sistema**
Execute o seguinte comando para atualizar os pacotes existentes e o sistema:
```bash
sudo apt update && sudo apt upgrade -y
```

#### **2. Instalar Python e Pip**
Garanta que você tenha o Python 3.8 ou superior:
```bash
sudo apt install python3 python3-pip -y
```
Verifique as versões:
```bash
python3 --version
pip3 --version
```

#### **3. Instalar o Gerenciador de Ambientes Virtuais**
Crie ambientes isolados para seus projetos:
```bash
sudo apt install python3-venv -y
```

#### **4. Instalar NVIDIA Drivers e CUDA (Para GPU NVIDIA)**
Se você planeja usar uma GPU NVIDIA para acelerar o treinamento de modelos:
- Verifique sua GPU:
  ```bash
  lspci | grep -i nvidia
  ```
- Instale os drivers NVIDIA:
  ```bash
  sudo apt install nvidia-driver-515 -y
  ```
- Instale o CUDA Toolkit:
  Baixe e instale o pacote do [site oficial da NVIDIA](https://developer.nvidia.com/cuda-toolkit).

#### **5. Instalar Frameworks e Bibliotecas Necessárias**
Certifique-se de que seu ambiente tem as bibliotecas populares de AI:
```bash
pip3 install numpy pandas matplotlib seaborn
pip3 install scikit-learn
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip3 install tensorflow
pip3 install jupyterlab
```

#### **6. Instalar Ferramentas Adicionais**
- **IDE ou Editor de Código**:
  - Visual Studio Code:
    ```bash
    sudo snap install code --classic
    ```
  - PyCharm:
    ```bash
    sudo snap install pycharm-community --classic
    ```
- **Git**:
  ```bash
  sudo apt install git -y
  ```

#### **7. Configurar Jupyter Notebook**
Configure o Jupyter Notebook para usar com projetos de AI:
```bash
pip3 install notebook
jupyter notebook
```

#### **8. Instalar Docker (Opcional para Ambientes Isolados)**
Docker é útil para criar ambientes portáteis e consistentes:
```bash
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

#### **9. Instalar OpenCV (Para Processamento de Imagem)**
```bash
pip3 install opencv-python opencv-contrib-python
```

#### **10. Configurar um Ambiente Deep Learning Completo (Opcional)**
- Instale o Anaconda (uma distribuição Python completa para Data Science e AI):
  1. Baixe o instalador do [site oficial da Anaconda](https://www.anaconda.com).
  2. Instale o Anaconda:
     ```bash
     bash Anaconda3-*.sh
     ```
  3. Crie um ambiente:
     ```bash
     conda create -n ai python=3.9
     conda activate ai
     ```

#### **11. Testar a Configuração**
Crie um script Python para verificar as instalações:
```python
import numpy as np
import tensorflow as tf
import torch

print("NumPy versão:", np.__version__)
print("TensorFlow versão:", tf.__version__)
print("PyTorch versão:", torch.__version__)
```

Salve como `test_env.py` e execute:
```bash
python3 test_env.py
```

#### **12. Documentar a Configuração**
Crie um arquivo README.md para manter um registro da configuração e as versões instaladas.
