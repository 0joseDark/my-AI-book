### **AI Environment Setup on Ubuntu/Linux**

#### **1. Update the System**
Run the following command to update existing packages and the system:
```bash
sudo apt update && sudo apt upgrade -y
```

#### **2. Install Python and Pip**
Ensure you have Python 3.8 or higher:
```bash
sudo apt install python3 python3-pip -y
```
Check the versions:
```bash
python3 --version
pip3 --version
```

#### **3. Install Virtual Environment Manager**
Create isolated environments for your projects:
```bash
sudo apt install python3-venv -y
```

#### **4. Install NVIDIA Drivers and CUDA (For NVIDIA GPU)**
If you plan to use an NVIDIA GPU to accelerate model training:
- Check your GPU:
  ```bash
  lspci | grep -i nvidia
  ```
- Install NVIDIA drivers:
  ```bash
  sudo apt install nvidia-driver-515 -y
  ```
- Install the CUDA Toolkit:
  Download and install the package from the [official NVIDIA site](https://developer.nvidia.com/cuda-toolkit).

#### **5. Install Necessary Frameworks and Libraries**
Ensure your environment has popular AI libraries:
```bash
pip3 install numpy pandas matplotlib seaborn
pip3 install scikit-learn
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip3 install tensorflow
pip3 install jupyterlab
```

#### **6. Install Additional Tools**
- **IDE or Code Editor**:
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

#### **7. Configure Jupyter Notebook**
Set up Jupyter Notebook for use with AI projects:
```bash
pip3 install notebook
jupyter notebook
```

#### **8. Install Docker (Optional for Isolated Environments)**
Docker is useful for creating portable and consistent environments:
```bash
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

#### **9. Install OpenCV (For Image Processing)**
```bash
pip3 install opencv-python opencv-contrib-python
```

#### **10. Set Up a Complete Deep Learning Environment (Optional)**
- Install Anaconda (a comprehensive Python distribution for Data Science and AI):
  1. Download the installer from the [official Anaconda website](https://www.anaconda.com).
  2. Install Anaconda:
     ```bash
     bash Anaconda3-*.sh
     ```
  3. Create an environment:
     ```bash
     conda create -n ai python=3.9
     conda activate ai
     ```

#### **11. Test the Setup**
Create a Python script to verify the installations:
```python
import numpy as np
import tensorflow as tf
import torch

print("NumPy version:", np.__version__)
print("TensorFlow version:", tf.__version__)
print("PyTorch version:", torch.__version__)
```

Save it as `test_env.py` and run:
```bash
python3 test_env.py
```

#### **12. Document the Setup**
Create a `README.md` file to keep a record of the configuration and installed versions.
