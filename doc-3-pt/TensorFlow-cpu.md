### **O que é TensorFlow?**

O TensorFlow é uma biblioteca open-source desenvolvida pela Google para machine learning e inteligência artificial. Ele oferece ferramentas para desenvolver e treinar redes neurais, além de trabalhar com tarefas como classificação, regressão, processamento de linguagem natural e visão computacional.

### **Por que usar TensorFlow para CPU?**

Embora o TensorFlow suporte GPUs para aceleração de cálculos, muitos projetos podem ser executados apenas com CPUs, especialmente em máquinas sem GPUs dedicadas ou em tarefas que não exijam grande poder computacional.

**Vantagens:**
- Compatibilidade: Funciona em qualquer máquina com suporte básico para Python.
- Fácil configuração: Não requer instalação de drivers de GPU.
- Eficiência para tarefas pequenas ou médias.

---

### **Instalação do TensorFlow para CPU**

1. **Configurar ambiente Python:**
   Recomenda-se criar um ambiente virtual para evitar conflitos com outras bibliotecas.

   ```bash
   python -m venv tf_cpu_env
   source tf_cpu_env/bin/activate  # Linux/Mac
   tf_cpu_env\Scripts\activate     # Windows
   ```

2. **Instalar TensorFlow para CPU:**
   A versão padrão do TensorFlow já inclui suporte para CPUs.

   ```bash
   pip install tensorflow
   ```

3. **Verificar instalação:**
   Após a instalação, confirme que o TensorFlow está funcionando.

   ```python
   import tensorflow as tf
   print(tf.__version__)
   ```

---

### **Exemplo de uso: Treinamento de um modelo básico com CPU**

Aqui está um exemplo de como criar e treinar um modelo de classificação com TensorFlow usando apenas a CPU.

#### **1. Importar bibliotecas**
```python
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
```

#### **2. Gerar dados sintéticos**
```python
# Gerar dados para classificação
X, y = make_classification(
    n_samples=1000, n_features=20, n_classes=2, random_state=42
)

# Dividir em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### **3. Criar o modelo**
```python
# Modelo simples de rede neural
model = Sequential([
    Dense(64, activation='relu', input_shape=(20,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilar o modelo
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

#### **4. Treinar o modelo**
```python
# Treinamento
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
```

#### **5. Avaliar o modelo**
```python
# Avaliar no conjunto de teste
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")
```

---

### **Otimização para CPUs**

1. **Configurar threads:**
   O TensorFlow permite ajustar o número de threads para execução em CPU.

   ```python
   import tensorflow as tf
   tf.config.threading.set_intra_op_parallelism_threads(4)
   tf.config.threading.set_inter_op_parallelism_threads(2)
   ```

2. **Desativar GPU explicitamente:**
   Se a máquina tiver uma GPU, mas você quiser usar apenas a CPU:

   ```python
   import os
   os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
   ```

---

### **Recursos Adicionais**
- **Documentação oficial:** [TensorFlow](https://www.tensorflow.org/)
- **Guias de otimização para CPU:** TensorFlow oferece suporte para aceleração via bibliotecas como Intel MKL em CPUs Intel.